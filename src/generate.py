from aitextgen import aitextgen

ai = aitextgen(
    tf_gpt2="774M",
    cache_dir="converted",
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