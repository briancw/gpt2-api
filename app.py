import gpt_2_simple as gpt2

model_name='124M'

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, model_name=model_name)

# Generate Params
# run_name='run1',
# checkpoint_dir='checkpoint',
# model_name='124M',
# sample_dir='samples',
# return_as_list=True,
# truncate='',
# destination_path='',
# sample_delim='=' * 20 + '\n',
# prefix='',
# seed=None,
# nsamples=1,
# batch_size=1,
# length=20,
# temperature=0.5,
# top_k=10
# top_p=0.0,
# include_prefix=True,
output_text = gpt2.generate(
    sess,
    model_name=model_name,
    length=10,
    nsamples=1,
    return_as_list=True,
    prefix='Hello world! '
)

i = 0
while i < len(output_text):
    print("Sample " + str(i))
    print('========')
    print(output_text[i])
    print('========\n')
    i += 1
