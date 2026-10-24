# Esta celda YA trae el import y la función planificar: no los borres.
# Completa solo desde el TODO de abajo.
import gradio as gr

INTERESES = ["cultura", "naturaleza", "gastronomía", "artesanía", "aventura", "familia"]


def planificar(dias, presupuesto, intereses, grupo):
    try:
        ruta, problemas = crear_ruta(int(dias), int(presupuesto), intereses, grupo)
    except Exception as e:
        return ruta_a_html(None, [f"La API no respondió ({type(e).__name__}). Espera un minuto y vuelve a intentar."])
    return ruta_a_html(ruta, problemas)


# TODO: arma la interfaz con gr.Blocks. Necesitas:
#   - entradas: gr.Slider (días 1-3), gr.Number (presupuesto), gr.CheckboxGroup(INTERESES), gr.Radio (grupo)
#   - un gr.Button y una salida gr.HTML()
#   - conectar con: boton.click(planificar, [entradas...], salida)
#   - lanzarla con: demo.launch(share=True, show_error=True)   → te da el link público


if "demo" not in globals():
    print("👆 Falta completar el TODO: arma la interfaz con gr.Blocks (guardada en `demo`) y lánzala.")
