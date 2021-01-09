# Mongo Database
  
## Deployment
```bash
$ docker run -d --name mongodb --network="kafka-network" -p 27888:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=secret mongo
```

## Upload particular dataset to MongoDB
```bash
$ python -m services.mongodb.uploader -d CICIDS -t train
$ python -m services.mongodb.uploader -d CICIDS -t test

$ python -m services.mongodb.uploader -d TRANSFORMED_CICIDS -t train
$ python -m services.mongodb.uploader -d TRANSFORMED_CICIDS -t test

$ python -m services.mongodb.uploader -d NET -t train
$ python -m services.mongodb.uploader -d NET -t test

$ python -m services.mongodb.uploader -d TRANSFORMED_NET -t train
$ python -m services.mongodb.uploader -d TRANSFORMED_NET -t test
```  

## MongoDB Interface
MongoDB python interface is stored under `services.mongodb.utils.py`
- To insert row into `ost` database:
```bash
from services.mongodb.utils import MongoFactory

_id = 100
type = 'sample'
collection_name = 'some_document'
row = {"sample_document": "sample_value"}
 
MongoFactory().insert_row(_id, row, type, collection_name, verbose=False)
```   
Described row will be written to `ost` DB at `some_document` table with protected `_id=100` and context `{"sample_document": "sample_value"}`.  


## Mongo Compass
As the additional UI for mongo database `Mongo Compass` can be utilized.
For that navigate to [official MongoDB documentation](https://www.mongodb.com/try/download/compass) and download appropriate type and version.
Afterwards once `initializing connection with database` fill requested `URI` with `mongodb://admin:secret@localhost:27888/?authSource=admin?retryWrites=True`

 
## Good to know
*URI* - Uniform Resource Identifier - utilized to connect applications and db instances
E.G.:
`mongodb://admin:secret@localhost:27888/?authSource=admin?retryWrites=True`

*Mongo Atlas* - cloud based functionality allows to create/manipulate mongo database in cloud 
   