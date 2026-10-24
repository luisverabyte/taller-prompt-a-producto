# Guía paso a paso del ponente: De prompt a producto

Esta guía es tu guion para dictar el taller. En cada paso encuentras:

- 🎤 **Di en voz alta**: qué estamos haciendo y por qué.
- 🖱️ **Haz**: qué clic o acción hacer en pantalla.
- 📋 **Copia y pega**: el código exacto y en qué celda va.

**Regla única para todos los bloques de código:** en Colab haz clic dentro de la celda, selecciona todo (`Ctrl+A`), borra y pega el bloque. Luego ejecuta con ▶️ (o `Shift+Enter`). No hay que combinar nada a mano.

## Enlaces (tenlos en pestañas antes de empezar)

| Para qué | Enlace |
|---|---|
| Repositorio (QR de las slides) | https://github.com/luisverabyte/taller-prompt-a-producto |
| Notebook de inicio (lo que abre el público) | https://colab.research.google.com/github/luisverabyte/taller-prompt-a-producto/blob/cp0-inicio/taller.ipynb |
| Notebook resuelto, para tu demo | https://colab.research.google.com/github/luisverabyte/taller-prompt-a-producto/blob/main/taller.ipynb |
| Rescate: CP1 ya resuelto (para quien se atrase) | https://colab.research.google.com/github/luisverabyte/taller-prompt-a-producto/blob/cp1-primera-llamada/taller.ipynb |
| Rescate: CP1 y CP2 resueltos | https://colab.research.google.com/github/luisverabyte/taller-prompt-a-producto/blob/cp2-logica-producto/taller.ipynb |
| Rescate: todo resuelto | https://colab.research.google.com/github/luisverabyte/taller-prompt-a-producto/blob/cp3-interfaz/taller.ipynb |
| Crear la API key | https://aistudio.google.com/apikey |
| Slides (6) | https://claude.ai/artifact/EzxFRTU9of6zAR5kDQyf7H |
| Temporizador | https://claude.ai/artifact/L1DZjfz6VDavxRXdjQmaMh |

## Antes de empezar (tu checklist, 10 min antes)

- [ ] Temporizador abierto en pantalla completa (`F`), listo para iniciar con `espacio`.
- [ ] Tu notebook **resuelto** (`main`) abierto en una pestaña, con la demo ya ejecutada y el link `gradio.live` abierto en otra pestaña.
- [ ] El notebook de **inicio** (`cp0-inicio`) abierto en otra pestaña, **sin ejecutar nada**: es el que escribirás en vivo.
- [ ] Tu API key creada y guardada como secreto `GEMINI_API_KEY` en Colab.
- [ ] Zoom de fuente del navegador al 150% (`Ctrl` y `+`).
- [ ] Hotspot del celular listo por si cae el wifi.

---

## 0:00 – 0:04 · Bienvenida

🎤 **Di:**
> "Hoy no vamos a ver una demo: vamos a construir un prototipo de IA y cada pareja se lo lleva funcionando. Sin instalar nada, solo navegador. Levanten la mano: ¿quién ya usó una API de IA? Júntense en parejas: uno que ya sabe con uno que empieza."

🖱️ **Haz:**
1. Inicia el temporizador (`espacio`).
2. Muestra la slide 1 con el QR del repositorio.
3. Pide que escaneen el QR y abran el repositorio, y que creen su API key en https://aistudio.google.com/apikey si aún no la tienen.

---

## 0:04 – 0:10 · Demo y arquitectura

🎤 **Di:**
> "Esto es lo que vamos a construir: un asistente que arma rutas turísticas del Valle del Mantaro. Le digo cuántos días tengo, mi presupuesto y qué me interesa, y me devuelve una ruta. Pero lo importante no es el resultado, es el flujo."

🖱️ **Haz:**
1. Abre tu pestaña con el link `gradio.live` y arma una ruta: 2 días, S/ 150, artesanía y cultura, en pareja.
2. Ve a la **slide 2** (el diagrama) y recórrela de izquierda a derecha.

🎤 **Di sobre el diagrama:**
> "Un chat responde texto libre. Un producto necesita cuatro cosas: un prompt con reglas, una llamada a la API, una respuesta con forma fija, que podamos validar, y una interfaz para que alguien que no programa lo use. Esas cuatro piezas las construimos hoy, en tres checkpoints."

3. Ve a la **slide 3** y explica los stickers: 🟢 verde cuando les sale, 🔴 rojo cuando necesitan ayuda de un mentor.

---

