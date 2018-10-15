#!/bin/sh
set -x

sudo su -
yum install -y docker git

service docker start

docker pull horiacloud/rv-docker

docker run -p 80:80 -it --rm --name rv horiacloud/rv-docker
