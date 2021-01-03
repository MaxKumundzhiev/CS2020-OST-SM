# Deploying Cassandra Database on windows

## Download and install Java development kit 8+
## Download and extract cassandra .tar file https://www.apache.org/dyn/closer.lua/cassandra/3.0.23/apache-cassandra-3.0.23-bin.tar.gz 
## Navigate to bin folder inside cassandra folder
## Run the command
```
cassandra.bat
```
## Cassandra provides CQL, a querying language that resembles to a large extent the traditional SQL. To usel CQL, run the command inside bin folder
```
cqlsh
```

## How to use the API

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
