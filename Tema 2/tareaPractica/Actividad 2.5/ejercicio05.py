from anexo import series;
"""
5. Muestra una lista con los comentarios que tengan más de 40 caracteres.
"""
listaComentario = [(c["reseñas"], cm["comentario"]) for c in series for cm in c["reseñas"] if len(cm["comentario"]) > 40]
print(listaComentario)