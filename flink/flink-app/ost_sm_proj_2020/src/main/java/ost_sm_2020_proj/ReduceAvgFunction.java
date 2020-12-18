package ost_sm_2020_proj;

import org.apache.flink.api.common.functions.FlatMapFunction;
import org.apache.flink.api.common.functions.ReduceFunction;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.util.Collector;
import org.json.JSONObject;

public class ReduceAvgFunction implements ReduceFunction<Tuple2<Integer, Double>> {

    @Override
    public Tuple2<Integer, Double> reduce(Tuple2<Integer, Double> flow1,
                                  Tuple2<Integer, Double> flow2) throws Exception {

        double running_avg = (flow1.f1 + flow2.f1) / 2;
        return  new Tuple2<>(flow2.f0, running_avg);
    }
}
