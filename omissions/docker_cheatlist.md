```
Check docker version 
$ docker -v

List Docker Containers
$ docker ps 
$ docker ps -a # all dockers

Create docker Image 
$ docker build -t <image-name> .
    e.g. docker build -t python-imdb . 

Run Docker Container
$ docker run <image-name> 
    e.g. docker run python-imdb 

Run Docker Container with interactive (-i) and sudo (-t) mode 
$ docker run -t -i <image-name> 
    e.g. docker run -t -i python-imdb

Run Docker Container with forwarding ports
$ docker run -p 8000:8000 <image-name> 
where: 
    "-p" flag - manages forwarding of ports    

Connect to the running Docker Container (either use Docker Dashboards OR check Docker Container ID)
$ docker exec -it <docker container ID> bash
OR
$ docker exec -it <docker container ID> /bin/sh

To create/change a root password in a running container
$ docker exec -itu root <container ID> passwd

```