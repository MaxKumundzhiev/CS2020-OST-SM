# Deploying Cassandra Database on windows

#### Download and install Java development kit 8+
#### Download and extract cassandra .tar file https://www.apache.org/dyn/closer.lua/cassandra/3.0.23/apache-cassandra-3.0.23-bin.tar.gz 
#### Navigate to bin folder inside cassandra folder
#### Run the command
```
cassandra.bat
```
#### Cassandra provides CQL, a querying language that resembles to a large extent the traditional SQL. To usel CQL, run the command inside bin folder
```
cqlsh
```

## We used Cassandra for storing

#### non-vpn2016 dataset 
#### the results of the transformations inside flink app

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
##### Please note that there is a method called build_schema for inferring the schema from features types. It supports all data types at the time of writing (int, float, list, text)
```
db.create_table(keyspace, tablename, schema, order_by=...order the results by some clustering key...)
```
### load the data from a json file
#### if the json file contains each instance on a line then set line_by_line = True
#### if the json file contains an array of json data, or a sinle json object then set line_by_line=False
#### as_dataframe will extract the data and construct a dataframe (should be set to True along with proprecss).
#### if preprocess is set to True, then TLS, HTTPS, and DNS attributes will be dropped. List types will be transformed in a way such that each element will become an independent dimension (Useful for preprocessing test data before storing it in the database).
#### if as_dataframe is set to True then preprocess must be set to True as well.
```
  data = load_json_file(path_to_file, line_by_line=True, as_dataframe=False, preprocess=False)
```

### insert the data into an existing partition
```
  db.insert_batch_data(...)
```
# Update !!!!
## We provided two simple commands for creating Cassandra parition and storing training data for any of the data sets on the fly

# Example for using the commands

## Please make sure you have a running cassandra service

## navigate to CassandraDb and run the following two commands
```
python main.py --create-table {table-name} --dataset {name of dataset}
```

## The previous command will create a partition representing the data set inside a running Cassandra instance. The schema will be inferred automatically from the dataset

## to insert raw data inside the previously created partition run the following command

```
python main.py --insert-data {name of dataset to be inserted} --table-name {table-name}
```
