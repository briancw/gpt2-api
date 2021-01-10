#!/bin/bash
docker run \
-it \
--rm \
-v $PWD/models:/aitext/models \
-v $PWD/input:/aitext/input \
-v $PWD/src:/aitext/src \
-v $PWD/converted:/aitext/converted \
aitextgen \
bash