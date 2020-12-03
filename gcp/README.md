# How GCP is setup? 
1. It was launched bare Linux Ubuntu VM
2. Installed **conda** and added to HOME path **conda**
```bash
# Setup Ubuntu
sudo apt update --yes
sudo apt upgrade --yes

# Get Miniconda and make it the main Python interpreter
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
bash ~/miniconda.sh -b -p ~/miniconda 
rm ~/miniconda.sh

export PATH=~/miniconda/bin:$PATH
```    

3. Installed Docker
```bash
sudo apt install docker.io

# The Docker service needs to be setup to run at startup. To do so, type in each command followed by enter:
sudo systemctl start docker
sudo systemctl enable docker

```

# How GCP endpoints are set up
[Official Google Documentation](https://cloud.google.com/endpoints/docs/openapi/get-started-compute-engine-docker)
[Deploy GCP Endpoints](https://cloud.google.com/endpoints/docs/openapi/get-started-compute-engine-docker#code)

## 1. Deploying the API && Endpoints configuration 
- under `./api/endpoints` created `openapi.yml`
    - changed default configurations on:
  ```
  swagger: "2.0"
  
  info:
      description: "OST-SM Cloud Engine Endpoints API."
  title: "OST-SM"
  version: "1.0.0"
  host: "echo-api.endpoints.dazzling-task-267622.cloud.goog"
  ```
  
- deployed/attached api configurations to the ost-sm project
```bash
$ cd ./api/endpoints && gcloud endpoints services deploy openapi.yaml 
```

- Enabled Endpoints service:
```bash
$ gcloud services enable ENDPOINTS_SERVICE_NAME
e.g.: gcloud services enable echo-api.endpoints.dazzling-task-267622.cloud.goog
```   

## 2. Deploying the API backend 
So far you have deployed the OpenAPI document to Service Management, but you haven't yet deployed the code that serves the API backend. This section walks you through getting Docker set up on your VM instance and running the API backend code and the ESP in a Docker container.
**IMPORTANT** We skipped granting access for external services because GCP was initiated by default with all accesses.

- connect to remote gcp machine
- create your own container network called esp_net
```$ sudo docker network create --driver bridge esp_net ```
- run the sample Echo server that serves the sample API:
```$ sudo docker run --detach --name=echo --net=esp_net gcr.io/google-samples/echo-python:1.0 ```  

```$ sudo docker run --name=esp --detach --publish=80:8080 --net=esp_net gcr.io/endpoints-release/endpoints-runtime:1 --service=OST-SM  --rollout_strategy=managed  --backend=echo:8080```


- add generated api key to ENV variables   
```$ export ENDPOINTS_KEY=AIzaSyAppXepx_5QkqBTY6Vd1Xdo0WtKfa1qbkM ```
