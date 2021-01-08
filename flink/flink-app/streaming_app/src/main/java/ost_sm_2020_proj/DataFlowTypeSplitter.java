package ost_sm_2020_proj;

import org.apache.flink.api.common.functions.MapFunction;
import org.apache.flink.api.java.tuple.Tuple2;
import org.json.JSONObject;

public class DataFlowTypeSplitter implements MapFunction<JSONObject, Tuple2<String, Integer>> {

    @Override
    public Tuple2<String, Integer> map(JSONObject flow) throws Exception {
        return new Tuple2<>(flow.getString("label"), 1);
    }
}
