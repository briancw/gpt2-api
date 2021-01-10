# How to
Build with ```./build.sh```<br>
Startup with ```start.sh``` or ```gpu-start.sh```<br>

### Generate Manually
Run ```python3 src/generate.py``` for manual generation using input/input.txt as primer text

### Run API
Run ```python3 src/app.py``` to startup API on port 3000

# Convert GPT2 model
https://docs.aitextgen.io/gpt-2-simple/
transformers-cli convert --model_type gpt2 --tf_checkpoint checkpoint/run1 --pytorch_dump_output pytorch --config checkpoint/run1/hparams.json

# Docs
https://docs.aitextgen.io/