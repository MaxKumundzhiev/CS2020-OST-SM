package ost_sm_2020_proj;

import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.json.JSONObject;

public class Main {
    public static void main(String args[]) throws Exception {
        StreamExecutionEnvironment env = StreamExecutionEnvironment
                .getExecutionEnvironment();

        DataStreamSource<JSONObject> dataStream = env
                .addSource(new CustomSource());

        // get all http[s] packets info


        // Count # of http and dns flows
        DataStream<Tuple2<Integer, Integer>> httpDnsFlows = dataStream
                .filter(new DataFlowFilter())
                .flatMap(new DataFlowSplitter())
                .keyBy(flow -> flow.f0 )
                .sum(1);

        // Add Cassandra sink
        // TODO...

        httpDnsFlows.print();

        env.execute("FilterStrings");
    }
}
