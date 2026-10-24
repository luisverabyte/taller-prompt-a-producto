# Kit para la organización: taller "De prompt a producto"

Este documento reúne todo lo que necesita la organización del evento (GDG Huancayo / Prisma Latam). El ponente solo se encarga del contenido y de dictar el taller.

**Formato:** taller práctico de 45 minutos, en parejas, con laptop. Cada pareja sale con un prototipo de IA funcionando.

## 1. Mensaje previo para los asistentes (enviar 1 día antes)

### Versión corta (WhatsApp)

> 👋 ¡Mañana es el taller **De prompt a producto**! Para aprovecharlo, ven con:
> 💻 Tu laptop **cargada** (y cargador por si acaso)
> 🔑 Tu **API key de Gemini ya creada** (toma 2 minutos, es gratis): https://aistudio.google.com/apikey
> 🌐 Una cuenta de Google (usaremos Google Colab, no necesitas instalar nada)
> 📲 Un celular para probar tu prototipo
> Trabajaremos en parejas. Si ya usaste IA, ¡ven a ayudar! Si recién empiezas, ¡ven a aprender!

### Versión larga (correo)

**Asunto:** Taller De prompt a producto: qué traer

Hola,

Mañana construiremos en 45 minutos un prototipo de IA funcionando usando la API de Gemini. Para que no pierdas tiempo, por favor prepara lo siguiente:

1. **Laptop cargada.** No necesitas instalar programas: trabajaremos desde el navegador con Google Colab.
2. **Una cuenta de Google** para abrir Colab.
3. **Tu API key de Gemini ya creada.** Entra a https://aistudio.google.com/apikey, inicia sesión y presiona "Crear clave de API". Guárdala, la usaremos al inicio.
4. **Tu celular**, para abrir tu prototipo y compartirlo.

Trabajaremos en parejas, mezclando a quienes ya usaron una API de IA con quienes recién empiezan.

¡Nos vemos!

## 2. Códigos QR

Los QR se generan al publicar el repositorio y quedan en `materiales/qr/`:

| Archivo | Para qué sirve |
|---|---|
| `qr-repositorio.png` | Lleva al repositorio con las instrucciones y los notebooks. Para proyectar y para las mesas. |
| `qr-muro.png` | Lleva al formulario donde cada pareja sube su link (solo si crean el formulario). |

## 3. Muro de links (Google Form)

Crear un formulario de respuesta corta y proyectar la hoja de respuestas en pantalla. Preguntas:

1. Nombre de la pareja (obligatoria)
2. ¿Qué problema resuelve su prototipo? (una frase)
3. ¿Para quién es? (usuario)
4. Link público de Gradio (obligatoria, debe empezar con `https://`)

## 4. Guía para los mentores (1 página)

**Su rol:** recorrer la sala y atender a quienes tengan sticker 🔴 rojo. No resuelvan por ellos: guíenlos a la causa.

| Síntoma | Causa probable | Qué hacer |
|---|---|---|
| `No encontré tu API key` | El secreto no existe o está mal nombrado | Debe llamarse exactamente `GEMINI_API_KEY`, sin espacios |
| Lo mismo, con el nombre correcto | No activó "Acceso desde el notebook" | Interruptor del secreto en el panel 🔑 |
| `API key not valid` | Key copiada incompleta | Generar otra en AI Studio y pegarla de nuevo |
| `429` / `RESOURCE_EXHAUSTED` | Límite gratuito alcanzado | Esperar 1 minuto. Si sigue: `USE_MOCK = True` |
| `404 model not found` | El modelo cambió de nombre | Cambiar la variable `MODEL` en la primera celda |
| Aviso rojo de pip: `dependency conflicts` | Ignóralo. No afecta al taller; confirma que al final de la celda salga ✅ |
| `ModuleNotFoundError` | No ejecutó la primera celda | Ejecutar la celda de preparación |
| `AttributeError: 'NoneType'...` en el CP1 | Dejó `respuesta = None` | Completar el TODO de la llamada |
| El link de Gradio no abre | Notebook cerrado o celda detenida | Volver a ejecutar la última celda y mantener la pestaña abierta |
| Va muy atrasado | | Abrir la rama del checkpoint anterior desde el README (ya viene resuelto) |
| Sin internet | | `USE_MOCK = True` en la primera celda: todo corre con respuestas precargadas |

## 5. Checklist de logística

**Materiales**
- [ ] Stickers verdes y rojos (uno de cada color por pareja como mínimo)
- [ ] QR del repositorio en cada mesa (impresos o proyectados)
- [ ] Temporizador visible en pantalla durante todo el taller

**Personas**
- [ ] 2 o 3 mentores del GDG recorriendo la sala
- [ ] Alguien que tome la foto grupal final

**Espacio y conexión**
- [ ] Wifi probado con la cantidad de asistentes esperada, más un hotspot de respaldo
- [ ] Tomas de corriente o regletas para las mesas
- [ ] Proyector con buena visibilidad (el ponente sube el zoom de fuente al 150%)

**Cierre**
- [ ] Foto grupal con las laptops mostrando cada prototipo funcionando
- [ ] Invitar a presentar la versión mejorada en un próximo meetup de Prisma Latam y GDG Huancayo
