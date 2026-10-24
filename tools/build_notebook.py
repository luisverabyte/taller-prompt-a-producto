"""Arma taller.ipynb a partir de tools/celdas/ para un checkpoint dado.

Uso: python tools/build_notebook.py --stage {0,1,2,3} [--out taller.ipynb]

stage 0 = punto de partida (CP1, CP2 y CP3 con TODOs)
stage 1 = CP1 resuelto
stage 2 = CP1 y CP2 resueltos
stage 3 = todo resuelto (rama main)
"""
import argparse
import pathlib

import nbformat

RAIZ = pathlib.Path(__file__).resolve().parent.parent
CELDAS = RAIZ / "tools" / "celdas"

# (nombre base, tipo, etapa desde la que viene resuelta; None = siempre igual)
PASOS = [
    ("00_intro", "md", None),
    ("01_setup", "code", None),
    ("02_cp1", "md", None),
    ("03_cp1", "code", 1),
    ("04_cp2", "md", None),
    ("05_schemas", "code", None),
    ("06_prompt", "code", 2),
    ("07_validar", "code", 2),
    ("08_crear_ruta", "code", None),
    ("09_probar_ruta", "code", None),
    ("10_reto", "md", None),
    ("11_reto", "code", None),
    ("12_cp3", "md", None),
    ("13_html", "code", None),
    ("14_ui", "code", 3),
    ("15_cierre", "md", None),
]


def leer(base, tipo, desde, stage):
    ext = "md" if tipo == "md" else "py"
    if desde is None:
        ruta = CELDAS / f"{base}.{ext}"
    else:
        ruta = CELDAS / f"{base}.{'solved' if stage >= desde else 'todo'}.{ext}"
    return ruta.read_text(encoding="utf-8").rstrip("\n")


def construir(stage):
    nb = nbformat.v4.new_notebook()
    nb.metadata = {
        "colab": {"provenance": []},
        "kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"},
        "language_info": {"name": "python"},
    }
    for base, tipo, desde in PASOS:
        fuente = leer(base, tipo, desde, stage)
        celda = nbformat.v4.new_markdown_cell(fuente) if tipo == "md" else nbformat.v4.new_code_cell(fuente)
        celda["id"] = base.replace("_", "-")
        nb.cells.append(celda)
    return nb


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", type=int, choices=[0, 1, 2, 3], default=3)
    ap.add_argument("--out", default=str(RAIZ / "taller.ipynb"))
    args = ap.parse_args()
    nbformat.write(construir(args.stage), args.out)
    print(f"stage {args.stage} -> {args.out}")
