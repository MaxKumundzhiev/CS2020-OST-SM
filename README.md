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

###  1. Extract Datasets
```bash
$ python -m extractor.handler -d CICIDS 
$ python -m extractor.handler -d NET 
```

###  2. Transform Datasets
```bash
$ python -m transformer.handler -d CICIDS 
$ python -m transformer.handler -d NET 
```

### 3. MongoBD
#### 2.a. Deploy MongoBD
```bash
** Deploy mongodb container   
$ docker run -d --name mongodb --network="kafka-network" -p 27888:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=secret mongo
```
#### 2.b. Upload data to MongoDB
```bash
$ python -m services.mongodb.uploader -d CICIDS -t train
$ python -m services.mongodb.uploader -d CICIDS -t test

$ python -m services.mongodb.uploader -d TRANSFORMED_CICIDS -t train
$ python -m services.mongodb.uploader -d TRANSFORMED_CICIDS -t test

$ python -m services.mongodb.uploader -d SELECTED_CICIDS -t train
$ python -m services.mongodb.uploader -d SELECTED_CICIDS -t test

$ python -m services.mongodb.uploader -d NET -t train
$ python -m services.mongodb.uploader -d NET -t test

$ python -m services.mongodb.uploader -d TRANSFORMED_NET -t train
$ python -m services.mongodb.uploader -d TRANSFORMED_NET -t test

$ python -m services.mongodb.uploader -d SELECTED_NET -t train
$ python -m services.mongodb.uploader -d SELECTED_NET -t test
```

### 3. CassandraDB 
Navigate to `services/cassandradb` and follow described in `README` steps

### 4. Spark
```bash
$ cd spark (navigate to spark microservice) 
$ docker-compose up (spin up spark docker container follow jupyter notebook instructions)
```

### 5. Off-line training
Train certain model within particular dataset:
```bash
$ python -m services.ml_kit.train -d <DATASET NAME> -t <TYPE OF TASK> -m <MODEL NAME>

For example:
$ python -m services.ml_kit.train -d SELECTED_CICIDS -t binary_class -m logistic-regressor 
```

Train all models within all datasets: 
```bash
# CICIDS Binary Classification
$ python -m services.ml_kit.train -d SELECTED_CICIDS -t binary_class -m logistic-regressor
$ python -m services.ml_kit.train -d SELECTED_CICIDS -t binary_class -m decision-tree
$ python -m services.ml_kit.train -d SELECTED_CICIDS -t binary_class -m random-forest

# CICIDS Multiclass Classification
$ python -m services.ml_kit.train -d SELECTED_CICIDS -t multi_class -m logistic-regressor
$ python -m services.ml_kit.train -d SELECTED_CICIDS -t multi_class -m decision-tree 
$ python -m services.ml_kit.train -d SELECTED_CICIDS -t multi_class -m random-forest

# NET Binary Classification
$ python -m services.ml_kit.train -d SELECTED_NET -t binary_class -m logistic-regressor
$ python -m services.ml_kit.train -d SELECTED_NET -t binary_class -m decision-tree
$ python -m services.ml_kit.train -d SELECTED_NET -t binary_class -m random-forest

# NET Multiclass Classification
$ python -m services.ml_kit.train -d SELECTED_NET -t multi_class -m logistic-regressor
$ python -m services.ml_kit.train -d SELECTED_NET -t multi_class -m decision-tree 
$ python -m services.ml_kit.train -d SELECTED_NET -t multi_class -m random-forest
``` 

### 6. Kafka
The execution should be done from `services/kafka` folder. 

#### Before Deployment
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
#### docker.env options
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
 
#### Deployment
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
