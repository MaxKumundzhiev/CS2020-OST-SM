package ost_sm_2020_proj;

import org.apache.flink.api.common.functions.FlatMapFunction;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.util.Collector;
import org.json.JSONObject;

public class DataFlowSplitter implements FlatMapFunction<JSONObject,
        Tuple2< Integer, Integer > > {

    @Override
    public void flatMap(JSONObject flow, Collector<Tuple2<Integer, Integer>> collector) throws Exception {

        collector.collect(new Tuple2<>(flow.getInt("dst_port"), 1));
    }
}
