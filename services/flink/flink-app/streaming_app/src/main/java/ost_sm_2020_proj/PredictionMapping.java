package ost_sm_2020_proj;

import org.apache.flink.api.common.functions.FlatMapFunction;
import org.apache.flink.api.common.functions.MapFunction;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.util.Collector;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class PredictionMapping implements MapFunction<JSONObject, Tuple2<Integer, String>> {

    private static final String model_url = "http://localhost:8050/predict";

    @Override
    public Tuple2<Integer, String> map(JSONObject jsonObject) throws Exception {
        String jsonInputString = jsonObject.toString();

        URL url = new URL(model_url);
        HttpURLConnection con = (HttpURLConnection)url.openConnection();
        con.setRequestMethod("POST");

        con.setRequestProperty("Content-Type", "application/json; utf-8");
        con.setRequestProperty("Accept", "application/json");
        con.setDoOutput(true);

        try(OutputStream os = con.getOutputStream()) {
            byte[] input = jsonInputString.getBytes("utf-8");
            os.write(input, 0, input.length);
        }

        JSONObject jsonResponse;

        try(BufferedReader reader =
                    new BufferedReader(
                            new InputStreamReader(con.getInputStream()))) {
            String res = reader.readLine();

            jsonResponse = new JSONObject(res);
        }

        return new Tuple2<>( jsonResponse.getInt("id"), jsonResponse.getString("label"));
    }
}
