#!/bin/sh
set -x

sudo su -
yum install -y docker git

service docker start

docker container run -p 80:8080 -d rv/rv-docker
