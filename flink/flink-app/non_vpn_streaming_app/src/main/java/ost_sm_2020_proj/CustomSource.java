package ost_sm_2020_proj;

import org.apache.flink.streaming.api.functions.source.SourceFunction;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;
import java.nio.charset.Charset;

public class CustomSource implements SourceFunction<JSONObject> {

    boolean isRunning = true;
    String url = "http://localhost:8000/non_vpn";

    @Override
    public void run(SourceContext<JSONObject> ctx) throws JSONException,
            IOException {
        InputStream is = new URL(url).openStream();

        BufferedReader rd = new BufferedReader(new InputStreamReader(
                is, Charset.forName("UTF-8")
        ));

        while ( !rd.readLine().isEmpty() && isRunning ) {
            String jsonText = rd.readLine();

            if( jsonText == null ) break;

            JSONObject flow = new JSONObject(jsonText);

            ctx.collect(flow);
        }

        rd.close();
    }

    @Override
    public void cancel() {
        isRunning = false;
    }
}
