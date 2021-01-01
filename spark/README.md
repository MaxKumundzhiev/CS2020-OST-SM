# Spark 


## Deployment
Deploy represenative spark environment on executable machine

```
$ docker run -p 8888:8888 --name spark jupyter/pyspark-notebook -v <path-to-project>/CS2020-OST-SM/datase:/usr/src/app/dataset

```
For example:

```
$ docker run -p 8888:8888 --name spark jupyter/pyspark-notebook -v /home/zozo/Documents/Study/3rd/OST/CS2020-OST-SM/dataset:/usr/src/app/dataset

```

Stop container:

```
$ docker stop <container name>

```

Once you done wit