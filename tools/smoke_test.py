"""Ejecuta taller.ipynb en modo SIN CONEXION (mock) y revisa que todo funcione.

Uso: python tools/smoke_test.py [ruta_notebook]
Sale con codigo 1 si falla alguna celda que no sea un TODO esperado.
"""
import json
import os
import pathlib
import sys
import traceback

import nbformat

RAIZ = pathlib.Path(__file__).resolve().parent.parent
os.chdir(RAIZ)
sys.path.insert(0, str(RAIZ))
ruta_nb = sys.argv[1] if len(sys.argv) > 1 else "taller.ipynb"
nb = nbformat.read(ruta_nb, as_version=4)

import gradio as gr

lanzadas = []
_launch = gr.Blocks.launch


def launch_local(self, *a, **kw):
    kw.update(share=False, prevent_thread_lock=True)
    lanzadas.append(self)
    return _launch(self, *a, **kw)


gr.Blocks.launch = launch_local

ns = {"__name__": "__main__"}
fallos = []
for celda in nb.cells:
    if celda.cell_type != "code":
        continue
    codigo = "\n".join(l for l in celda.source.splitlines() if not l.lstrip().startswith(("!", "%")))
    codigo = codigo.replace("USE_MOCK = False", "USE_MOCK = True")
    try:
        exec(compile(codigo, celda["id"], "exec"), ns)
        print(f"[ok]    {celda['id']}")
    except Exception as e:
        fallos.append(celda["id"])
        print(f"[FALLA] {celda['id']}: {type(e).__name__}: {e}")

# --- pruebas extra (solo si CP2 esta resuelto) ---
extras_ok = True
if "validar_ruta" in ns and "03-cp1" not in fallos:
    Ruta, Parada, Dia = ns["Ruta"], ns["Parada"], ns["Dia"]
    lugar = next(iter(ns["NOMBRES"]))
    mala = Ruta(resumen="x", costo_total_soles=999, dias=[Dia(dia=1, titulo="t", paradas=[
        Parada(nombre="Lugar inventado", distrito="d", horas=9, costo_soles=999, tip="t")])])
    problemas = ns["validar_ruta"](mala, 2, 100)
    print("validar(ruta mala):", len(problemas), "problemas")
    validar_pendiente = "TODO: agrega al menos dos validaciones" in open(ruta_nb, encoding="utf-8").read()
    extras_ok = validar_pendiente or len(problemas) >= 3
    if validar_pendiente:
        print("  (validar_ruta es un TODO en este checkpoint: se omite esa comprobacion)")

    # reintento: primer intento invalido, segundo valido
    buena = json.loads(open("data/mock_responses.json", encoding="utf-8").read())["ruta_2d"]
    respuestas = [json.dumps({"basura": True}), json.dumps(buena)]

    class R:
        def __init__(self, t): self.text = t

    class M:
        def generate_content(self, **kw): return R(respuestas.pop(0))

    class C:
        models = M()

    cliente_real = ns["client"]
    ns["client"] = C()
    ruta, probs = ns["crear_ruta"](2, 150, ["cultura"], "pareja")
    ns["client"] = cliente_real
    print("reintento ->", "ok" if ruta and not probs else f"FALLO {probs}")
    extras_ok = extras_ok and bool(ruta) and not probs

if lanzadas:
    from gradio_client import Client
    demo = lanzadas[-1]
    salida = Client(demo.local_url, verbose=False).predict(2, 150, ["cultura"], "pareja", api_name="/planificar")
    print("gradio /planificar ->", "html ok" if "<h3>" in salida else f"RARO: {salida[:80]}")
    extras_ok = extras_ok and "<h3>" in salida
    for d in lanzadas:
        d.close()

esperados = {"03-cp1"} if "TODO: llama al modelo" in open(ruta_nb, encoding="utf-8").read() else set()
inesperados = set(fallos) - esperados
print("\nFallos inesperados:", sorted(inesperados) or "ninguno", "| extras:", "ok" if extras_ok else "FALLAN")
sys.exit(1 if inesperados or not extras_ok else 0)
