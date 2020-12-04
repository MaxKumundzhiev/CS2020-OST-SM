# Deployment
```bash
spin up the cluster
$ docker-compose up

within another terminal, to know when kafka cluster finished initialising
$ docker-compose logs -f broker | grep started
```