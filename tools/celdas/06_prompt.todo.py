# TODO: escribe el system prompt. Un buen prompt tiene:
#   - Rol: quién es el asistente
#   - Reglas claras y numeradas (usar SOLO el catálogo, respetar presupuesto y días)
#   - Qué hacer cuando no puede cumplir (decirlo en "advertencia", no inventar)
#   - El catálogo: json.dumps(LUGARES, ensure_ascii=False)
SYSTEM_PROMPT = f"""Eres una guía de turismo del Valle del Mantaro.
TODO: agrega tus reglas aquí.

Catálogo:
{json.dumps(LUGARES, ensure_ascii=False)}
"""
print(SYSTEM_PROMPT[:600], "...")
