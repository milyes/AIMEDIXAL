Structure complète du projet (tree)



MedRiskAI/
│── backend/                      # 📌 Backend Flask (API & modèle IA)
│   │── models/                    # Dossier des modèles IA
│   │   │── parkinson_model.pkl     # Modèle IA pré-entrainé
│   │   │── train_model.py          # Script d'entraînement du modèle IA
│   │── app.py                      # API Flask principale
│   │── requirements.txt            # Dépendances Python (Flask, scikit-learn, pandas, etc.)
│   │── config.py                   # Fichier de configuration (DB, API keys, etc.)
│── frontend/                       # 📌 Interface utilisateur (Web UI)
│   │── static/                     # Fichiers statiques (CSS, JS, images)
│   │   │── styles.css              # Feuille de style
│   │   │── script.js               # Gestion API et interactions UI
│   │── templates/                  # Pages HTML pour l'interface web
│   │   │── index.html              # Page principale avec le formulaire utilisateur
│   │── app_frontend.py             # Serveur Flask pour l'interface web
│── database/                       # 📌 Base de données
│   │── medrisk.db                  # Fichier SQLite (ou autre DB)
│   │── models.py                   # Schéma de la base de données (SQLAlchemy)
│── scripts/                        # 📌 Scripts auxiliaires
│   │── calcul_fichier.sh            # Script Bash pour les calculs électriques/médicaux
│   │── data_preprocessing.py        # Nettoyage et préparation des données
│   │── feature_extraction.py        # Extraction des caractéristiques des données
│── tests/                          # 📌 Tests unitaires
│   │── test_api.py                 # Tests pour l’API Flask
│   │── test_model.py               # Tests pour le modèle IA
│── docs/                           # 📌 Documentation du projet
│   │── README.md                   # Description générale du projet
│   │── api_documentation.md        # Documentation détaillée de l’API
│── deployment/                     # 📌 Déploiement et configuration
│   │── Dockerfile                  # Configuration pour le déploiement avec Docker
│   │── docker-compose.yml           # Orchestration Docker (backend, frontend, DB)
│   │── nginx.conf                   # Configuration Nginx pour le serveur web
│── .gitignore                       # 📌 Fichiers à ignorer dans Git
│── requirements.txt                 # 📌 Dépendances globales du projet
│── run.sh                           # 📌 Script pour exécuter facilement l’application
