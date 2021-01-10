from aitextgen import aitextgen
from pathlib import Path

from flask import Flask, abort, jsonify, request
from flask_cors import CORS, cross_origin

# Initialize text generation
ai = aitextgen(
    tf_gpt2="774M",
    cache_dir="converted",
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

    # if 'text' not in data or len(data['text']) == 0 or 'model' not in data:
    if 'text' not in data or 'min_length' not in data or 'max_length' not in data:
        abort(400)
    else:
        text = data['text']
        min_length = data['min_length']
        max_length = data['max_length']

        # Debug input values
        print(text, prompt, min_length)

        # Generate Text
        result = ai.generate_one(
            to_gpu=True,
            prompt=text,
            min_length=min_length,
            max_length=max_length,
        )

        return jsonify({result: result})

# Simple route for helping test app is running
@app.route('/')
def hello_world():
   return 'Hello World'

# Run App
app.run(host='0.0.0.0', port=3000)