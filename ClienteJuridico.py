from Cliente import Cliente

class ClienteJuridico(Cliente):
    def __init__(self, nombre_apellido, cedula, correo, direccion, telefono,nombre_contacto, telefono_contacto,correo_contacto   ):
        super().__init__(nombre_apellido, cedula, correo, direccion, telefono)
        self.nombre_contacto = nombre_contacto
        self.telefono_contacto = telefono_contacto
        self.correo_contacto = correo_contacto

    def mostrarCliente(self):
        infobasic = super().mostrarCliente() 
        info_contacto = (f"\nNombre de Contacto: {self.contacto_nombre}\n"
                         f"Teléfono de Contacto: {self.contacto_telefono}\n"
                         f"Correo de Contacto: {self.contacto_correo}")
        return infobasic + info_contacto  