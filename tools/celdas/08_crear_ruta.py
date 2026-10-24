def crear_ruta(dias, presupuesto, intereses, grupo, intentos=3):
    """Pide una ruta al modelo, la valida y reintenta pasando los errores."""
    pedido = (
        f"Días: {dias}\n"
        f"Presupuesto máximo por persona: S/ {presupuesto}\n"
        f"Intereses: {', '.join(intereses) or 'cualquiera'}\n"
        f"Viaja: {grupo}"
    )
    ruta, problemas = None, []
    for intento in range(1, intentos + 1):
        contenido = pedido
        if problemas:
            contenido += "\n\nCorrige estos problemas de tu respuesta anterior:\n- " + "\n- ".join(problemas)
        respuesta = client.models.generate_content(
            model=MODEL,
            contents=contenido,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                response_mime_type="application/json",
                response_schema=Ruta,
                temperature=0.4,
            ),
        )
        try:
            ruta = Ruta.model_validate_json(respuesta.text)
        except ValidationError:
            problemas = ["La respuesta no cumple el esquema JSON."]
            continue
        problemas = validar_ruta(ruta, dias, presupuesto)
        if not problemas:
            print(f"✅ Ruta válida en el intento {intento}")
            return ruta, []
        print(f"⚠️ Intento {intento}: {len(problemas)} problema(s), reintentando...")
    return ruta, problemas
