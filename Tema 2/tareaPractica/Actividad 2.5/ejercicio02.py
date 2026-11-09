from anexo import series;
"""
2. Muestra los títulos de las series que sean de Fantasía o Misterio.
"""

titulosSeiresFM = [s["titulo"] for s in series if "Fantasía" in s["generos"] or "Misterio" in s["generos"]]
print(titulosSeiresFM)