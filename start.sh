#!/bin/bash
docker run \
-it \
--rm \
-v $PWD/models:/gpt-2-simple/models \
-v $PWD/input:/gpt-2-simple/input \
-v $PWD/src:/gpt-2-simple/src \
gpt-2-simple \
bash
