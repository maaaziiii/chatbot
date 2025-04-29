from flask import Flask, render_template, request, jsonify
from chat import get_response  # Import get_response from your working chat.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('front.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data['message']
    response = get_response(message)
    return jsonify({'answer': response})

if __name__ == "__main__":
    app.run(debug=True)
