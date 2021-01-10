# Kafka
Kafka utilizes streaming classification-wise system.

## Description
It will be generated a stream of records for particular dataset and process those to predict corresponding class approaching corresponding pretrained models.


## Before Deployment
Before launching proposed commands, navigate to `docker.env` and setup desired parameters:
```
!!! ALL PARAMETRES ARE POSITIONAL (I.E. REQUIRED)
For example:
    DATASET=SELECTED_CICIDS
    MODEL=logistic-regressor
    MODELS_CHECKPOINT=/usr/src/app/services/models/ 
    TASK_TYPE=binary_class
    DATABASE=mongodb
    DB_NAME='ost'
    DB_URL='mongodb://admin:secret@localhost:27888/?authSource=admin'
    DATABASE=mongodb

Explanation:
    DATASET=<NAME OF DATASET TO PROCESS> 
    MODEL=<MODEL TO USE> 
    MODELS_CHECKPOINT=/usr/src/app/services/models/ # SHOULD BE KEPT SAME
    TASK_TYPE=<TYPE OF TARGET LABEL>
    DATABASE=<DATABASE TO WRITE RESULTS> # [WIP] PAUSE
    DB_NAME=<DATABASE NAME> # [WIP] PAUSED
    DB_URL=<DATABASE URI> # [WIP] PAUSED
    DATABASE=<DATABASE ENGINE> # [WIP] PAUSED
``` 
### docker.env options
```bash
List of available datasets names:
- SELECTED_CICIDS
- SELECTED_NET
```

```bash
List of available models names:
- logistic-regressor
- decision-tree
- random-forest
```

```bash
List of available models names:
- logistic-regressor
- decision-tree
- random-forest
```

```bash
List of available tasks names:
- binary_class
- multi_class
```
 
## Deployment
```bash
# mandatory [Terminal 1]
spin up the kafka && zookeeper clusters 
$ docker-compose -f docker-compose.kafka.yml up

# mandatory [Terminal 2]
spin up the generator && detector   
$ docker-compose --env-file docker.env up

# addition [Terminal 3] # specific case
to know when kafka cluster finished initialising 
$ docker-compose -f docker-compose.kafka.yml logs broker 
```

Sample `detector` output:
```json
    detector_1   | GET ROW {'rev_pld_var': 0.0, 'src_port': 64103, 'pld_distinct': 1, 'bytes_out': 64, 'hdr_mean': 8.0, 'time_length': 9.5367431640625e-07, 'num_pkts_out': 2, 'http_method': nan, 'pld_mean': 32.0, 'rev_pld_distinct': 1, 'num_pkts_in': 2, 'hdr_distinct': 1, 'rev_hdr_distinct': 1, 'hdr_bin_40': 0, 'pr': 17, 'pld_max': 32, 'rev_pld_max': 79, 'http_code': nan, 'pld_bin_inf': 0, 'rev_pld_mean': 79.0, 'pld_median': 32, 'dst_port': 53, 'id': 5444624, 'rev_pld_bin_128': 2, 'rev_hdr_bin_40': 0, 'bytes_in': 158, 'http_content_len': nan, 'dns_answer_cnt': nan, 'dns_query_cnt': 1.0, 'tls_svr_key_exchange_len': nan, 'tls_svr_cnt': nan, 'tls_cnt': nan, 'tls_key_exchange_len': nan, 'tls_svr_ext_cnt': nan, 'tls_svr_cs_cnt': nan, 'tls_cs_cnt': nan, 'tls_ext_cnt': nan}
    detector_1   | PREDICTION: [3.]
```

# Notions
```
- Apache Kafka is a piece of software which, as all pieces of software, runs on actual computers.
First, a bit of terminology. Kafka being a distributed system, it runs in a cluster, i.e. multiple computers (a.k.a. nodes) that communicate with one another. In Kafka jargon, nodes are called brokers.

- What does Kafka need in order to run? Actually, it only needs two things — a Kafka broker and a Zookeeper instance.
Zookeeper - it is a coordination software, distributed as well, used by Apache Kafka to keep track of the cluster state and members. It is an essential component of any Kafka cluster,
 ```