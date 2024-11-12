class Producto():
    def __init__(self,id,name,description,price,category,inventory,compatible_vehicles):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.inventory = inventory
        self.compatible_vehicles = compatible_vehicles
    
    def mostrar_producto(self):
        return (f"Id:{self.id}, Nombre:{self.name}, Description:{self.description}, Price:{self.price}")