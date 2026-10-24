"""Cliente simulado con la misma forma que el SDK de Gemini (plan B sin internet).

Devuelve respuestas precargadas de data/mock_responses.json, asi el codigo del
taller es identico con o sin conexion.
"""
import json
import re


class _Respuesta:
    def __init__(self, text):
        self.text = text


class _Models:
    def __init__(self, mocks):
        self._mocks = mocks

    def generate_content(self, *, model, contents, config=None):
        schema = getattr(config, "response_schema", None)
        nombre = getattr(schema, "__name__", None)
        texto = contents if isinstance(contents, str) else json.dumps(contents)
        if nombre == "Ruta":
            m = re.search(r"Días:\s*(\d)", texto)
            dias = min(max(int(m.group(1)) if m else 2, 1), 3)
            return _Respuesta(json.dumps(self._mocks[f"ruta_{dias}d"], ensure_ascii=False))
        if nombre is not None:
            return _Respuesta(json.dumps(self._mocks["reto"], ensure_ascii=False))
        return _Respuesta(self._mocks["saludo"])


class MockClient:
    def __init__(self, ruta_json="data/mock_responses.json"):
        with open(ruta_json, encoding="utf-8") as f:
            self.models = _Models(json.load(f))
