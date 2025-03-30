#!/bin/bash

# Chemin vers le fichier de sauvegarde (l'original)
BACKUP_PATH="/data/data/com.termux/files/home/AIMEDIXAL_backup/app.py"

# Chemin vers le fichier actuel à remplacer
TARGET_PATH="/data/data/com.termux/files/home/AIMEDIXAL/app.py"

# Remplacer l'ancien app.py par le nouveau
cp $BACKUP_PATH $TARGET_PATH

# Redémarrer l'application
python3 $TARGET_PATH

