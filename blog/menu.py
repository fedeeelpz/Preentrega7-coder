def mostrar_menu():
    print('--- MENU DEL BLOG ---')
    print('1. Ver todos los posts')
    print('2. Buscar por titulo')
    print('3. Filtrar por tag')
    print('4. validar posts')
    print('5. Salir')
    try:
        opcion = int(input('Ingrese una opcion:'))
        return opcion
    except ValueError:
        print('Ingrese unicamente numeros, intente de nuevo')
        return None