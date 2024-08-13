from flask import Flask, jsonify, request
import os
app = Flask(__name__)
from dotenv import load_dotenv
load_dotenv()

@app.route('/')
def home():
    return jsonify({"message": "API is up and running!"})

@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {"name": "John Doe", "age": 30}
    return jsonify(sample_data)

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.json
    return jsonify({"received": data}), 201

@app.route('/api/env', methods=['GET'])
def get_env_var():
    var_name = request.args.get('var', '')
    env_var_value = os.getenv(var_name, 'Variable not found')
    return jsonify({var_name: env_var_value})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))