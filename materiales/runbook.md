# Runbook del ponente: De prompt a producto (45 min)

> 🎤 Para el texto exacto que debes decir en cada paso, con el código para copiar y pegar, usa [guia-paso-a-paso.md](guia-paso-a-paso.md). Este runbook es el resumen de tiempos y contingencias.

Guion minuto a minuto. En cada fase: qué dices, qué haces en pantalla y qué haces si algo falla.

## Antes del taller (tu checklist personal)

- [ ] Reemplazar `data/lugares.json` con tu investigación (mismo formato) y correr `python tools/make_mock.py`.
- [ ] Abrir `main` en Colab con **tu** API key real y correrlo completo, de punta a punta.
- [ ] Abrir el link `share` de Gradio desde tu celular.
- [ ] Confirmar que `MODEL` en la primera celda existe con tu key. Si da 404, lista los modelos con `[m.name for m in client.models.list()]` y cambia la variable en `tools/celdas/01_setup.py`, luego `python tools/build_notebook.py --stage 3` y repite para cada rama.
- [ ] Probar el notebook con `USE_MOCK = True` con el wifi apagado.
- [ ] Tener abiertas en pestañas: la rama `main`, el notebook `cp0-inicio` (el que replica el público), el temporizador y las slides.
- [ ] Zoom de fuente del notebook al 150% y tema claro (se ve mejor en proyector).
- [ ] Tener tu propia API key lista en Secretos de Colab, y una segunda por si te limitan.

## 0:00 - 0:04  Bienvenida (4 min)

**Di:** el objetivo es salir con un prototipo funcionando, no solo ver una demo.
**Haz:** pregunta a mano alzada quién ya usó una API de IA. Pide que formen parejas mezclando perfiles. Proyecta el QR del repo.
**Si falla:** que quien no tenga laptop mire con su pareja; el trabajo es en pareja.

## 0:04 - 0:10  Demo y arquitectura (6 min)

**Di:** "Un chat responde texto libre. Un producto necesita respuestas con forma fija, reglas y una interfaz."
**Haz:**
1. Muestra el prototipo final (rama `main`, link público) con: 2 días, S/ 150, intereses artesanía + cultura, pareja.
2. Muestra el diagrama: `prompt → llamada a la API → respuesta estructurada → interfaz`.
3. Anuncia los 3 checkpoints y el sistema de stickers.

**Si falla la demo en vivo:** abre el notebook con `USE_MOCK = True`. Para el público es idéntico.

## 0:10 - 0:20  Checkpoint 1: primera llamada (10 min)

**Di:** "Un request son tres cosas: modelo, contenido y respuesta."
**Haz (code-along):**
1. Abre `cp0-inicio` en Colab. Que cada pareja haga lo mismo.
2. Ejecuta la celda de preparación. Muestra dónde pegar la key (🔑 Secretos).
3. Escribe en vivo la llamada del CP1 y ejecútala.
4. Esperas stickers verdes. Mentores atienden los rojos.

**Si alguien no tiene key o internet:** `USE_MOCK = True`.
**Si más del 30% sigue en rojo al minuto 18:** no esperes. Pide que pasen a la rama `cp1-primera-llamada` y sigue.
**Errores típicos:** secreto mal nombrado, acceso al notebook sin activar, 429 por límites (ver README).

## 0:20 - 0:32  Checkpoint 2: del prompt a la lógica del producto (12 min)

**Di:** "El prompt es el 20% del producto. Las reglas, el formato y las validaciones son el otro 80%."
**Haz:**
1. (2 min) Muestra el esquema Pydantic (`Ruta`, `Dia`, `Parada`) y explica por qué pedimos JSON.
2. (3 min) Escribe el system prompt: rol, reglas numeradas y "si no se puede, dilo en advertencia". Destaca la regla de usar **solo el catálogo**: evita inventos.
3. (3 min) Escribe `validar_ruta` con dos validaciones y ejecuta `crear_ruta`. Muestra el reintento si aparece.
4. (4 min) Micro-reto: cada pareja cambia `ROL`, `DATOS` y `PREGUNTA`.

**Dato para decir en vivo:** la validación revisa lo que le pides (lugares del catálogo, costo, días), no que los tips sean verdad. En las pruebas el modelo agregó detalles que no estaban en el catálogo. Validar es decidir qué revisas.
**Tips de PM (30 segundos, dilos mientras escriben):** define el usuario, el caso de uso mínimo y la métrica. Ejemplo de métrica: porcentaje de rutas válidas a la primera.
**Si vas tarde:** salta el micro-reto y pásalo a la tarea. **Nunca recortes el CP3**, es el momento más motivador.
**Rama de rescate:** `cp2-logica-producto`.

## 0:32 - 0:40  Checkpoint 3: interfaz y compartir (8 min)

**Di:** "Una API no es un producto hasta que alguien que no programa puede usarla."
**Haz:**
1. Muestra la función `planificar` y explica que Gradio solo conecta entradas con esa función.
2. Escribe el `gr.Blocks` (o pégalo si vas justo de tiempo) y ejecuta `demo.launch(share=True)`.
3. Pide que abran el link en su celular y lo suban al muro compartido.

**Si el link muestra "Error" sin detalle:** la API falló al responder. Con `show_error=True` ahora se ve el motivo; casi siempre es el 503 de alta demanda: espera unos segundos y pulsa el botón de nuevo.
**Si falla `share=True`:** sin internet el link público no existe. Usa la URL local o la pestaña embebida de Colab y muestra desde ahí.
**Rama de rescate:** `cp3-interfaz`.

## 0:40 - 0:45  Showcase y cierre (5 min)

**Haz:**
1. Elige 2 o 3 parejas voluntarias, 1 minuto cada una: qué problema resuelve y para quién.
2. Cierra con "de prototipo a producto": evaluación (10 casos de prueba), costos (por consulta), privacidad (no datos personales a la API) y feedback (5 usuarios reales).
3. Invita a Prisma Latam y GDG Huancayo a presentar su versión mejorada en un próximo meetup.
4. **Foto grupal** con las laptops mostrando cada prototipo funcionando.

## Plan de contingencias

| Qué pasa | Qué haces |
|---|---|
| Se cae el wifi | Hotspot propio. Si tampoco hay: `USE_MOCK = True` para todos. |
| Error 503 "alta demanda" en varias parejas | Es el servicio de Google, no el código. El notebook reintenta solo. Si persiste: que cambien a `MODEL = "gemini-3.1-flash-lite"` o pasen a `USE_MOCK = True`. Tú sigue con el mock en pantalla. |
| Muchos 429 a la vez | Todos comparten la IP del local, pero los límites son por proyecto. Pide que cada pareja use su propia key y espacia las ejecuciones. Si persiste: mock. |
| Colab no abre o está lento | Que usen la rama más cercana desde su celular o con su pareja. Tú sigues desde tu pantalla. |
| Vas 5 minutos atrasado | Pega `validar_ruta` y el `gr.Blocks` completos desde las ramas en lugar de escribirlos. |
| Te quedas sin tiempo | Cierra con el showcase de 2 parejas y comparte el repo. |

## Enlaces del ponente

- Slides (6): https://claude.ai/artifact/EzxFRTU9of6zAR5kDQyf7H
- Temporizador (también en `materiales/temporizador.html`, funciona sin conexión una vez abierto): https://claude.ai/artifact/L1DZjfz6VDavxRXdjQmaMh

Atajos del temporizador: `espacio` inicia o pausa, `←` y `→` cambian de fase, `+` y `-` ajustan un minuto, `R` reinicia y `F` pone pantalla completa.
