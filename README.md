# Blog Django
    Proyecto en desarrollo backend de un blog web.
## Descripción
    ---Este repositorio contiene la estructura base de un futuro blog mediante Django.  
    ---Incluye la configuración base del proyecto y una aplicación llamada `posts`.
## Instalación
Clonar el repositorio:
    ```bash
    git clone https://github.com/fedeeelpz/Preentrega6-coder
```
Entrar a la carpeta del proyecto:
    ```
    cd blog_consola
```
Crear entorno virtual:
    python -m venv venv
Activar entorno virtual:
    En Windows PowerShell:
        ```
        .\venv\Scripts\Activate.ps1
    
    En Linux o macOS:
        ```
        source venv/bin/activate
    ```
Instalar dependencias:
    ```
    pip install -r requirements.txt
```
Ejecutar el servidor:
    ```
    python manage.py runserver
```
Abrir en el navegador:
    http://127.0.0.1:8000/
Aplicaciones
    - posts: aplicación inicial para manejar las publicaciones del blog.