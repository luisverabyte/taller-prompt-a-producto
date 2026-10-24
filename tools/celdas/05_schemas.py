from typing import Optional
from pydantic import BaseModel, ValidationError

with open("data/lugares.json", encoding="utf-8") as f:
    LUGARES = json.load(f)["lugares"]
NOMBRES = {l["nombre"] for l in LUGARES}
print(len(LUGARES), "lugares en el catálogo")


class Parada(BaseModel):
    nombre: str
    distrito: str
    horas: float
    costo_soles: int
    tip: str


class Dia(BaseModel):
    dia: int
    titulo: str
    paradas: list[Parada]


class Ruta(BaseModel):
    resumen: str
    dias: list[Dia]
    costo_total_soles: int
    advertencia: Optional[str] = None
