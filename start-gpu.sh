#!/bin/bash
docker run \
-it \
--rm \
--gpus all \
-v $PWD/models:/gpt-2-simple/models \
-v $PWD/input:/gpt-2-simple/input \
-v $PWD/app.py:/gpt-2-simple/app.py \
gpt-2-simple-gpu \
bash
