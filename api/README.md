# Google Cloud Engine API
**GCP-wise Service Name: `echo-api.endpoints.dazzling-task-267622.cloud.goog`**
 
Here you can find the configurations and functionalities for OST-SM Google Cloud Engine.


## Structure
.api/endpoints - store `openapi.yml` configuration file within instance endpoints.

## Routines
TBD

## Deployment
````bash
check gcp project-wise deployed services
$ gcloud services list

[WIP] deploy endpoints
$ gcloud endpoints services deploy openapi.yaml

[WIP] enable endpoints
$ gcloud services enable <service name>
$ gcloud services enable echo-api.endpoints.dazzling-task-267622.cloud.goog 
```
    