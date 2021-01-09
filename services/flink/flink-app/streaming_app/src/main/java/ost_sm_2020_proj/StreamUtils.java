package ost_sm_2020_proj;

import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.json.JSONObject;

public class StreamUtils {

    public static DataStreamSource<JSONObject> getStreamingData(StreamExecutionEnvironment env,String url) {

        DataStreamSource<JSONObject> dataStream = env
                .addSource(new CustomSource(url));

        return dataStream;
    }
}
