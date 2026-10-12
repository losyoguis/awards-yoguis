#!/bin/bash
cd "$(dirname "$0")"
if ! command -v python3 >/dev/null 2>&1; then
  echo "Se necesita Python 3 para iniciar la presentación."
  read -r -p "Presiona Enter para cerrar..."
  exit 1
fi
python3 iniciar_servidor.py
