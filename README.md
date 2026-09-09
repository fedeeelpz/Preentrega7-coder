# Proyecto de consola interactiva
## Funcionalidades de la consola
Este proyecto contiene los siguientes módulos:
--- datos.py: Este módulo maneja la persistencia y la lectura/escritura de datos desde el archivo posts.json.
    Contiene:
        diccionario: perfil_autor: Este diccionario almacena la información del autor de los posts
        tupla: estados_post: Contiene 3 estados posibles para todos los posts
        set: etiquetas_blog: Contiene las posibles etiquetas para los posts
        funciones: cargar_posts() y guardar_posts() para la interacción con posts.json
--- menu.py: Contiene la función mostrar_menu() la cual sirve para mostrar las opciones del menú interactivo en pantalla al usuario. El menú consta de 7 opciones donde las primeras 6 accionan sobre los métodos del objeto Blog y la última opción (7) finaliza la ejecución del programa.
--- operaciones.py: Contiene la función interactiva crear_nuevo_post_interactivo() para recopilar los datos introducidos por el usuario.
--- validaciones.py: Contiene la función validar_post(post, estados_permitidos) para verificar la estructura y datos obligatorios de un post.
--- modelos.py: Define las clases principales del sistema:
    Clase Post: Encapsula los atributos de una publicación (id, título, contenido, autor, tags, estado) y permite convertirlos mediante to_dict() y from_dict().
    Clase Blog: Administra la colección de objetos Post, conteniendo la lógica de negocio y sus métodos para listar, buscar, filtrar, crear y validar posts.
--- main.py: Aquí es donde se ejecuta el código para poner en funcionamiento el menú interactivo como punto de entrada del programa, protegido por el bloque if __name__ == "__main__":.

## Ejecución:
debemos escribir en la terminal el comando python main.py para ejecutar el sistema

## Qué hace cada opción del menú:
1 ---> Muestra en consola la información detallada de cada publicación en la lista llamando a mi_blog.listar_posts().
2 ---> Busca publicaciones cuyo título contenga un término específico (case-insensitive) llamando a mi_blog.buscar_por_titulo().
3 ---> Filtra publicaciones que contengan una etiqueta específica (case-insensitive) llamando a mi_blog.filtrar_por_tag().
4 ---> Recopila los datos para crear un nuevo post interactivo, lo incluye en el blog con mi_blog.crear_post() y guarda los cambios en posts.json.
5 ---> Permite elegir un post de la lista para verificar la estructura, las claves obligatorias y los tipos de datos llamando a mi_blog.validar_post().
6 ---> Guarda explícitamente el estado actual de los posts de la instancia Blog en el archivo posts.json mediante guardar_posts().
7 ---> Finaliza la ejecución del menú.

## Cambios respecto al checkpoint anterior:
* Se migró el sistema a Programación Orientada a Objetos (POO) mediante la creación de las clases Blog y Post en modelos.py.
* Se implementó la persistencia de datos con archivos JSON mediante las funciones cargar_posts() y guardar_posts() en datos.py, reemplazando la lista estática en memoria.
* Se ampliaron las opciones del menú de 5 a 7 para dar soporte al flujo completo de creación interactiva y guardado manual en posts.json.