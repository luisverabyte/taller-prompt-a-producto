ruta, problemas = crear_ruta(
    dias=2,
    presupuesto=150,
    intereses=["artesanía", "cultura"],
    grupo="pareja",
)
if ruta:
    print(ruta.model_dump_json(indent=2))
print("Problemas:", problemas or "ninguno ✅")
