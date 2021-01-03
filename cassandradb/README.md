<h1>Cassandra Database Storage part</h1>
### please refer to https://cassandra.apache.org/doc/latest/getting_started/installing.html for information on how to install cassandra database
<ul>
  <li>
    #### json_utils script file contains methods for parsing json files either line by line or in a batch fashion
  </li>
  <li>
    ### db_utils script exposes CassandraDb class which supports operations like creating a keyspace, creating partitions or tables inside a keyspace,insert a batch of json    records inside an existing partition, querying an existing partition, and last but least updating a batch of records...
  </li>
  <li>
    ### Cassandra connection parameters (ip address, port), and some partitions schemas are pre-defined inside config.py script
  </li>
</ul>

## Specific for flink part !!!!!

#### initialize a CassandraDb Class
```
db = CassandraDb(config["ip_addr"], config["port"])
```
#### create a keyspace with an arbitrary name
```
db.create_keyspace(keyspace)
```
#### Create a partition inside a keyspace
##### Please note that there is a method called build_schema for inferring the schema from features types but at the time of writing it only supports int, and float data types
```
db.create_table(keyspace, tablename, schema, order_by=...order the results by some clustering key...)
```
### load the data from a json file

```
  data = load_json_file(path_to_file, line_by_line=..., as_dataframe=False, preprocess=False)
```

### insert the data into an existing partition
```
  db.insert_batch_data(...)
```
