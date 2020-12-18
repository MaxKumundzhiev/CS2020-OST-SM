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
        StreamExecutionEnvironment env = StreamExecutionEnvironment
                .getExecutionEnvironment();

        DataStreamSource<JSONObject> dataStream = env
                .addSource(new CustomSource());

        // Transformation #1
        // number of flows grouped by the label

        DataStream<Tuple2<String, Integer>> flowsType = dataStream
                .flatMap(new DataFlowTypeSplitter())
                .keyBy(flow -> flow.f0)
                .sum(1);

        flowsType.print();

        // Transformation #2
        // average # of bytes sent to http or dns application every 5 seconds

        DataStream<Tuple2<Integer, Double>> httpDnsFlows = dataStream
                .filter(new DataFlowFilter())
                .map(new DataFlowMapFunction())
                .keyBy(flow -> flow.f0)
                .window(TumblingProcessingTimeWindows.of(Time.seconds(5)))
                .reduce(new ReduceAvgFunction());

        httpDnsFlows.print();

        CassandraSink.addSink( httpDnsFlows )
                .setQuery("INSERT INTO ost_sm_2020.bytes_in_avg_sink (dst_port, bytes_in_avg) VALUES(?, ?)")
                .setHost("127.0.0.1")
                .build();
        // TODO...

        env.execute("FilterStrings");
    }
}
