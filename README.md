# 🏔️ De prompt a producto

**Construye un prototipo de IA con la API de Gemini en 45 minutos.**
Taller hands-on (code-along) para GDG Huancayo y la comunidad Prisma Latam.

Al terminar tendrás un asistente que arma **rutas turísticas del Valle del Mantaro**, con interfaz web y un link público que puedes abrir desde tu celular. Después lo adaptas a un problema real tuyo.

```
prompt  →  llamada a la API  →  respuesta estructurada (JSON)  →  interfaz
```

## Empezar en 3 pasos (solo necesitas navegador y cuenta de Google)

1. **Crea tu API key** en [Google AI Studio](https://aistudio.google.com/apikey) (es gratis).
2. **Abre el notebook en Colab:**
   [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/luisverabyte/taller-prompt-a-producto/blob/cp0-inicio/taller.ipynb)
3. **Guarda tu key como secreto:** en Colab abre 🔑 **Secretos**, crea `GEMINI_API_KEY`, pega la key y activa **Acceso desde el notebook**.

Ejecuta la primera celda con ▶️ y sigue el notebook de arriba hacia abajo.

## Los 3 checkpoints

| # | Qué haces | Cuándo |
|---|---|---|
| 1 | Tu primera llamada a la API | min 10-20 |
| 2 | Del prompt a la lógica del producto: esquema JSON, system prompt y validaciones | min 20-32 |
| 3 | Interfaz con Gradio y link público | min 32-40 |

Cuando completes uno, levanta la mano o pega el sticker 🟢 verde. Si te atascas, pega el 🔴 rojo y un mentor te ayuda.

## ¿Te atrasaste? Salta a la rama del checkpoint anterior

Cada rama tiene el notebook con ese checkpoint **ya resuelto**. Si no pudiste terminar el CP1, abre la rama `cp1` y sigue con el CP2.

| Rama | Estado del notebook | Abrir |
|---|---|---|
| `cp0-inicio` | Punto de partida (CP1, CP2 y CP3 por completar) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/luisverabyte/taller-prompt-a-producto/blob/cp0-inicio/taller.ipynb) |
| `cp1-primera-llamada` | CP1 resuelto | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/luisverabyte/taller-prompt-a-producto/blob/cp1-primera-llamada/taller.ipynb) |
| `cp2-logica-producto` | CP1 y CP2 resueltos | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/luisverabyte/taller-prompt-a-producto/blob/cp2-logica-producto/taller.ipynb) |
| `cp3-interfaz` y `main` | Todo resuelto | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/luisverabyte/taller-prompt-a-producto/blob/main/taller.ipynb) |

## 🔌 Plan B: sin internet o sin API key

En la celda de preparación cambia:

```python
USE_MOCK = True
```

El notebook usa respuestas precargadas (`data/mock_responses.json`) y todo el código funciona igual. Es útil para ver el flujo completo aunque falle el wifi. Con el modo simulado la respuesta no cambia según tu prompt, solo según el número de días (1 a 3).

## Problemas frecuentes

| Error | Qué hacer |
|---|---|
| `No encontré tu API key` | El secreto debe llamarse exactamente `GEMINI_API_KEY` y tener activado **Acceso desde el notebook**. Vuelve a ejecutar la primera celda. |
| `429` o `RESOURCE_EXHAUSTED` | Alcanzaste el límite gratuito. Espera un minuto y reintenta, o usa `USE_MOCK = True`. Tus límites actuales están en AI Studio. |
| `503 UNAVAILABLE` (alta demanda) | El modelo está saturado. El notebook ya reintenta solo unos segundos. Si persiste, espera un minuto, prueba otro modelo (`MODEL = "gemini-3.1-flash-lite"`) o usa `USE_MOCK = True`. |
| `404` o `model not found` | Cambia `MODEL` en la primera celda por otro modelo Flash disponible. Para listarlos: `[m.name for m in client.models.list()]`. |
| Aviso rojo de pip: `dependency conflicts` | Ignóralo, no afecta al taller. Lo importante es que la celda termine con ✅ |
| `API key not valid` | Copiaste la key incompleta o con espacios. Genera otra en AI Studio. |
| El link de Gradio no abre | Ejecuta de nuevo la última celda. El link solo funciona mientras el notebook siga abierto y ejecutándose. |
| El JSON no pasa la validación | Es parte del taller: revisa tu system prompt y agrega la regla que falta. |

## Adáptalo a tu problema (micro-reto)

En el Checkpoint 2 hay una celda con **3 variables** (`ROL`, `DATOS`, `PREGUNTA`). Cámbialas por tu caso (turismo, agro, educación, comercio) y piensa en tres cosas:

1. **Usuario:** ¿para quién es?
2. **Caso de uso mínimo:** ¿qué es lo único que debe hacer bien?
3. **Métrica:** ¿cómo sabes que funciona?

## De prototipo a producto

- **Evaluación:** arma 10 casos de prueba y mide cuántos pasan tu validación.
- **Costos:** calcula el costo por consulta y cuántas harán tus usuarios.
- **Privacidad:** no envíes datos personales a la API si no es necesario.
- **Feedback:** pon el link en manos de 5 usuarios reales.

## Estructura del repositorio

```
taller.ipynb              notebook del taller (cambia según la rama)
mock_client.py            cliente simulado para el modo sin conexión
data/lugares.json         catálogo de lugares (datos de ejemplo, por verificar)
data/mock_responses.json  respuestas precargadas
tools/                    scripts para regenerar y probar los notebooks
materiales/               guía paso a paso, runbook, kit para la organización y temporizador
```

## Para el ponente

```bash
python tools/make_mock.py                       # regenera las respuestas precargadas si cambias lugares.json
python tools/build_notebook.py --stage 3        # regenera taller.ipynb (0 = inicio, 3 = completo)
python tools/smoke_test.py taller.ipynb         # prueba el notebook completo sin API key
```

> ⚠️ `data/lugares.json` contiene datos de ejemplo marcados con `"verificado": false`. Revísalos y reemplázalos antes del taller; luego ejecuta `make_mock.py` para que el modo sin conexión use los datos nuevos.

## Siguiente paso

Sube tu versión mejorada y preséntala en un próximo meetup con **Prisma Latam** y **GDG Huancayo**. 📸
