class Pago():
    def __init__(self,num_cedula, tipo_pago, moneda_pago, fecha_pago):
        self.num_cedula = num_cedula
        self.tipo_pago = tipo_pago
        self.moneda_pago = moneda_pago
        self.fecha_pago = fecha_pago

    def MostrarPago(self):
        return self.num_cedula, self.fecha_pago