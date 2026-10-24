import gradio as gr

INTERESES = ["cultura", "naturaleza", "gastronomía", "artesanía", "aventura", "familia"]


def planificar(dias, presupuesto, intereses, grupo):
    ruta, problemas = crear_ruta(int(dias), int(presupuesto), intereses, grupo)
    return ruta_a_html(ruta, problemas)


# TODO: arma la interfaz con gr.Blocks. Necesitas:
#   - entradas: gr.Slider (días 1-3), gr.Number (presupuesto), gr.CheckboxGroup(INTERESES), gr.Radio (grupo)
#   - un gr.Button y una salida gr.HTML()
#   - conectar con: boton.click(planificar, [entradas...], salida)
#   - lanzarla con: demo.launch(share=True)   → te da el link público
