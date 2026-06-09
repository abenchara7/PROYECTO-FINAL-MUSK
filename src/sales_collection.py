class SalesCollection:

    def __init__(self, sales):
        self.sales = sales

    
    def sales_by_client(self, id_cliente):
        return [s for s in self.sales if s.client_id == id_cliente]

    
    def total_amount_by_client(self, id_cliente):
        ventas_del_cliente = self.sales_by_client(id_cliente)
        return sum(s.amount for s in ventas_del_cliente)

    
    def average_amount_by_client(self, id_cliente):
        ventas_del_cliente = self.sales_by_client(id_cliente)
        if len(ventas_del_cliente) == 0:
            return 0
        return round(self.total_amount_by_client(id_cliente) / len(ventas_del_cliente), 2)
