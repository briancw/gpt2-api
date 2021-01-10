FROM nvidia/cuda:11.1-base-ubuntu20.04

ENV LANG=C.UTF-8
RUN mkdir /aitext
WORKDIR /aitext
ADD ./requirements.txt /aitext/requirements.txt
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y nano
RUN pip3 install -r requirements.txt
RUN rm requirements.txt