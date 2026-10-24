class Respuesta(BaseModel):
    titulo: str
    pasos: list[str]
    por_que: str
    advertencia: Optional[str] = None


# 👇 Cambia estas 3 variables
ROL = "Eres un asesor agrícola que ayuda a pequeños productores del Valle del Mantaro."
DATOS = "Cultivos de la zona: papa, maca, maíz, alcachofa. Heladas fuertes entre junio y agosto."
PREGUNTA = "Quiero sembrar papa en julio, ¿qué debo tener en cuenta?"


def consultar(rol, datos, pregunta):
    respuesta = client.models.generate_content(
        model=MODEL,
        contents=pregunta,
        config=types.GenerateContentConfig(
            system_instruction=f"{rol}\nUsa solo estos datos y no inventes otros:\n{datos}",
            response_mime_type="application/json",
            response_schema=Respuesta,
            temperature=0.4,
        ),
    )
    return Respuesta.model_validate_json(respuesta.text)


r = consultar(ROL, DATOS, PREGUNTA)
print(r.titulo)
for i, paso in enumerate(r.pasos, 1):
    print(f"{i}. {paso}")
print("Por qué:", r.por_que)
