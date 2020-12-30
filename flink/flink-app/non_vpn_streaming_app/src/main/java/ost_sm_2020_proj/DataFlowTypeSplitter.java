package ost_sm_2020_proj;

import org.apache.flink.api.common.functions.FlatMapFunction;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.util.Collector;
import org.json.JSONObject;

public class DataFlowTypeSplitter implements FlatMapFunction<JSONObject, Tuple2<String, Integer>> {

    @Override
    public void flatMap(JSONObject flow, Collector<Tuple2<String, Integer>> collector) throws Exception {

        collector.collect(new Tuple2<>(flow.getString("label"), 1));
    }
}
