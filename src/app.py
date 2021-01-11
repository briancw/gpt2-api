from aitextgen import aitextgen
from pathlib import Path
import sys
import torch
from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin

# Check if GPU is available
gpu_available = torch.cuda.is_available()

# Load specific model from command line
model = "124M"
if len(sys.argv) == 2:
    model = sys.argv[1]

# Initialize text generation
ai = aitextgen(
    tf_gpt2="774M",
    cache_dir="models",
    to_gpu=gpu_available,
)

# Initialize App
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/generate", methods=['POST'])
@cross_origin()
def get_gen():
    data = request.get_json()

    if 'prompt' not in data:
        abort(400)
    else:
        prompt = data['prompt']
        min_length = 10
        max_length = 10
        temperature = 0.7
        seed = None
        do_sample = True
        pad_token_id = None
        repetition_penalty = 1.0
        length_penalty = 1.0

        if 'min_length' in data:
            min_length = data['min_length']
        if 'max_length' in data:
            max_length = data['max_length']
        if 'temperature' in data:
            temperature = data['temperature']
        if 'seed' in data:
            seed = data['seed']
        if 'do_sample' in data:
            do_sample = data['do_sample']
        if 'pad_token_id' in data:
            pad_token_id = data['pad_token_id']
        if 'repetition_penalty' in data:
            repetition_penalty = data['repetition_penalty']
        if 'length_penalty' in data:
            length_penalty = data['length_penalty']

        # Debug input values
        print(prompt, min_length, max_length)

        # Generate Text
        result = ai.generate_one(
            prompt = prompt,
            min_length = min_length,
            max_length = max_length,
            temperature = temperature,
            do_sample = do_sample,
            seed = seed, # Int < 2^32
            pad_token_id = pad_token_id, # Int
            
            # I can't find these in the source code and don't know how they get applied
            # num_beams = 1,
            repetition_penalty = repetition_penalty,
            length_penalty = length_penalty,
            # no_repeat_ngram_size = 1, # Int
        )

        return result

# Simple route for helping test app is running
@app.route('/')
def hello_world():
   return 'Hello World'

# Run App
app.run(host='0.0.0.0', port=3000)