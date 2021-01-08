package ost_sm_2020_proj;

import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.streaming.api.functions.KeyedProcessFunction;
import org.apache.flink.util.Collector;
import org.apache.flink.walkthrough.common.entity.Alert;

public class ProcessPredictions extends KeyedProcessFunction<Integer, Tuple2<Integer, String>, Alert> {

    private String label;

    public ProcessPredictions(String label) {
        this.label = label;
    }
@Override
public void processElement(
        Tuple2<Integer, String> prediction,
        Context context,
        Collector<Alert> collector) throws Exception {
        if ( prediction.f1.equalsIgnoreCase(label) ) {

            Alert alert = new Alert();

            alert.setId( prediction.f0 );

            collector.collect(alert);
        }
    }
}
