FROM ubuntu:14.04

# Add application sources
ADD . /opt/birdhouse

# cd into application
WORKDIR /opt/birdhouse

# Install system dependencies
RUN bash bootstrap.sh -i && bash requirements.sh

# Run install
RUN make clean install 

# Volume for data, cache, logfiles, ...
VOLUME /data

# Ports used in birdhouse
EXPOSE 8090 8094

# Update config and start supervisor ...
CMD ["make", "start"]

