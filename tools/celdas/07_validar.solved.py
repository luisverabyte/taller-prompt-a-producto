def validar_ruta(ruta: Ruta, dias: int, presupuesto: int) -> list[str]:
    """Devuelve la lista de problemas. Lista vacía = la ruta es válida."""
    problemas = []
    if len(ruta.dias) != dias:
        problemas.append(f"Se pidieron {dias} días y la ruta tiene {len(ruta.dias)}.")
    for d in ruta.dias:
        for p in d.paradas:
            if p.nombre not in NOMBRES:
                problemas.append(f"El lugar {p.nombre!r} no está en el catálogo.")
        horas = sum(p.horas for p in d.paradas)
        if horas > 8:
            problemas.append(f"El día {d.dia} suma {horas} horas (máximo 8).")
    total = sum(p.costo_soles for d in ruta.dias for p in d.paradas)
    if total > presupuesto:
        problemas.append(f"El costo es S/ {total} y el presupuesto es S/ {presupuesto}.")
    return problemas
