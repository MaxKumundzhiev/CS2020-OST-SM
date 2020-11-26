# CS2020-OST-SM :construction: 
CS2020-OST-SM application


## Application Description
### Application Propose
The application propose is the provision of 3 classification pre-trained on real-world data models which enables to predict 3 different types of targets.

### Application Structure
The application assumed to be deployed onto the dedicated GCP instance, jointly the application will provide finite number of endpoints to trigger dedicated parts of the application by api.      

**The application is splitted on dedicated independent microservices** 
<div id="divActivites" name="divActivites" style="border:thin">
    <textarea id="inActivities" name="inActivities" style="border:1px solid black;">
    Each and every microservice is independently deployable.
    Communicates between microservices operates based on interface of each microservice.
    </textarea> 
</div> 

<ul>
  <li>mongodb microservice and corresponding interface to interact with it.</li>
  <li>cassandradb microservice and corresponding interface to interact with it.</li>
  <li>ml-kit microservice</li>
  <li>spark microservice</li>
  <li>flink microservice</li>
</ul>


## Service Diagram 
![Service Diagram](service_diagram/OST-SM.jpg "OST-SM Diagram") 


## Data Description
The project data source is [NetML Challenge 2020](https://github.com/ACANETS/NetML-Competition2020)
- Data is represented as the collection of  `1,199,139 flows` in spreaded across `3 different datasets` (including detailed flow features and labels.)
    - NetML
      NetML dataset is constructed by selecting several PCAP files from www.stratosphereips.org website.
    - CICIDS2017
      CICIDS2017 dataset is generated using https://www.unb.ca/cic/datasets/ids-2017.html
    - non-vpn2016
       non-vpn2016 dataset is the subset of ISCX-VPN-nonVPN2016 dataset from https://www.unb.ca/cic/datasets/vpn.html
       Detailed description can be found at: [NetML: A Challenge for Network Traffic Analytics](https://arxiv.org/abs/2004.13006)

## Requirements
The assumed environment provider: **conda**
To set up conda on your machine follow steps on [official documentation](https://docs.conda.io/en/latest/miniconda.html)

**Create dedicated conda environment and set up dependencies**    
```bash
$ conda create -n OST python=3.8 -y && conda activate OST
$ pip install -r reqirements.txt 
```     

## Deployment
 :information_source: under process

#### MongoDB deployment
```bash
$ 
```

#### CassandraDB deployment
```bash
$ 
```

#### ML-KIT deployment
```bash
$ 
```

#### Spark deployment
```bash
$ 
```

#### Flink deployment
```bash
$ 
```
