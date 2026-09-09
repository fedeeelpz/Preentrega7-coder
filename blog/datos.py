import json
from pathlib import Path

perfil_autor = {
    "nombre": "Federico Lopez",
    "bio": "Estudiante de ingenieria",
    "especialidad": "python",
    "redes_sociales": ["@fedeeelpz", "@Smqcked19"],
    "articulos_publicados": 1,
    "activo": True
}

estados_post = ('borrador', 'publicado', 'archivado')
etiquetas_blog = {'Python', 'Django', 'Web', 'Backend', 'html', 'C++', 'Java', 'SQL'}

# Ruta hacia el archivo JSON usando pathlib
ruta_json = Path(__file__).parent / "posts.json"


def cargar_posts():
    """
    Carga los posts desde posts.json.
    Retorna una lista vacía si el archivo no existe, está vacío o es corrupto.
    """
    # Verificamos la existencia con el método .exists() de Path
    if not ruta_json.exists():
        print("Aviso: 'posts.json' no existe. Se iniciará con lista vacía.")
        return []

    try:
        with open(ruta_json, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Error al leer 'posts.json' ({e}). Se iniciará con lista vacía.")
        return []


def guardar_posts(posts):
    """
    Guarda la lista de objetos Post convertidos a dict en posts.json.
    """
    lista_dicts = [p.to_dict() for p in posts]

    try:
        with open(ruta_json, "w", encoding="utf-8") as file:
            json.dump(lista_dicts, file, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar en 'posts.json': {e}")
        return False