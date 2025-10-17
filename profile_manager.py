from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, Any

DATA = Path("data")
DATA.mkdir(parents=True, exist_ok=True)
PROFILE_PATH = DATA / "user_profiles.json"

if not PROFILE_PATH.exists():
    PROFILE_PATH.write_text("{}", encoding="utf-8")

def load_profiles() -> Dict[str, Any]:
    return json.loads(PROFILE_PATH.read_text(encoding="utf-8"))

def save_profiles(db: Dict[str, Any]) -> None:
    PROFILE_PATH.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")

def update_profile(user: str, analysis: Dict[str, Any]) -> Dict[str, Any]:
    db = load_profiles()
    profile = db.get(user, {"history": []})
    profile["last_pcm"] = analysis.get("pcm_guess")
    profile["last_sentiment"] = analysis.get("sentiment")
    profile["last_keywords"] = analysis.get("keywords", [])
    profile["last_intelligences"] = analysis.get("intelligences", {})
    profile["history"].append(analysis)
    db[user] = profile
    save_profiles(db)
    return profile
