from flask import Flask, request, jsonify
from transformers import pipeline
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

app = Flask(__name__)

model_name = 'google/flan-t5-large'
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Move the model to the GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model = model.to(device)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    print(prompt)
    max_length = data.get('max_length', 100)  # Default max_length

    # Tokenize and generate output
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(inputs.input_ids, max_length=256)
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(response_text)

    # Return the response
    return jsonify({"generated_text": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # You can specify your desired port
