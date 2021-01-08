package ost_sm_2020_proj;

import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.functions.KeyedProcessFunction;
import org.apache.flink.streaming.connectors.cassandra.CassandraSink;
import org.apache.flink.util.Collector;
import org.apache.flink.walkthrough.common.entity.Alert;
import org.apache.flink.walkthrough.common.sink.AlertSink;
import org.json.JSONObject;

public class PredictionMain {

    public static void main(String [] args) throws Exception {
        String url = "http://localhost:8000/non_vpn/test/challenge";

        StreamExecutionEnvironment env = StreamExecutionEnvironment
                .getExecutionEnvironment();

        DataStreamSource<JSONObject> dataStream = StreamUtils.getStreamingData(env, url);

        DataStream<Tuple2<Integer, String>> preds =
                dataStream.map(new PredictionMapping());

        preds.print();

        CassandraSink.addSink( preds )
                .setQuery("INSERT INTO ost_sm_2020.predictions_sink (id, label) VALUES(?, ?)")
                .setHost("127.0.0.1")
                .build();

        // Raise an alert when some flow is detected
        DataStream<Alert> alerts =
                dataStream.map(new PredictionMapping())
                .keyBy(p -> p.f0)
                .process(new ProcessPredictions("Chatting"));

        alerts.addSink(new AlertSink());

        env.execute("Predictions Streaming");
    }
}
