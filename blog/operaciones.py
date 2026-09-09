from .datos import estados_post, perfil_autor
from .modelos import Post
def listar_posts(lista):
    """
    Muestra en consola la información detallada de cada publicación en la lista.

    Args:
        lista (list): Lista de diccionarios donde cada uno representa un post.

    Handling:
        Captura la excepción KeyError en caso de que algún post no contenga
        las claves esperadas ('id', 'titulo', 'contenido', 'autor', etc.).
    """
    try:
        for post in lista:
            print(f"Id del post: {post['id']}, Titulo: {post['titulo']}, Contenido: {post['contenido']}, Autor: {post['autor']['nombre']}, Tags: {post['tags']}, Estado: {post['estado']}")
    except KeyError as e:
        print(f'Error: falta la clave {e} en uno de los posts')
def buscar_por_titulo(lista, termino):
    """
    Busca publicaciones cuyo título contenga un término específico (case-insensitive).

    Args:
        lista (list): Lista de diccionarios de publicaciones.
        termino (str): Texto o palabra clave a buscar dentro de los títulos.

    Returns:
        list: Lista con los posts coincidentes.
    """
    termino_normalizado = termino.lower().strip()
    encontrados = []
    for post in lista:
        if termino_normalizado in post['titulo'].lower():
            encontrados.append(post)
    if len(encontrados) > 0:
        print(f"\n --- Publicaciones encontradas para '{termino}' ---")
        for post in encontrados:
            print(f"ID: {post['id']} | Título: {post['titulo']}")
    else:
        print(f"\n No se encontraron publicaciones con la palabra '{termino}'.")
    return encontrados
def filtrar_por_tag(lista, tag):
    """
    Filtra publicaciones que contengan una etiqueta específica (case-insensitive).

    Args:
        lista (list): Lista de diccionarios de publicaciones.
        tag (str): Etiqueta o categoría a buscar dentro de las etiquetas del post.

    Returns:
        list: Lista de las publicaciones que contienen el tag.
    """
    tag_buscado = tag.lower().strip()
    tags_encontrados = []
    for post in lista:
        tags_post_minuscula = [t.lower() for t in post['tags']]
        if tag_buscado in tags_post_minuscula:
            tags_encontrados.append(post)
    if len(tags_encontrados) > 0:
        print(f"\n--- Posts con el tag '{tag}' ---")
        for post in tags_encontrados:
            print(f"ID: {post['id']} | Título: {post['titulo']} | Tags: {post['tags']}")
    else:
        print(f"\nNo se encontraron posts con el tag '{tag}'.")
    return tags_encontrados

def crear_nuevo_post_interactivo():
    "Esta funcion se encarga de solicitarle al usuairio una lista de atributos para asignarle a su nuevo post que quiere publicar, automaticamente este post lo creamos como un objeto de la clase post"
    print("\n--- CREAR NUEVO POST ---")
    post_id = input("Ingrese el ID único del post: ").strip()
    titulo = input("Ingrese el título: ").strip()
    contenido = input("Ingrese el contenido: ").strip()

    # Selección de etiquetas separadas por coma
    tags_string = input("Ingrese etiquetas separadas por coma por ejemplo (Python, Django): ")
    tags = [tag.strip() for tag in tags_string.split(",") if tag.strip()]

    # Validación contra tu tupla estados_post
    print(f"Estados disponibles: {estados_post}")
    estado = input("Ingrese el estado: ").strip().lower()
    if estado not in estados_post:
        estado = "borrador"

    # Instanciación utilizando tu diccionario perfil_autor
    nuevo_post = Post(
        id=post_id,
        titulo=titulo,
        contenido=contenido,
        autor=perfil_autor,
        tags=tags,
        estado=estado,
    )

    return nuevo_post

