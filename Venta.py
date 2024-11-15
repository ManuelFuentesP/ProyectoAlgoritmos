class Venta():
    def __init__(self, ced, productos_comprados, metodo_pago, metodo_envio, total):
        self.ced = ced
        self.productos_comprados = productos_comprados
        self.metodo_pago = metodo_pago
        self.metodo_envio = metodo_envio
        self.total = total
    
    def mostrarVenta(self):
        return self.total