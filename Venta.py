class Venta():
    def __init__(self, ced, productos_comprados, metodo_pago, metodo_envio, total, fecha_venta):
        self.ced = ced
        self.productos_comprados = productos_comprados
        self.metodo_pago = metodo_pago
        self.metodo_envio = metodo_envio
        self.total = total
        self.fecha_venta = fecha_venta
    
    def mostrarVenta(self):
        return self.total, self.metodo_pago, self.metodo_envio