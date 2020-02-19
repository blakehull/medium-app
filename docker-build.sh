#!/bin/sh

docker build -t mltag:latest .
docker run -it -d -P mltag:latest
docker ps --format "{{.Ports}}"
url=$(docker ps --format "{{.Ports}}{{.Image}}" | grep mltag | cut -d- -f1 | tr -d '[:space:]')
container=$(docker ps --format "{{.ID}}->{{.Image}}" | grep mltag | cut -d- -f1 | tr -d '[:space:]')
echo "RUNNING ON: " ${url}
echo "Starting Up..."
sleep 20
curl -w "\n" -X GET "http://${url}/similar_tags/machine%20learning"

