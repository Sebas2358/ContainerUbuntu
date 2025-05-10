# Use Ubuntu 20.04 as base
FROM ubuntu:20.04

# Install some packages
RUN apt-get update && apt-get install -y curl vim
RUN apt update && apt install -y lsb-release


CMD ["/bin/bash"]