## 0:10 – 0:20 · Checkpoint 1: primera llamada a la API

### Paso 1.1 · Abrir el notebook de inicio
🖱️ Abre el enlace de **cp0-inicio** (tabla de arriba). Pide al público que haga lo mismo.

🎤 **Di:**
> "Esto es Google Colab: un cuaderno de código en la nube. Cada bloque es una celda y se ejecuta con el botón de play. No instalamos nada en nuestras laptops."

### Paso 1.2 · Guardar la API key como secreto
🖱️ **Haz:** en el panel izquierdo abre el icono 🔑 **Secretos** → **Agregar secreto** → nombre `GEMINI_API_KEY` → pega tu key → activa **Acceso desde el notebook**.

🎤 **Di:**
> "La API key es como la contraseña de nuestra cuenta. Nunca la pegamos dentro del código ni la compartimos: va en Secretos. Si no activan Acceso desde el notebook, el código no la podrá leer, y ese es el error más común."

### Paso 1.3 · Ejecutar la celda de preparación
🖱️ **Haz:** ejecuta la primera celda de código (la que empieza con `# ⚙️ Preparación`). Tarda cerca de un minuto. No modifiques nada.

🎤 **Di mientras carga:**
> "Esta celda instala dos librerías, lee la API key del secreto y crea el cliente. El cliente es nuestro teléfono para llamar al modelo. Fíjense en el MODEL: usamos Gemini 3.5 Flash-Lite, el más pequeño, barato y rápido, suficiente para este prototipo."

⚠️ **Si sale un aviso rojo de "dependency conflicts":** 🎤 "Ignórenlo, es un aviso de pip, no un error nuestro. Lo importante es que al final diga ✅ Listo."

### Paso 1.4 · Tu primera llamada
🎤 **Di:**
> "Un request tiene tres partes: el modelo al que llamo, el contenido que le envío, y la respuesta que recibo. Eso es todo lo que es una API de IA."

🖱️ **Haz:** en la celda del Checkpoint 1 (empieza con `# TODO: llama al modelo`), borra todo y pega:

📋 **Copia y pega:**

```python
respuesta = client.models.generate_content(
    model=MODEL,
    contents="Salúdame en una frase como si fueras una guía de turismo de Huancayo.",
)
print(respuesta.text)
```

🎤 **Di tras ejecutar:**
> "Ese texto no lo escribí yo: lo generó el modelo. Cambien el contenido por lo que quieran y vuelvan a ejecutar. Cuando les salga una respuesta, levanten la mano o pongan el sticker verde."

**Mentores atienden stickers rojos.** Errores típicos: secreto mal nombrado o sin acceso al notebook.

> ⏱️ Si a los 18 minutos hay muchos rojos, di: "Los que se atrasaron, abran la rama cp1-primera-llamada: ya viene resuelto el Checkpoint 1."

---

## 0:20 – 0:32 · Checkpoint 2: del prompt a la lógica del producto

🎤 **Di:**
> "Una llamada suelta es un experimento. Para que sea un producto necesito tres cosas: una forma fija para la respuesta, reglas claras para el modelo y una forma de comprobar que cumplió. Vamos a construir las tres."

### Paso 2.1 · El esquema (la forma de la respuesta)
🖱️ **Haz:** ejecuta la celda que empieza con `from typing import Optional` sin cambiar nada. Debe imprimir `12 lugares en el catálogo`.

🎤 **Di:**
> "Estas clases dicen cómo debe verse la respuesta: una Ruta tiene días, cada día tiene paradas y cada parada tiene nombre, horas, costo y un tip. Es un contrato: si el modelo responde otra cosa, el código se entera. Y fíjense en el catálogo: son 12 lugares reales cargados de un archivo. El modelo solo podrá recomendar esos."

### Paso 2.2 · El system prompt
🎤 **Di:**
> "El system prompt es el manual de instrucciones del asistente. Tiene un rol, reglas numeradas, qué hacer cuando no puede cumplir, y el catálogo. La regla clave es la 1: usa solo el catálogo. Así evitamos que invente lugares."

🖱️ **Haz:** en la celda del system prompt (empieza con `# TODO: escribe el system prompt`), borra todo y pega:

📋 **Copia y pega:**

