from Producto import Producto
import requests
import json

from Cliente import Cliente
from ClienteJuridico import ClienteJuridico
#revisar si se agrega el producto bien con su id

def crearProducto (id_producto,name,description,price,category,inventory,compatible_vehicles,productos_objeto,productos):
    nuevo_producto = Producto(id_producto,name,description,price,category,inventory,compatible_vehicles)
    productos_objeto.append(nuevo_producto)
    productos.append(nuevo_producto.mostrar_producto())

def buscarProductosPorCategoria(productos_objeto):
    '''
    Función que muestra los productos según la categoría seleccionada.
    Muestra una lista de categorías disponibles y permite al usuario seleccionar una para ver los productos correspondientes.
    '''
    categorias = set(producto.category for producto in productos_objeto)
    categorias = list(categorias)
    
    print("Categorías disponibles:")
    for i, categoria in enumerate(categorias):
        print(f"{i + 1} -- {categoria}")

    opcion = input("Ingrese el número de la categoría que desea buscar: ")
    if opcion.isnumeric() and 1 <= int(opcion) <= len(categorias):
        categoria_seleccionada = categorias[int(opcion) - 1]
        print(f"Productos en la categoría '{categoria_seleccionada}':")
        for producto in productos_objeto:
            if producto.category == categoria_seleccionada:
                print(producto.mostrar_producto())
    else:
        print("Opción inválida")


def buscarProductosPorPrecio(productos_objeto):
    '''
    Función que permite buscar productos dentro de un rango de precios.
    Solicita al usuario que ingrese el rango de precios y muestra los productos dentro de ese rango.
    '''
    try:
        precio_min = float(input("Ingrese el precio mínimo: "))
        precio_max = float(input("Ingrese el precio máximo: "))
        print(f"Productos con precio entre {precio_min} y {precio_max}:")

        for producto in productos_objeto:
            if precio_min <= producto.price <= precio_max:
                print(producto.mostrar_producto())
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos para los precios.")


def buscarProductosPorNombre(productos_objeto):
    '''
    Función que permite buscar productos por nombre.
    Solicita al usuario el nombre o parte del nombre y muestra los productos correspondientes.
    '''
    nombre = input("Ingrese el nombre o parte del nombre del producto que desea buscar: ").lower()
    print(f"Productos que contienen '{nombre}' en su nombre:")

    for producto in productos_objeto:
        if nombre in producto.name.lower():
            print(producto.mostrar_producto())


def buscarProductosPorDisponibilidad(productos_objeto):
    '''
    Función que muestra los productos disponibles en inventario según la cantidad mínima especificada.
    Solicita al usuario que ingrese una cantidad mínima y muestra los productos con inventario igual o mayor a esa cantidad.
    '''
    try:
        cantidad_minima = int(input("Ingrese la cantidad mínima de inventario: "))
        print(f"Productos con inventario mayor o igual a {cantidad_minima} unidades:")

        for producto in productos_objeto:
            if producto.inventory >= cantidad_minima:
                print(producto.mostrar_producto())
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para la cantidad mínima.")

