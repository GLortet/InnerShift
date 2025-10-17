@echo off
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
setx OPENAI_API_KEY "RENTRE_TA_CLE_ICI"
python main.py --audio sample.wav --user "Gilles"
