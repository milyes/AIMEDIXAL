#!/bin/bash

VERSION=$1

if [[ -z "$VERSION" ]]; then
    echo "Usage: ./run.sh <version>"
    exit 1
fi

if [[ ! -f "app_v${VERSION}.py" ]]; then
    echo "Version app_v${VERSION}.py introuvable."
    exit 1
fi

echo "Lancement d'AIMEDIXAL version ${VERSION}..."
python3 app_v${VERSION}.py


