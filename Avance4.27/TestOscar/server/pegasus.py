from flask import Flask, request, jsonify
from transformers import pipeline
from transformers import PegasusTokenizer, PegasusForConditionalGeneration
import torch

app = Flask(__name__)

model_name = "google/pegasus-large"
model = PegasusForConditionalGeneration.from_pretrained(model_name).to("cuda")
tokenizer = PegasusTokenizer.from_pretrained(model_name)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    max_length = data.get('max_length', 100)  # Default max_length

    # Tokenize input
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True).to("cuda")
    
    # Generate summary
    summary_ids = model.generate(inputs["input_ids"], max_length=60, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    print(summary)

    # Return the response
    return jsonify({"generated_text": summary})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # You can specify your desired port
