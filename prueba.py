import requests

requests_productos = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json')
contenido_productos = requests_productos.content
info_equipos = open('productos.json','wb')
info_equipos.write(contenido_productos)
info_equipos.close()