class Cliente():
    def __init__(self, nombre_apellido, cedula, correo, direccion, telefono):
        self.nombre_apellido = nombre_apellido
        self.cedula = cedula
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
    
    def mostrarCliente(self):
        return (f"Nombre: {self.nombre_apellido}")
    