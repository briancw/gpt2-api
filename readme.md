# Text Generation API built on [aitextgen](https://github.com/minimaxir/aitextgen)

### How to run
Build a Docker container with ```./build.sh```<br>
Startup with ```start.sh``` or ```gpu-start.sh```<br>
To run with GPU acceleration, you must have nvidia drivers installed on the host machine and nvidia-docker2<br>
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker<br>
If you do not have these on the host, everything will still run in CPU.<br>

### Download GPT2 models
The script src/get_model.py can be used to both download GPT2 models from Google Server and convert them to the correct format for this project.<br>
Run ```python3 src/get_model.py 124M``` to download and convert the 124M model. Other options are "345M" "774M" and "1558M". This script can also download other HuggingFace models.<br>

### Generate Text Manually
Place some input text into input/input.txt<br>
Edit src/generate.py to select a model, enable/disable GPU acceleration, and text generation properties.<br>
Run ```python3 src/generate.py```<br>

### Run API
Edit src/app.py to select model, enable/disable GPU acceleration, or other text gen properties.<br>
Run ```python3 src/app.py``` to startup the http API on port 3000<br>

### Request text from API
There is an example script in client-example/ for how to access the API with NodeJS.<br>

### Alternative method for converting GPT2 models
https://docs.aitextgen.io/gpt-2-simple/
transformers-cli convert --model_type gpt2 --tf_checkpoint checkpoint/run1 --pytorch_dump_output pytorch --config checkpoint/run1/hparams.json<br>
(I could not get this to work personally)<br>

### Docs for aitextgen
https://docs.aitextgen.io/
