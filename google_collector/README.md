# Google collector

Simple script running in a croned Docker container, collecting google search results for a list of keywords
Depends on google pypi module (to evaluate) and pandas

# Parameters
keywords file

# About deploying pandas in Docker on Raspberry Pi 3
docker build on raspeberry pi fails (compiler gets killed)
Building the container with 
    docker buildx build --platform linux/arm/v7
takes forever
Trying to explicitly list all dependancies in requirements.txt did not work

Trying to push swap to 2 GB on rpi : WORKS ! 256 or 512 MB should be enough for swap size.
Takes more than two hours though, emulation and cross compilation to be worked on

# docker memo for emulation build (currently unused)
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
