# ⚙️ Preparación: ejecútala una vez y sigue
!pip install -q google-genai gradio   # si sale un aviso rojo de "dependency conflicts", ignóralo

import os, json, subprocess

REPO = "https://github.com/luisverabyte/taller-prompt-a-producto"
if not os.path.exists("data/lugares.json"):
    subprocess.run(["git", "clone", "--depth", "1", REPO, "taller"], check=True)
    os.chdir("taller")

USE_MOCK = False   # True = sin internet / sin API key (respuestas precargadas)
MODEL = "gemini-3.5-flash-lite"   # el modelo más pequeño, barato y rápido

try:
    from google.colab import userdata
    API_KEY = userdata.get("GEMINI_API_KEY")
except Exception:
    API_KEY = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types

if USE_MOCK:
    from mock_client import MockClient
    client = MockClient()
    print("🔌 Modo SIN CONEXIÓN: usando respuestas precargadas")
elif not API_KEY:
    raise RuntimeError(
        "No encontré tu API key. Revisa que el secreto se llame GEMINI_API_KEY y que "
        "tenga activado el acceso desde el notebook. Si no tienes key o internet, "
        "pon USE_MOCK = True."
    )
else:
    client = genai.Client(
        api_key=API_KEY,
        # si la API se satura (429, 503), reintenta sola unos segundos
        http_options=types.HttpOptions(retry_options=types.HttpRetryOptions(
            attempts=5, initial_delay=2, max_delay=20, http_status_codes=[429, 500, 503, 504])),
    )
    print("✅ Listo, conectado con", MODEL)
