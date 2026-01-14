@echo off
echo [ETAPE 1] Verification de la qualite (Tests)...
call .venv\Scripts\activate
python -m pytest tests/

if %errorlevel% neq 0 (
    echo [ERREUR] Les tests ont echoue. Le programme ne se lancera pas.
    pause
    exit /b
)

echo [ETAPE 2] Lancement du programme...

python main.py
pause
