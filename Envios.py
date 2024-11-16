class Envios():
    def __init__(self, num_cedula, orden_compra, metodo_envio, datos_motorizado, fecha_envio):
        self.num_cedula = num_cedula
        self.orden_compra = orden_compra
        self.metodo_envio = metodo_envio
        self.datos_motorizado = datos_motorizado
        self.fecha_envio = fecha_envio
    
    def mostrarEnvio(self):
        return self.num_cedula, self.orden_compra, self.metodo_envio, self.datos_motorizado