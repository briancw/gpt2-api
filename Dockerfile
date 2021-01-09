FROM tensorflow/tensorflow:1.15.2-py3

ENV LANG=C.UTF-8
RUN mkdir /gpt-2-simple
WORKDIR /gpt-2-simple
ADD ./requirements.txt /gpt-2-simple/requirements.txt
RUN pip3 install -r requirements.txt
RUN rm requirements.txt
