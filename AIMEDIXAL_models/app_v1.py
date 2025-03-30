from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur AIMEDIXAL v1"

@app.route('/analyze', methods=['GET'])
def analyze():
    return jsonify({"message": "Analyse en cours...", "version": "v1"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

