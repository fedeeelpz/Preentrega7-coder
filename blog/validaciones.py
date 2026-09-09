def validar_post(post, estados_permitidos):
    """
    Valida la estructura, las claves obligatorias y los tipos de datos de un post.

    Args:
        post (dict): Diccionario que contiene la información de la publicación.
        estados_permitidos (tuple | list | set): Colección con los estados válidos 
            que puede tener el post (ej. 'borrador', 'publicado', 'archivado').

    Returns:
        tuple: Contiene dos elementos:
            - bool: True si el post cumple con todas las reglas, False en caso contrario.
            - str: Mensaje descriptivo de éxito o del error específico encontrado.
    """
    if not isinstance(post, dict):
        return False, 'El post debe ser un diccionario.'
    claves_obligatorias = ['id', 'titulo', 'contenido', 'autor', 'tags', 'estado']
    for clave in claves_obligatorias:
        if clave not in post:
            return False, f"Falta la clave obligatoria '{clave}'"
    if not isinstance(post['titulo'], str) or (post['titulo'].strip() == ''):
        return False, 'El titulo no puede estar vacio'
    if not isinstance(post['contenido'], str) or (post['contenido'].strip() == ''):
        return False, 'El contenido no puede estar vacío.'
    if not isinstance(post['autor'], dict):
        return False, 'El autor debe ser un diccionario.'
    if 'nombre' not in post['autor']:
        return False, "El autor debe contener la clave 'nombre' válida."
    if not isinstance(post['tags'], list):
        return False, 'Los tags deben ser una lista.'
    if post['estado'] not in estados_permitidos:
        return False, f"El estado '{post['estado']}' no es válido."
    return True, 'El post es válido.'