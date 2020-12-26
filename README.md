Simple script querying Google search daily with a list of keywords

Data is loaded into a database to be displayed in Grafana
# Twitter collector

Simple service running in a Docker container, collecting tweets through Twitter's streaming API and writing these tweets as newline-delimited JSON files in a Docker volume  
Depends on twython

# Parameters
keyword : the keyword to poll the Twitter Streaming API

# docker memo
docker run --privileged --rm docker/binfmt:a7996909642ee92942dcd6cff44b9b95f08dad6
docker buildx build --platform linux/arm/v7 -t seo_monitor/google_k_rpi .
docker save seo_monitor/google_k_rpi | gzip > google_rpi.tar.gz

gunzip google_rpi.tar.gz
docker load -i google_rpi.tar
docker volume create google-mdr   
docker run -d \
  --name google_keywords \
  --mount source=google-mdr,target=/app \
  seo_monitor/google_k_rpi:latest

