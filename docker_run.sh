#!/usr/bin/env bash
#sudo docker build -t pelican .
#docker tag pelican tobymccann/pelican
docker pull tobymccann/pelican:latest
docker run -t --name=pelican-run -v $(pwd):/site tobymccann/pelican
docker rm pelican-run