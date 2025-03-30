from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur AIMEDIXAL v3"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    if not data or "symptome" not in data:
        return jsonify({"error": "Données invalides. Format attendu: {'symptome': '...'"}), 400
    
    # Simulation d'une analyse avancée
    result = {
        "message": "Analyse avancée terminée",
        "input": data,
        "diagnostic": "Probable maladie de Parkinson" if "tremblements" in data["symptome"].lower() else "Pas de signe de Parkinson",
        "version": "v3"
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

