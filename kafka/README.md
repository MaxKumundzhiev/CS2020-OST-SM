# Kafka
Streaming Fraud Detection System based on Kafka and Python interface.

# Description
We will generate a stream of transactions and process those to detect which ones are potential fraud.
- Docker images taken from Confluent Platform — Confluent being a major actor in the Apache Kafka community — and was inspired by their Kafka single node example.


# Notions
```
Apache Kafka is a piece of software which, as all pieces of software, runs on actual computers.
First, a bit of terminology. Kafka being a distributed system, it runs in a cluster, i.e. multiple computers (a.k.a. nodes) that communicate with one another. In Kafka jargon, nodes are called brokers.
```

```
What does Kafka need in order to run? Actually, it only needs two things — a Kafka broker and a Zookeeper instance.
Zookeeper - it is a coordination software, distributed as well, used by Apache Kafka to keep track of the cluster state and members. It is an essential component of any Kafka cluster,
 ```

# Deployment
```bash
spin up the cluster
$ docker-compose up

within another terminal, to know when kafka cluster finished initialising
$ docker-compose logs -f broker | grep started
```