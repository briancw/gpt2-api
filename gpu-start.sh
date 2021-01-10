#!/bin/bash
docker run \
-it \
--rm \
--gpus all \
-v $PWD/models:/aitext/models \
-v $PWD/input:/aitext/input \
-v $PWD/src:/aitext/src \
-p 3000:3000 \
aitextgen \
bash