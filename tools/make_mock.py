"""Genera data/mock_responses.json con totales coherentes con data/lugares.json."""
import json
import pathlib

raiz = pathlib.Path(__file__).resolve().parent.parent
lugares = {l["id"]: l for l in json.loads((raiz / "data/lugares.json").read_text("utf-8"))["lugares"]}


def parada(id_, tip):
    l = lugares[id_]
    return {"nombre": l["nombre"], "distrito": l["distrito"], "horas": l["horas"],
            "costo_soles": l["costo_soles"], "tip": tip}


def ruta(resumen, dias, advertencia=None):
    dias_json = [{"dia": i + 1, "titulo": t, "paradas": [parada(*p) for p in ps]}
                 for i, (t, ps) in enumerate(dias)]
    total = sum(p["costo_soles"] for d in dias_json for p in d["paradas"])
    return {"resumen": resumen, "dias": dias_json, "costo_total_soles": total, "advertencia": advertencia}


mocks = {
    "saludo": "¡Hola desde Huancayo! Soy Gemini (respuesta precargada: estás en modo sin conexión).",
    "ruta_1d": ruta("Un día para conocer el centro de Huancayo y probar un clásico de la zona.", [
        ("Centro y sabores", [
            ("plaza-constitucion", "Ve temprano, hay menos gente."),
            ("cerrito-libertad", "Lleva una casaca, el viento sube con la tarde."),
            ("pachamanca", "Pide la porción para compartir."),
        ])]),
    "ruta_2d": ruta("Dos días: ciudad y miradores el primero, artesanía el segundo.", [
        ("Ciudad y miradores", [
            ("plaza-constitucion", "Empieza aquí para ubicarte."),
            ("torre-torre", "Lleva zapatillas con buen agarre."),
            ("parque-identidad", "Ideal para la última luz de la tarde."),
        ]),
        ("Manos artesanas", [
            ("hualhuas", "Pregunta por los talleres abiertos al público."),
            ("san-jeronimo-tunan", "Compara precios antes de comprar."),
        ])]),
    "ruta_3d": ruta("Tres días con ciudad, artesanía y un paseo a la laguna.", [
        ("Ciudad", [
            ("plaza-constitucion", "Buen punto de partida."),
            ("cerrito-libertad", "Sube con calma, hay altura."),
        ]),
        ("Artesanía", [
            ("hualhuas", "Lleva efectivo para comprar tejidos."),
            ("cochas-mates", "Pide ver el proceso de tallado."),
        ]),
        ("Laguna y sabores", [
            ("laguna-paca", "Llega antes del mediodía."),
        ])]),
    "reto": {
        "titulo": "Plan sugerido",
        "pasos": ["Define quién es tu usuario.", "Elige el caso de uso más pequeño.", "Mide si funciona con 5 personas reales."],
        "por_que": "Respuesta precargada del modo sin conexión.",
        "advertencia": None,
    },
}
(raiz / "data/mock_responses.json").write_text(json.dumps(mocks, ensure_ascii=False, indent=2), "utf-8")
print("ok", {k: v.get("costo_total_soles") for k, v in mocks.items() if isinstance(v, dict) and "costo_total_soles" in v})
