from aitextgen import aitextgen
from pathlib import Path

from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin

# Initialize text generation
ai = aitextgen(
    tf_gpt2="774M",
    cache_dir="models",
    to_gpu=True,
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
        seed = None # Int < 2^32
        do_sample = True
        pad_token_id = None # string

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

        # Debug input values
        print(prompt, min_length, max_length)

        # Generate Text
        result = ai.generate_one(
            prompt = prompt,
            min_length = min_length,
            max_length = max_length,
            temperature = temperature,
            do_sample = do_sample,
            seed = seed,
            pad_token_id = pad_token_id,
        )

        return result

# Simple route for helping test app is running
@app.route('/')
def hello_world():
   return 'Hello World'

# Run App
app.run(host='0.0.0.0', port=3000)