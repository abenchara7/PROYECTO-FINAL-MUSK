class Sale:
    # Constructor: recibe los 6 datos de la venta
    def __init__(self, sale_id, client_id, product, category, amount, date):
        self.sale_id = sale_id
        self.client_id = client_id
        self.product = product
        self.category = category
        self.amount = amount
        self.date = date

    # Convierte el objeto a diccionario (útil para el reporte final)
    def to_dict(self):
        return {
            "sale_id": self.sale_id,
            "client_id": self.client_id,
            "product": self.product,
            "category": self.category,
            "amount": self.amount,
            "date": self.date
        }
