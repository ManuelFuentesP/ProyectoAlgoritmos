class Venta():
    def __init__(self, ced, productos_comprados, metodo_pago, metodo_envio, total, fecha_venta, pago):
        self.ced = ced
        self.productos_comprados = productos_comprados
        self.metodo_pago = metodo_pago
        self.metodo_envio = metodo_envio
        self.total = total
        self.fecha_venta = fecha_venta
        self.pago = pago
    
    def mostrarVenta(self):
        return self.ced, self.productos_comprados, self.total, self.metodo_pago, self.metodo_envio, self.pago