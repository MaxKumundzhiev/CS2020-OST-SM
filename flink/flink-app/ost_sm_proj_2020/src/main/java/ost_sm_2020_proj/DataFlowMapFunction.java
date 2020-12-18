package ost_sm_2020_proj;

import org.apache.flink.api.common.functions.MapFunction;
import org.apache.flink.api.java.tuple.Tuple2;
import org.json.JSONObject;

public class DataFlowMapFunction implements MapFunction<JSONObject, Tuple2<Integer, Double>> {
    @Override
    public Tuple2<Integer, Double> map(JSONObject flow) throws Exception {
        return new Tuple2<>(flow.getInt("dst_port"), flow.getDouble("bytes_in"));
    }
}
