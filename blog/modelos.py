from .datos import estados_post
from .validaciones import (buscar_por_titulo,filtrar_por_tag,listar_posts,validar_post,)

class Autor:
    def __init__(self,nombre,bio="",especialidad=None,redes_sociales=None,articulos_publicados=None,):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = (redes_sociales if redes_sociales is not None else [])
        self.articulos_publicados = (articulos_publicados if articulos_publicados is not None else [])

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "bio": self.bio,
            "especialidad": self.especialidad,
            "redes_sociales": self.redes_sociales,
            "articulos_publicados": self.articulos_publicados,
        }


class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

    @classmethod
    def from_dict(cls, d):
        return cls(
            id=d.get("id"),
            titulo=d.get("titulo"),
            contenido=d.get("contenido"),
            autor=d.get("autor"),
            tags=d.get("tags", []),
            estado=d.get("estado"),
        )

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict()
            if hasattr(self.autor, "to_dict")
            else self.autor,
            "tags": self.tags,
            "estado": self.estado,
        }


class Blog:
    def __init__(self, posts=None):
        self.posts = posts if posts is not None else []

    @classmethod
    def desde_lista_dicts(cls, lista_dicts):
        posts_objetos = []
        for d in lista_dicts:
            post_obj = (
                Post.from_dict(d) if hasattr(Post, "from_dict") else d
            )
            posts_objetos.append(post_obj)
        return cls(posts=posts_objetos)

    def crear_post(self, post):
        es_valido, mensaje = self.validar_post(post)
        if es_valido:
            self.posts.append(post)
            return True, mensaje
        return False, mensaje

    def validar_post(self, post):
        post_dict = (
            post.to_dict() if hasattr(post, "to_dict") else post
        )
        return validar_post(post_dict, estados_post)

    def obtener_posts(self):
        return self.posts

    def listar_posts(self):
        lista_dicts = [
            p.to_dict() if hasattr(p, "to_dict") else p for p in self.posts
        ]
        listar_posts(lista_dicts)

    def buscar_por_titulo(self, termino):
        lista_dicts = [
            p.to_dict() if hasattr(p, "to_dict") else p for p in self.posts
        ]
        return buscar_por_titulo(lista_dicts, termino)

    def filtrar_por_tag(self, tag):
        lista_dicts = [
            p.to_dict() if hasattr(p, "to_dict") else p for p in self.posts
        ]
        return filtrar_por_tag(lista_dicts, tag)