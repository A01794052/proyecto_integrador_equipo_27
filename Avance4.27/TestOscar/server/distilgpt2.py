from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

model_name = 'EleutherAI/gpt-neo-2.7B'
generator = pipeline("text-generation", model=model_name, device=0)  # Use device=0 for GPU

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    max_length = data.get('max_length', 100)  # Default max_length

    # Generate text
    output = generator(prompt, max_new_tokens=max_length)
    print(output)
    
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # You can specify your desired port
