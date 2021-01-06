## Spark
The Spark microservice is supposed to apply particular feature selection algorithms accordingly incoming dataset.

## Requirements
It is required to have preinstalled docker CLI and docker-compose CLI 

## Launch Spark Docker Container
```bash
$ docker-compose up
```

## Get to Know Spark
Spark utilizes few interfaces. Jointly our microservice it is used `pyspark`.  
* Pyspark subpackages
  * pyspark.ml
  * pyspark.sql
  * pyspark.mllib
  * pyspark.resource
  * pyspark.streaming 

We are going to approach few of listed subpackages:   
* pyspark.sql <- interact with data
* pyspark.ml <- feature selection algorithms 

## Feature Selection Algorithms
3 source datasets -- 3 different feature selection algorithms 
1.
2. 
3.    
