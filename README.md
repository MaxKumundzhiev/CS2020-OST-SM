# CS2020-OST-SM Application 

**Each team member has dedicated git branch to work on with corresponding name.**
<ul><b>Participants</b>:
<li><s>Ahmad Abdelrahim -- user-1</s>></li>
<li>Bashar Khdr -- user-2</li>
<li>Georgie Kalaygie -- user-3</li>
<li>Tasnime Ayed -- user-4</li>
<li>Ekaterina Zolotareva -- user-5</li>
<li>Maksim Kumundzhiev -- user-6</li>
</ul>


## Kick off
```bash
$ mkdir ost-sm && cd ost-sm
$ git clone https://github.com/KumundzhievMaxim/CS2020-OST-SM.git && cd CS2020-OST-SM
$ git checkout user-{your_number}
```

## Hints 
1. do not forget frequently fetch updates from master branch if there are such.   
2. do more commits approaching your task. 
  use following format to commit changes:
  `$ git commit -m 'user-{your_number}, {what"s done}'`

4. do more PRs approaching your task.
  - write explicit description of PR;
  - assign yourself for pushing PR;
  - add reviewers (your team members) for PR;
  - DO NOT merge PR until at least one of team members will not review it;  

5. keep code clean and readable for other team members. 

## Deployment
###  0. Setup environment
```bash
** create conda environment
$ conda create -n {your_desired_environment_name} python=3.8 -y && conda activate {your_desired_environment_name}
$ pip install -r reqirements.txt

** create particular network for dockers
$ docker network create kafka-network 
```

###  1. Retrieve Source Datasets (dataset)
```bash
$ python -m dataset.handler -d dataset/CICIDS2017 -a fine 
$ python -m dataset.handler -d dataset/CICIDS2017 -a top
 
$ python -m dataset.handler -d dataset/NetML -a fine
$ python -m dataset.handler -d dataset/NetML -a top

$ python -m dataset.handler -d dataset/non-vpn2016 -a fine
$ python -m dataset.handler -d dataset/non-vpn2016 -a mid
$ python -m dataset.handler -d dataset/non-vpn2016 -a top  
```

### 2. MongoBD (mongodb) [WIP]
#### 2.a. Deploy MongoBD
```bash
** Deploy mongodb container
$ cd mongodb (navigate to mongodb microservice)   
$ docker run -d --name mongodb --network="kafka-network" -p 27888:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=secret mongo
```
#### 2.b. Upload data to MongoDB
```bash
$ python -m mongodb.handler --action upload --dataset all
```

### 3. CassandraDB (cassandradb) [WIP]
#### 3.a. Deploy CassandraDB
```bash
** Deploy cassandra container
$ cd cassandradb (navigate to cassandra microservice)   
$ ... 
```

#### 3.b. Upload data to CassandraDB
```bash
$ python -m cassandra.handler --action upload --dataset all (WIP)  
```

### 4. Feature Engineering (spark) [WIP]
```bash
$ cd spark (navigate to spark microservice) 
$ docker-compose up (spin up spark docker container follow jupyter notebook instructions)
```

### 5. Off-line models training (ml-kit) [WIP]
```bash
$ cd ml_kit (navigate to ml_kit microservice) 
$ python -m ml_kit.train --model <type of model> --dataset <dataset> --annotation <level of annotation>
    e.g.: $ python -m ml_kit.train --model svm --dataset cicids --annotation fine    
```

### 6. Streaming Prediction (kafka) [WIP]
```bash
$ cd kafka
```
Before launching the kafka microservice, navigate to `./kafka/docker.env` and setup desired parameters:
```
Example:
    DATASET=CICIDS2017
    LEVEL=top
    MODEL=svm
    DATABASE=mongodb

Explanation:
    DATASET=<NAME OF DATASET TO PROCESS> # TEST SET NOT TRAIN
    LEVEL=<LEVEL OF DATASET TO PROCESS> # FINE, MID, TOP -- EACH DATASET HAS IT"S OWN PARTICULAR TYPES 
    MODEL=<TYPE OF PREDICTING MODEL> # [SVM, DECISION TREE, RANDOM FOREST] 
    DATABASE=<DATABASE TO WRITE RESULTS> # [MONGODB, CASSANDRADB]
``` 

#### Deployment 
```bash
# mandatory [Terminal 1]
spin up the kafka && zookeeper clusters 
$ docker-compose -f docker-compose.kafka.yml up

# mandatory [Terminal 2]
spin up the generator && detector   
$ docker-compose --env-file docker.env up

# addition [Terminal 3]
to know when kafka cluster finished initialising 
$ docker-compose -f docker-compose.kafka.yml logs broker # specific case

# addition [Terminal 3]
to observe filtered by detector legit transactions (--topic streaming.transactions.legit)   
$ docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.legit

# addition [Terminal 3]
to observe filtered by detector fraud transactions (--topic streaming.transactions.fraud)
$ docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.fraud
```


     