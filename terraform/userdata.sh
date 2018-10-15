#!/bin/sh
set -x

sudo su -
yum install -y docker git

service docker start

docker pull horiacloud/rv-docker

docker run -it --rm --name rv horiacloud/rv-docker
