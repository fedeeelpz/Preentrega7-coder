from .blog.datos import cargar_posts, guardar_posts
from .blog.menu import mostrar_menu
from .blog.modelos import Blog
from .blog.operaciones import crear_nuevo_post_interactivo
#Vamos a definir la funcion la cual se encarga de la logica del menu interactivo y mostrarlo en pantalla al usuario para que pueda realizar las opciones que elija
def main():
    #Importamos datos iniciales desde el archivo posts.json el cual almacena la informacion de los posts publicados por un usuario
    datos_iniciales = cargar_posts()
    mi_blog = Blog.desde_lista_dicts(datos_iniciales)

    while True:
        opcion_usuario = mostrar_menu()

        # Opcion 1: Ver todos los posts
        if opcion_usuario == 1:
            mi_blog.listar_posts()

        # Opción 2: Buscar por título
        elif opcion_usuario == 2:
            palabra_a_buscar = input("Ingrese la palabra que desea buscar en los títulos: ").strip()
            hallados = mi_blog.buscar_por_titulo(palabra_a_buscar)
            if hallados:
                for p in hallados:
                    print(f"- {p.titulo}")
            else:
                print("No se encontraron coincidencias.")

        # Opción 3: Filtrar por tag
        elif opcion_usuario == 3:
            tag_a_buscar = input("Ingrese el tag que desea buscar en los posts: ").strip()
            hallados = mi_blog.filtrar_por_tag(tag_a_buscar)
            if hallados:
                for p in hallados:
                    print(f"- {p.titulo}")
            else:
                print("No se encontraron posts con esa etiqueta.")

        # Opcion 4: Crear nuevo post
        elif opcion_usuario == 4:
            nuevo_post = crear_nuevo_post_interactivo()
            exito, mensaje = mi_blog.crear_post(nuevo_post)
            print(mensaje)
            if exito:
                # Guardamos el post debido a que se creo de forma exitosa en nuestro archivo posts.json
                guardar_posts(mi_blog.obtener_posts())

       # Opción 5: Validar posts
        elif opcion_usuario == 5:
            posts = mi_blog.obtener_posts()
            if posts:
                print("\n--- POSTS DISPONIBLES PARA VALIDAR ---")
                for idx, p in enumerate(posts, start=1):
                    print(f"{idx}. {p.titulo}")
                try:
                    indice = int(input("Ingrese el número del post que desea validar: "))
                    if 1 <= indice <= len(posts):
                        es_valido, mensaje = mi_blog.validar_post(posts[indice - 1])
                        print(f"Resultado: {mensaje}")
                    else:
                        print("Número de post inválido.")
                except ValueError:
                    print("Debe ingresar un número entero válido.")
            else:
                print("No hay posts disponibles para validar.")

        # Opcion 6: Guardar posts en JSON
        elif opcion_usuario == 6:
            if guardar_posts(mi_blog.obtener_posts()):
                print("¡Posts guardados exitosamente en posts.json!")
        # Opcion 7: Salir
        elif opcion_usuario == 7:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break

        else:
            print("Opción inválida, intenta de nuevo.")

#Realizamos la llamada a la funcion una vez nos aseguramos que el nombre del usuario es el correcto para dar inicio a la accion que desea hacer
if __name__ == "__main__":
    main()