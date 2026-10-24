respuesta = client.models.generate_content(
    model=MODEL,
    contents="Salúdame en una frase como si fueras una guía de turismo de Huancayo.",
)
print(respuesta.text)
