# Mongo Database
  

# Deployment
```bash
$ docker run -d --name mongodb --network="kafka-network" -p 27888:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=secret mongo
```

# Mongo Compass
As the additional UI for mongo database `Mongo Compass` can be utilized.
For that navigate to [official MongoDB documentation](https://www.mongodb.com/try/download/compass) and download appropriate type and version.
Afterwards once `initializing connection with database` fill requested `URI` with `mongodb://admin:secret@localhost:27888/?authSource=admin`

   