def modificarProducto(id_producto, productos_objeto, productos):
    '''
    Función para modificar la información de un producto existente.
    Permite al usuario modificar solo los campos que desee y actualiza el archivo JSON.
    '''
    # Buscar el producto con el ID correspondiente
    producto_encontrado = None
    for producto in productos_objeto:
        if producto.id == id_producto:
            producto_encontrado = producto
            break

    if producto_encontrado:
        print(f"Producto encontrado: {producto_encontrado.mostrar_producto()}")
        
        # Solicitar al usuario la nueva información para cada campo, si el usuario lo desea
        nuevo_nombre = input(f"Nuevo nombre (actual: {producto_encontrado.name}) o presione Enter para no cambiar: ")
        if nuevo_nombre:  # Si el usuario ingresa un nuevo valor, actualiza
            producto_encontrado.name = nuevo_nombre
        
        nueva_descripcion = input(f"Nueva descripción (actual: {producto_encontrado.description}) o presione Enter para no cambiar: ")
        if nueva_descripcion:  # Si el usuario ingresa un nuevo valor, actualiza
            producto_encontrado.description = nueva_descripcion
        
        nuevo_precio = input(f"Nuevo precio (actual: {producto_encontrado.price}) o presione Enter para no cambiar: ")
        if nuevo_precio:  # Si el usuario ingresa un nuevo valor, actualiza
            producto_encontrado.price = nuevo_precio
        
        nueva_categoria = input(f"Nueva categoría (actual: {producto_encontrado.category}) o presione Enter para no cambiar: ")
        if nueva_categoria:  # Si el usuario ingresa un nuevo valor, actualiza
            producto_encontrado.category = nueva_categoria
        
        nuevo_inventario = input(f"Nuevo inventario (actual: {producto_encontrado.inventory}) o presione Enter para no cambiar: ")
        if nuevo_inventario:  # Si el usuario ingresa un nuevo valor, actualiza
            producto_encontrado.inventory = nuevo_inventario
        
        nuevos_vehiculos = input(f"Nuevos vehículos compatibles (actual: {producto_encontrado.compatible_vehicles}) o presione Enter para no cambiar: ")
        if nuevos_vehiculos:  # Si el usuario ingresa un nuevo valor, actualiza
            producto_encontrado.compatible_vehicles = nuevos_vehiculos
        
        # Actualizamos la lista de productos con la información modificada
        productos = [producto.mostrar_producto() for producto in productos_objeto]
        
        # Guardamos los cambios en el archivo JSON
        datos_actualizados = []
        for producto in productos_objeto:
            producto_dict = {
                "id": producto.id,
                "name": producto.name,
                "description": producto.description,
                "price": producto.price,
                "category": producto.category,
                "inventory": producto.inventory,
                "compatible_vehicles": producto.compatible_vehicles
            }
            datos_actualizados.append(producto_dict)
        
        # Guardamos la lista de productos actualizada en el archivo JSON
        with open('productos.json', 'w', encoding='utf-8') as archivo_productos:
            json.dump(datos_actualizados, archivo_productos, ensure_ascii=False, indent=2)
        
        print("Producto modificado con éxito.")
        print(producto_encontrado.mostrar_producto())  # Mostrar el producto actualizado

    else:
        print("Producto no encontrado.")

def eliminarProducto(id_producto, productos_objeto, productos):
    '''
    Función para eliminar un producto por su ID.
    Elimina el producto de la lista y actualiza el archivo JSON.
    '''
    # Buscar el producto con el ID correspondiente
    producto_encontrado = None
    for producto in productos_objeto:
        if producto.id == id_producto:
            producto_encontrado = producto
            break

    if producto_encontrado:
        # Eliminar el producto de la lista de objetos
        productos_objeto.remove(producto_encontrado)

        # Actualizar la lista de productos con los productos restantes
        productos = [producto.mostrar_producto() for producto in productos_objeto]

        # Guardar los cambios en el archivo JSON
        datos_actualizados = []
        for producto in productos_objeto:
            producto_dict = {
                "id": producto.id,
                "name": producto.name,
                "description": producto.description,
                "price": producto.price,
                "category": producto.category,
                "inventory": producto.inventory,
                "compatible_vehicles": producto.compatible_vehicles
            }
            datos_actualizados.append(producto_dict)

        # Guardamos la lista de productos actualizada en el archivo JSON
        with open('productos.json', 'w', encoding='utf-8') as archivo_productos:
            json.dump(datos_actualizados, archivo_productos, ensure_ascii=False, indent=2)

        print(f"Producto con ID {id_producto} eliminado con éxito.")
    else:
        print(f"Producto con ID {id_producto} no encontrado.")

