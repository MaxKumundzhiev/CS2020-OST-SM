# Google Cloud Engine API
Here you can find the configurations and functionalities for OST-SM Google Cloud Engine.

## Structure
./endpoints - store `openapi.yml` configuration file within instance endpoints.

## Routines


## Deployment
````bash
check gcp project-wise deployed services
$ gcloud services list

deploy endpoints
$ gcloud endpoints services deploy openapi.yaml 
```    