import gpt_2_simple as gpt2
import os

# Change me to download other models
# Options are 124M 345M 774M and 1558M
model_name = "124M"

if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/