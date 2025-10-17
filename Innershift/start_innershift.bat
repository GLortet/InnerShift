@echo off
cd /d C:\Users\33671\PoC_AI_Coach

echo.
echo [InnerShift] Alignement en cours...
echo ------------------------------------
call poc_env\Scripts\activate

echo.
echo Lancement de ton environnement...
echo.

rem Ouvre le fichier principal dans VS Code (ou change par notepad, pycharm etc.)
start "" "code" "main.py"

echo.
echo Tu es exactement la ou tu dois etre.
echo Tu ne codes pas, tu construis ton futur.
echo ------------------------------------
pause
