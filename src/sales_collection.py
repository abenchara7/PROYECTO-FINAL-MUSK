class SalesCollection:
    # Recibe una lista de objetos Sale
    def __init__(self, sales):
        self.sales = sales

    # Devuelve todas las ventas de un cliente concreto
    def sales_by_client(self, id_cliente):
        return [s for s in self.sales if s.client_id == id_cliente]

    # Suma el total gastado por un cliente
    def total_amount_by_client(self, id_cliente):
        ventas_del_cliente = self.sales_by_client(id_cliente)
        return sum(s.amount for s in ventas_del_cliente)

    # Calcula el gasto medio por compra de un cliente
    def average_amount_by_client(self, id_cliente):
        ventas_del_cliente = self.sales_by_client(id_cliente)
        if len(ventas_del_cliente) == 0:
            return 0
        return round(self.total_amount_by_client(id_cliente) / len(ventas_del_cliente), 2)
