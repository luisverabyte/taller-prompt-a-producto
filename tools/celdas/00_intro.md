# 🏔️ De prompt a producto
**Taller de 45 min: construye un prototipo de IA con la API de Gemini.**

Al final tendrás un asistente que recomienda **rutas turísticas del Valle del Mantaro**, con una interfaz y un link público que puedes abrir desde tu celular. Después lo adaptas a un problema tuyo.

| Checkpoint | Qué haces | Tiempo |
|---|---|---|
| **1** | Tu primera llamada a la API | 10-20 min |
| **2** | Del prompt a la lógica del producto (JSON + validaciones) | 20-32 min |
| **3** | Interfaz con Gradio y link público | 32-40 min |

### Antes de empezar (una sola vez)
1. Crea tu API key en [Google AI Studio](https://aistudio.google.com/apikey).
2. En Colab abre 🔑 **Secretos** (panel izquierdo), crea uno llamado `GEMINI_API_KEY`, pega tu key y activa **Acceso desde el notebook**.
3. Ejecuta la celda de abajo con ▶️.

> 🆘 **¿Sin internet o sin key?** En la celda de preparación cambia `USE_MOCK = False` por `USE_MOCK = True`. El taller corre con respuestas precargadas y todo el código es el mismo.
>
> 🧭 **¿Te atrasaste?** Abre la rama del checkpoint anterior desde el README del repositorio: ya viene resuelto.
