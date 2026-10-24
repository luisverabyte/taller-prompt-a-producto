import gradio as gr

INTERESES = ["cultura", "naturaleza", "gastronomía", "artesanía", "aventura", "familia"]


def planificar(dias, presupuesto, intereses, grupo):
    try:
        ruta, problemas = crear_ruta(int(dias), int(presupuesto), intereses, grupo)
    except Exception as e:
        return ruta_a_html(None, [f"La API no respondió ({type(e).__name__}). Espera un minuto y vuelve a intentar."])
    return ruta_a_html(ruta, problemas)


with gr.Blocks(title="Rutas del Valle del Mantaro") as demo:
    gr.Markdown("# 🏔️ Rutas del Valle del Mantaro\nDime cuántos días tienes y armo tu ruta.")
    with gr.Row():
        with gr.Column():
            dias = gr.Slider(1, 3, value=2, step=1, label="Días")
            presupuesto = gr.Number(value=150, label="Presupuesto por persona (S/)")
            intereses = gr.CheckboxGroup(INTERESES, value=["cultura"], label="Intereses")
            grupo = gr.Radio(["solo", "pareja", "familia", "amigos"], value="pareja", label="¿Con quién viajas?")
            boton = gr.Button("Armar mi ruta", variant="primary")
        salida = gr.HTML()
    boton.click(planificar, [dias, presupuesto, intereses, grupo], salida)

demo.launch(share=True, show_error=True)   # ← te da un link público https://....gradio.live