```python
SYSTEM_PROMPT = f"""Eres una guía de turismo local del Valle del Mantaro (Huancayo, Perú).
Armas rutas para visitantes usando SOLO los lugares del catálogo.

Reglas:
1. Usa únicamente lugares del catálogo y copia su nombre exacto.
2. Cada día suma máximo 8 horas de visitas.
3. La suma de costo_soles de todas las paradas debe ser menor o igual al presupuesto.
4. Prioriza los intereses del visitante, pero mezcla al menos dos categorías.
5. Si los días o el presupuesto no alcanzan, dilo en "advertencia" en vez de inventar.
6. Cada parada lleva un tip corto y práctico.

Catálogo:
{json.dumps(LUGARES, ensure_ascii=False)}
"""
print(SYSTEM_PROMPT[:600], "...")
```

### Paso 2.3 · Las validaciones
🎤 **Di:**
> "Nunca confíen ciegamente en lo que responde el modelo. Esta función revisa tres cosas: que los días coincidan, que cada lugar esté en el catálogo y que el costo no pase del presupuesto. Si algo falla, devuelve una lista de problemas."

🖱️ **Haz:** en la celda `validar_ruta` (empieza con `def validar_ruta`), borra todo y pega:

📋 **Copia y pega:**

```python
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
```

### Paso 2.4 · Ver la lógica completa funcionar
🖱️ **Haz:** ejecuta las dos celdas siguientes sin cambiar nada: `def crear_ruta` y la que empieza con `ruta, problemas = crear_ruta(`.

🎤 **Di sobre `crear_ruta`:**
> "Aquí está la lógica del producto. Pedimos la ruta, la validamos y, si hay problemas, se los devolvemos al modelo diciéndole 'corrige esto' y reintentamos, hasta tres veces. Es un ciclo de autocorrección."

🎤 **Di sobre el resultado** (debe salir `✅ Ruta válida en el intento 1`):
> "Miren el JSON: siempre trae las mismas llaves, así que cualquier interfaz puede leerlo. Eso es una respuesta estructurada."

💬 **Dato para decir en vivo (importante):**
> "La validación revisa lo que le pedimos revisar: lugares, costo y días. No revisa que los tips sean verdad. En mis pruebas el modelo agregó detalles que no estaban en el catálogo, como una visita guiada o un teñido natural. Validar es decidir qué vas a revisar. Y mejorar eso es el siguiente nivel."

> Nota: el modelo pequeño a veces omite las tildes. Si pasa, dilo con naturalidad: "los modelos pequeños son más baratos y rápidos, pero cometen estos errores".

### Paso 2.5 · Micro-reto (4 min): llévalo a tu problema
🎤 **Di:**
> "Ahora, a su problema real. Cambien solo tres variables: el ROL, los DATOS y la PREGUNTA, y piensen en tres cosas de producto."

🎤 **Tips de Product Management** (30 segundos, slide 4):
> "Primero, el usuario: ¿para quién es? Segundo, el caso de uso mínimo: ¿qué es lo único que debe hacer bien? Tercero, la métrica: ¿cómo sé que funciona? Por ejemplo, el porcentaje de rutas válidas a la primera."

🖱️ **Haz:** en la celda del micro-reto (empieza con `class Respuesta`), cambia **solo estas tres líneas**. Ejemplos listos para pegar:

**Educación**
```python
ROL = "Eres un asesor pedagógico que ayuda a docentes de primaria de Huancayo."
DATOS = "Cursos: comunicación, matemática, ciencia. Aulas de 30 alumnos con un solo proyector."
PREGUNTA = "Quiero enseñar fracciones en 45 minutos con materiales que ya tengo en el aula."
```

**Comercio**
```python
ROL = "Eres un asesor para pequeños comerciantes del Mercado Mayorista de Huancayo."
DATOS = "Se vende papa, maíz y quesos. Los domingos hay feria. Los clientes piden delivery por WhatsApp."
PREGUNTA = "¿Cómo organizo los pedidos por WhatsApp para no perder ventas los domingos?"
```

**Turismo**
```python
ROL = "Eres un guía local que ayuda a viajeros que llegan a Huancayo por pocas horas."
DATOS = "Plaza Constitución, Cerrito de la Libertad, Parque de la Identidad Huanca y Feria Dominical."
PREGUNTA = "Tengo 4 horas libres un domingo, ¿qué visito primero?"
```

---

## 0:32 – 0:40 · Checkpoint 3: interfaz y compartir

🎤 **Di:**
> "Una API no es un producto hasta que alguien que no programa puede usarla. Con Gradio le ponemos cara a la función en pocas líneas, y nos regala un link público para abrirlo desde el celular."

### Paso 3.1 · La presentación de la ruta
🖱️ **Haz:** ejecuta la celda que empieza con `import html` sin cambiar nada.

