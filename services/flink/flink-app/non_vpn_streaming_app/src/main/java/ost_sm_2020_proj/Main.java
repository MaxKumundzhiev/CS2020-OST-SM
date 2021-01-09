package ost_sm_2020_proj;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.windowing.assigners.TumblingProcessingTimeWindows;
import org.apache.flink.streaming.api.windowing.time.Time;
import org.apache.flink.streaming.connectors.cassandra.CassandraSink;
import org.json.JSONObject;

public class Main {
    public static void main(String args[]) throws Exception {

        String url = "http://localhost:8000/non_vpn";

        StreamExecutionEnvironment env = StreamExecutionEnvironment
                .getExecutionEnvironment();

        DataStreamSource<JSONObject> dataStream = StreamUtils.getStreamingData(env, url);

        // Transformation #1
        // number of flows grouped by the label

        DataStream<Tuple2<String, Integer>> flowsCounter = dataStream
                .map(new DataFlowTypeSplitter())
                .keyBy(flow -> flow.f0)
                .sum(1);

        flowsCounter.print();

        CassandraSink.addSink( flowsCounter )
                .setQuery("INSERT INTO ost_sm_2020.flows_count_sink (label, count) VALUES(?, ?)")
                .setHost("127.0.0.1")
                .build();

        // Transformation #2
        // average # of bytes sent to http or dns application in a  5-second window

        DataStream<Tuple2<Integer, Double>> httpDnsFlows = dataStream
                .filter(new PortFilter())
                .map(new DataFlowMapFunction())
                .keyBy(flow -> flow.f0)
                .window(TumblingProcessingTimeWindows.of(Time.seconds(5)))
                .reduce(new ReduceAvgFunction());

        httpDnsFlows.print();

        CassandraSink.addSink( httpDnsFlows )
                .setQuery("INSERT INTO ost_sm_2020.bytes_in_avg_sink (id, dst_port, bytes_in_avg) VALUES(toTimeStamp( now()), ?, ?)")
                .setHost("127.0.0.1")
                .build();

        env.execute("FilterDataFlows");
    }
}
