@echo off
echo =====================================
echo 🔄 Vérification et installation de FFMPEG
echo =====================================

where ffmpeg >nul 2>nul
IF ERRORLEVEL 1 (
    echo ❌ ffmpeg non trouvé, installation en cours...
    winget install -e --id Gyan.FFmpeg
    echo ✅ Installation de ffmpeg terminée.
) ELSE (
    echo ✅ ffmpeg est déjà installé.
)

echo =====================================
echo 🔄 Vérification de l'environnement virtuel
echo =====================================

IF NOT EXIST "poc_env\" (
    echo ❌ Environnement virtuel non trouvé, création en cours...
    python -m venv poc_env
    echo ✅ Environnement virtuel créé.
) ELSE (
    echo ✅ Environnement virtuel déjà présent.
)

echo =====================================
echo 🔄 Activation de l'environnement virtuel et mise à jour de pip
echo =====================================

call poc_env\Scripts\activate

echo 🔄 Mise à jour de pip...
python -m pip install --upgrade pip

echo =====================================
echo 🔄 Installation des dépendances Python
echo =====================================

pip install -r requirements.txt

echo ✅ Configuration terminée, prêt à exécuter le programme !
pause