🎤 **Di:**
> "Esta celda solo convierte el JSON en tarjetas visuales. Es presentación, no lógica, así que no la vamos a escribir."

### Paso 3.2 · La interfaz
🎤 **Di:**
> "Gradio funciona así: declaro las entradas, un botón y una salida, y conecto el botón con la función planificar. Las entradas son los datos que le pasamos a la función crear_ruta, y la salida es lo que devuelve."

🖱️ **Haz:** en la celda de la interfaz (empieza con `# Esta celda YA trae el import`), borra todo y pega:

📋 **Copia y pega:**

```python
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
```

🎤 **Di mientras carga:**
> "Fíjense en la última línea: share=True. Eso crea un link público, temporal, que funciona mientras este notebook siga abierto. Y show_error=True hace que, si algo falla, veamos por qué en lugar de un error mudo."

### Paso 3.3 · Compartir
🖱️ **Haz:**
1. Abre el link `https://….gradio.live` que imprime la celda.
2. Pide que cada pareja lo abra **desde su celular**.
3. Pide que peguen su link en el muro compartido proyectado.

🎤 **Di:**
> "Acaban de construir y publicar un prototipo de IA que cualquiera puede abrir. Prueben con tres días y un presupuesto muy bajo, y vean cómo reacciona."

⚠️ **Si aparece "La API no respondió":** 🎤 "Es el servicio de Google con mucha demanda. Esperen unos segundos y presionen de nuevo el botón."

---

## 0:40 – 0:45 · Showcase y cierre

🖱️ **Haz:**
1. Invita a 2 o 3 parejas voluntarias, **1 minuto cada una**: qué problema resuelve y para quién.
2. Ve a la **slide 5** y cierra con "de prototipo a producto".

🎤 **Di:**
> "Un prototipo no es un producto. Para dar el salto necesitan cuatro cosas. Evaluación: armen diez casos de prueba y midan cuántos pasan su validación. Costos: calculen cuánto cuesta cada consulta. Privacidad: no manden datos personales a la API si no hace falta. Y feedback: pongan el link en manos de cinco usuarios reales."

3. Ve a la **slide 6** (con el QR del repositorio).

🎤 **Di:**
> "Esto es el inicio, no el final. Tienen el repositorio completo para seguir. Y los invito a presentar su versión mejorada en un próximo meetup con Prisma Latam y GDG Huancayo."

4. **Foto grupal** con las laptops mostrando cada prototipo funcionando.

---

## Si algo falla (tabla rápida)

| Qué ves | Qué decir y hacer |
|---|---|
| `No encontré tu API key` | "El secreto debe llamarse GEMINI_API_KEY y tener activado Acceso desde el notebook." Ejecutar de nuevo la primera celda. |
| Aviso rojo de pip (`dependency conflicts`) | "Ignórenlo, es solo un aviso." |
| `503` o alta demanda | "Es Google, no su código. El notebook reintenta solo." Si persiste: cambiar a `MODEL = "gemini-3.1-flash-lite"` o poner `USE_MOCK = True`. |
| `429` / `RESOURCE_EXHAUSTED` | Esperar un minuto o usar `USE_MOCK = True`. |
| `404 model not found` | Cambiar `MODEL` por otro modelo Flash disponible. |
| `NameError: name 'gr' is not defined` | Borraron la celda de preparación o no pegaron el bloque completo. Pegar el bloque entero de la celda 3.2. |
| `AssertionError: Falta completar el TODO` | Falta pegar el código del paso indicado. |
| El link de Gradio no abre | Ejecutar de nuevo la celda de la interfaz y no cerrar la pestaña. |
| No hay internet | `USE_MOCK = True` en la primera celda: todo corre con respuestas precargadas. |
| Se atrasa un grupo | Abrir la rama del checkpoint anterior (tabla de enlaces). |

## Presupuesto de tiempo

| Fase | Minutos | Qué NO recortar |
|---|---|---|
| Bienvenida | 4 | Formar parejas |
| Demo y arquitectura | 6 | El diagrama |
| Checkpoint 1 | 10 | Que todos vean su primera respuesta |
| Checkpoint 2 | 12 | Las validaciones. El micro-reto se puede pasar a tarea. |
| Checkpoint 3 | 8 | El link en el celular: es el momento más motivador |
| Showcase y cierre | 5 | La foto grupal |

Si vas 5 minutos atrasado, pega el bloque completo en lugar de escribirlo, y salta el micro-reto.
