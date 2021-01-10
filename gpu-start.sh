#!/bin/bash
docker run \
-it \
--rm \
--gpus all \
-v $PWD/models:/aitext/models \
-v $PWD/input:/aitext/input \
-v $PWD/src:/aitext/src \
-v $PWD/converted:/aitext/converted \
aitextgen \
bash