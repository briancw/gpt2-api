from aitextgen import aitextgen
from pathlib import Path

ai = aitextgen(
    tf_gpt2="124M",
    cache_dir="models",
    to_gpu=True,
)

input_text = Path('./input/input.txt').read_text()
print('Warmed up')

result = ai.generate_one(
    to_gpu=True,
    prompt=input_text,
    min_length=200,
    max_length=400,
)

print(result)

#ai.generate(
#    n=1,
#    to_gpu=True,
#    prompt="I believe in unicorns because",
#    max_length=100,
#)