from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur AIMEDIXAL v2"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    if not data:
        return jsonify({"error": "Aucune donnée reçue"}), 400
    return jsonify({"message": "Analyse terminée", "input": data, "version": "v2"})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

