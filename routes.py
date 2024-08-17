from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()

@app.route('/')
def home():
    try:
        return jsonify({"message": "API is up and running!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        sample_data = {"name": "John Doe", "age": 30}
        return jsonify(sample_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/data', methods=['POST'])
def post_data():
    try:
        data = request.get_json()
        if not data:
            raise ValueError("No JSON data provided.")
        return jsonify({"received": data}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/env', methods=['GET'])
def get_env_var():
    try:
        var_name = request.args.get('var', '')
        if not var_name:
            raise ValueError("Variable name 'var' not specified in request parameters.")
        env_var_value = os.getenv(var_name, 'Variable not found')
        return jsonify({var_name: env_var_value})
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/submit_resume', methods=['POST'])
def submit_resume():
    try:
        data = request.get_json()
        if not data:
            raise ValueError("No resume data provided.")

        # Format and save the resume data
        resume_filename = "resume_mockup.txt"
        with open(resume_filename, "w") as file:
            file.write("Resume\n\n")
            file.write(f"Name: {data.get('name', 'N/A')}\n")
            file.write(f"Email: {data.get('email', 'N/A')}\n\n")
            file.write("Education:\n")
            for edu in data.get("education", []):
                file.write(f"- {edu}\n")
            file.write("\nWork Experience:\n")
            for job in data.get("work_experience", []):
                file.write(f"- {job}\n")
            file.write("\nSkills:\n")
            for skill in data.get("skills", []):
                file.write(f"- {skill}\n")

        return jsonify({"message": "Resume successfully submitted and saved.", "file": resume_filename}), 201
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))