@echo off
cd /d "%~dp0"
py -3 iniciar_servidor.py
if errorlevel 1 (
  echo No se pudo iniciar. Verifica que Python 3 este instalado.
  pause
)
