from aitextgen import aitextgen

# Use to convert GPT2 models in /models to PyTorch
ai = aitextgen(
    tf_gpt2="124M",
    cache_dir="models",
    to_gpu=True,
)