# Función para agregar cliente al archivo JSON
def agregar_cliente_json(cliente):
    # Convertir el objeto cliente en un diccionario
    if isinstance(cliente, ClienteJuridico):
        cliente_data = {
            "nombre_apellido": cliente.nombre_apellido,
            "cedula": cliente.cedula,
            "correo": cliente.correo,
            "direccion": cliente.direccion,
            "telefono": cliente.telefono,
            "nombre_contacto": cliente.nombre_contacto,
            "telefono_contacto": cliente.telefono_contacto,
            "correo_contacto": cliente.correo_contacto,
            "tipo": "Juridico"
        }
    else:
        cliente_data = {
            "nombre_apellido": cliente.nombre_apellido,
            "cedula": cliente.cedula,
            "correo": cliente.correo,
            "direccion": cliente.direccion,
            "telefono": cliente.telefono,
            "tipo": "Natural"
        }
    
    # Leer el contenido existente en el archivo JSON (si existe)
    try:
        with open("clientes.json", "r") as file:
            clientes_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        clientes_data = []

    # Agregar el nuevo cliente a la lista de datos
    clientes_data.append(cliente_data)

    # Guardar todos los datos de clientes en el archivo JSON
    with open("clientes.json", "w") as file:
        json.dump(clientes_data, file, indent=4)

def cargar_clientes_json():
    try:
        with open("clientes.json", "r") as file:
            clientes_data = json.load(file)
        return clientes_data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def modificar_cliente_json(cedula_buscar):
    clientes_data = cargar_clientes_json()  # Llamar a la función que carga los datos desde el archivo
    
    # Buscar el cliente por su cédula
    cliente_encontrado = None
    for cliente in clientes_data:
        if cliente["cedula"] == cedula_buscar:
            cliente_encontrado = cliente
            break
    
    if cliente_encontrado:
        print("Cliente encontrado:")
        print(cliente_encontrado)

        # Modificar los datos del cliente
        print("Ingrese los nuevos datos o presione Enter para dejar el valor actual:")
        
        cliente_encontrado["nombre_apellido"] = input(f"Nombre y Apellido/Razón Social ({cliente_encontrado['nombre_apellido']}): ") or cliente_encontrado["nombre_apellido"]
        cliente_encontrado["correo"] = input(f"Correo electrónico ({cliente_encontrado['correo']}): ") or cliente_encontrado["correo"]
        cliente_encontrado["direccion"] = input(f"Dirección ({cliente_encontrado['direccion']}): ") or cliente_encontrado["direccion"]
        cliente_encontrado["telefono"] = input(f"Teléfono ({cliente_encontrado['telefono']}): ") or cliente_encontrado["telefono"]
        
        # Si el cliente es jurídico, modificar los datos adicionales
        if cliente_encontrado["tipo"] == "Juridico":
            cliente_encontrado["nombre_contacto"] = input(f"Nombre del contacto ({cliente_encontrado['nombre_contacto']}): ") or cliente_encontrado["nombre_contacto"]
            cliente_encontrado["telefono_contacto"] = input(f"Teléfono de contacto ({cliente_encontrado['telefono_contacto']}): ") or cliente_encontrado["telefono_contacto"]
            cliente_encontrado["correo_contacto"] = input(f"Correo de contacto ({cliente_encontrado['correo_contacto']}): ") or cliente_encontrado["correo_contacto"]
        
        # Guardar los datos actualizados en el archivo JSON (sin llamar a agregar_cliente_json)
        with open("clientes.json", "w") as file:
            json.dump(clientes_data, file, indent=4)
        
        print("Información del cliente actualizada correctamente.")
    else:
        print("Cliente no encontrado.")

def eliminar_cliente_json(cedula_buscar):
    # Cargar los clientes desde el archivo JSON
    clientes_data = cargar_clientes_json()
    
    # Buscar el cliente por su cédula
    cliente_encontrado = None
    for cliente in clientes_data:
        if cliente["cedula"] == cedula_buscar:
            cliente_encontrado = cliente
            break
    
    if cliente_encontrado:
        # Eliminar el cliente de la lista
        clientes_data.remove(cliente_encontrado)
        
        # Guardar los datos actualizados en el archivo JSON
        with open("clientes.json", "w") as file:
            json.dump(clientes_data, file, indent=4)
        
        print(f"Cliente con cédula {cedula_buscar} eliminado correctamente.")
    else:
        print("Cliente no encontrado.")

