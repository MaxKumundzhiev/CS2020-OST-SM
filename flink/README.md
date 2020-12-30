<h1>Streaming Pipeline for Non-vpn2016 Using Cassandra Database as a storage and flink as streaming environment</h1>
<img width="300" height="300" src="Flink-Workflo.png" alt="Flink workflow" title="Flink Workflow" />
<h2>The system comprises the following components</h2>
<ul>
  <li>
    Cassandra Database instance
  </li>
  <li>RESTful api micro service that streams the data using a generator</li>
  <li>flink application has a custom data source that reads the data from the streaming api and transforms it into a JSON Object</li>
</ul>
<h2>Inside the flink application. We performed the following two transformations</h2>
<ul>
  <li>First transformation counts the number of each data flow type (chat, P2P,...)</li>
  <li>Second transformation calculates the average # of incoming bytes to a http or dns app in a time window of 5 seconds. It has two processing steps</li>
  <ul>
    <li>It filters the incoming flows based on destination port number, and keep only http and dns related flows</li>
    <li>It applies a Time windowing aggregation to calculate the avg # of incoming bytes during 5 seconds</li>
  </ul>
  <li>The results of both transformations are dumped to a Cassandra Database sink for further processing...</li>
</ul>
