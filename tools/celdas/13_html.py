import html


def ruta_a_html(ruta, problemas):
    """Convierte la ruta en tarjetas HTML (esto es solo presentación)."""
    if ruta is None:
        return "<p>😕 No pude armar una ruta. Intenta de nuevo.</p>"
    e = html.escape
    out = [f"<h3>{e(ruta.resumen)}</h3>",
           f"<p><b>Costo estimado:</b> S/ {ruta.costo_total_soles} por persona</p>"]
    for d in ruta.dias:
        out.append(f"<div style=\"border:1px solid #8884;border-radius:12px;padding:12px;margin:10px 0\">"
                   f"<h4>Día {d.dia}: {e(d.titulo)}</h4><ul>")
        for p in d.paradas:
            out.append(f"<li><b>{e(p.nombre)}</b> · {e(p.distrito)} · {p.horas} h · S/ {p.costo_soles}"
                       f"<br><i>💡 {e(p.tip)}</i></li>")
        out.append("</ul></div>")
    avisos = ([ruta.advertencia] if ruta.advertencia else []) + problemas
    for a in avisos:
        out.append(f"<p>⚠️ {e(a)}</p>")
    return "".join(out)