def buscar_cliente_por_cedula(cedula_buscar):
    # Cargar los clientes desde el archivo JSON
    clientes_data = cargar_clientes_json()
    
    # Buscar el cliente por su cédula o RIF
    cliente_encontrado = None
    for cliente in clientes_data:
        if cliente["cedula"] == cedula_buscar:
            cliente_encontrado = cliente
            break
    
    if cliente_encontrado:
        # Si el cliente es encontrado, mostrar los datos
        print("Cliente encontrado:")
        print(cliente_encontrado)
    else:
        print(f"Cliente con cédula/RIF {cedula_buscar} no encontrado.")

def buscar_cliente_por_correo(correo_buscar):
    # Cargar los clientes desde el archivo JSON
    clientes_data = cargar_clientes_json()
    
    # Buscar el cliente por su correo electrónico
    cliente_encontrado = None
    for cliente in clientes_data:
        if cliente["correo"] == correo_buscar:
            cliente_encontrado = cliente
            break
    
    if cliente_encontrado:
        # Si el cliente es encontrado, mostrar los datos
        print("Cliente encontrado:")
        print(cliente_encontrado)
    else:
        print(f"Cliente con correo {correo_buscar} no encontrado.")

def main():

    productos = []
    productos_objeto = []
    requests_productos = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json')
    contenido_productos = requests_productos.content
    info_equipos = open('productos.json','wb')
    info_equipos.write(contenido_productos)
    info_equipos.close()
    clientes = []
    clientes = []
    clientes_objeto =[]

    # utf-8 para que se muestren los nombres con los acentos bien 
    with open('productos.json', 'r', encoding='utf-8') as archivo_productos:
        datos_productos = json.load(archivo_productos)
        for i in range(len(datos_productos)):
            id_producto = datos_productos[i]["id"] 
            name = datos_productos[i]["name"]
            description = datos_productos[i]["description"]
            price = datos_productos[i]["price"]
            category = datos_productos[i]["category"]
            inventory = datos_productos[i]["inventory"]
            compatible_vehicles = datos_productos[i]["compatible_vehicles"]
            print(f"ID: {id_producto}, Nombre: {name}")
            # Asegúrate de que la función crearProducto esté definida y de que los parámetros sean correctos
            crearProducto(id_producto, name, description, price, category, inventory, compatible_vehicles, productos_objeto, productos)  

    print("Bienvenido a la tienda en línea de productos para vehículos 🚗")
    while True: 
        gestion = input ("""Ingrese la gestión a la que desea acceder
        [1] » Gestión de productos
        [2] » Gestión de ventas
        [3] » Gestión de clientes        
        [4] » Gestión de pagos
        [5] » Gestión de envíos
        [6] » Indicadores de gestión
        [7] » Salir
        """)
        if gestion == "1":
            opcion = input ("""Ingrese la opcion
            [1] » Agregar Producto
            [2] » Buscar Producto
            [3] » Modificar Información        
            [4] » Eliminar Producto               
            [5] » Salir
            """)
            if opcion == "1":
                print ("hola")
                with open('productos.json', 'r', encoding='utf-8') as archivo_productos:
                    datos_productos = json.load(archivo_productos)

                # Verificar si hay productos en el JSON
                if datos_productos:
                    # Obtener el id más alto en la lista de productos
                    ultimo_id = max(producto["id"] for producto in datos_productos)
                    nuevo_id = ultimo_id + 1
                else:
                    # Si la lista está vacía, comenzar con el id 1
                    nuevo_id = 1
                
                id_prod = nuevo_id
                nombre = input ("Ingrese el nombre del producto")
                descripcion = input("Ingrese la descripción del producto")
                precio = input ("Ingrese el precio del producto") 
                categoria = input("Ingrese la categoria: aceites, filtros, empacaduras, tren delantero,rodamientos, motor, grasas, gomas, etc")
                inventario = input("Ingrese el inventario")
                modelo_vehiculo = input("Ingrese el modelo del vehiculo")
                producto = Producto(id_prod, nombre,descripcion,precio,categoria,inventario,modelo_vehiculo)
                productos.append(producto.mostrar_producto())
                print(productos)

                # Guardar la lista de productos actualizada en el archivo JSON
                # Crear el diccionario del nuevo producto
                producto = {
                    "id": id_prod,
                    "nombre": nombre,
                    "descripcion": descripcion,
                    "precio": precio,
                    "categoria": categoria,
                    "inventario": inventario,
                    "modelo_vehiculo": modelo_vehiculo
                }

                # Agregar el nuevo producto a la lista de datos_productos
                datos_productos.append(producto)

                # Guardar la lista de productos actualizada en el archivo JSON
                # el parámetro ensure_ascii es un argumento de la función json.dump() o json.dumps() que controla cómo se manejan los caracteres no ASCII (como caracteres especiales, acentos, letras en otros alfabetos, etc.) al guardar datos en formato JSON.
                with open('productos.json', 'w', encoding='utf-8') as archivo_productos:
                    json.dump(datos_productos, archivo_productos, ensure_ascii=False, indent=2)

                print("Producto agregado con éxito.")
            elif opcion == "2":
                criterio = input("""Seleccione el criterio de búsqueda:
                [1] » Categoría
                [2] » Precio
                [3] » Nombre
                [4] » Disponibilidad en inventario
                """)
                if criterio == "1":
                    buscarProductosPorCategoria(productos_objeto)
                elif criterio == "2":
                    buscarProductosPorPrecio(productos_objeto)
                elif criterio == "3":
                    buscarProductosPorNombre(productos_objeto)
                elif criterio =="4":
                    buscarProductosPorDisponibilidad(productos_objeto)
                else: 
                    break
            elif opcion == "3":
                print ("Modificar información de productos existentes")
                # Solicitar al usuario el ID del producto que desea modificar
                id_producto = int(input("Ingrese el ID del producto que desea modificar: "))
                modificarProducto(id_producto, productos_objeto, productos)
            elif opcion == "4":
                id_a_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
                eliminarProducto(id_a_eliminar, productos_objeto, productos)
            else: 
                break     
        elif gestion == "2":
            print (2)
        elif gestion == "3":
            opt = input("""Ingrese la opcion
            [1] » Registrar cliente
            [2] » Modificar cliente
            [3] » Eliminar cliente       
            [4] » Busqueda clientes              
            [5] » Salir
            """)
            if opt =="1":
                nombre_apellido = input ("Ingrese el Nombre y Apellido o Razón Social")
                cedula = input ("Ingrese el numero de cedula")
                correo = input ("Ingrese su correo electronico")
                direccion = input ("Ingrese su dirección de envio")
                telefono = input ("Ingrese su telefono")
                es_juridico = input ("Es cliente jurídico: (1)-Si (2)-No")
                if es_juridico == "Si":
                    print("Es persona jurídica")
                    nombre_contacto = input("Ingrese el nombre de la persona de contacto")
                    telefono_contacto = input("Ingrese el telefono de la persona de contacto")
                    correo_contacto = input("Ingrese el correo de la persona de contacto")
                    cliente_juridico = ClienteJuridico(nombre_apellido,cedula,correo,direccion,telefono,nombre_contacto,telefono_contacto,correo_contacto)
                    clientes.append(cliente_juridico)
                    print (cliente_juridico.mostrarCliente())
                    agregar_cliente_json(cliente_juridico)
                else: 
                    cliente = Cliente(nombre_apellido,cedula,correo,direccion,telefono)
                    clientes.append(cliente)
                    print (cliente.mostrarCliente())
                    agregar_cliente_json(cliente)
            elif opt == "2":
               cedula_buscar = input("Ingrese el número de cédula del cliente a modificar: ")
               modificar_cliente_json(cedula_buscar)
            elif opt == "3":
                cedula_a_eliminar = input("Ingrese la cédula del cliente a eliminar: ")
                eliminar_cliente_json(cedula_a_eliminar)
            elif opt =="4":
                busq = input ("Ingrese el tipo de busqueda (1)-Rif o Cedula (2)-Correo")
                if busq =="1":
                    cedula_a_buscar = input("Ingrese la cédula o RIF del cliente a buscar: ")
                    buscar_cliente_por_cedula(cedula_a_buscar)  
                elif busq =="2":
                    correo_a_buscar = input("Ingrese el correo electrónico del cliente a buscar: ")
                    buscar_cliente_por_correo(correo_a_buscar)
        elif gestion == "4":
            print (2)
        elif gestion == "5":
            print (5)
        else:
            break
main()