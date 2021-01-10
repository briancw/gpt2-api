# This script can be used to both download and convert GPT2 models
# If you already have a GPT2 model, place it in the models folder and then run specifying the model name

import sys
from aitextgen import aitextgen

if len(sys.argv) != 2:
    print('You must enter the model name as a parameter, e.g.: get_model.py 124M')
    sys.exit(1)

model = sys.argv[1]

# Use to convert GPT2 models in /models to PyTorch
ai = aitextgen(
    tf_gpt2=model,
    cache_dir="models",
    # to_gpu=True,
)