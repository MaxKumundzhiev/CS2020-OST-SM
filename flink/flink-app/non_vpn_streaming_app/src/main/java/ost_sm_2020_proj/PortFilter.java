package ost_sm_2020_proj;

import org.apache.flink.api.common.functions.FilterFunction;
import org.json.JSONObject;

public class PortFilter implements FilterFunction<JSONObject> {

    @Override
    public boolean filter(JSONObject flow) throws Exception {

        int dst_port = flow.getInt("dst_port");

        return  dst_port == 443 || dst_port == 53;
    }
}
