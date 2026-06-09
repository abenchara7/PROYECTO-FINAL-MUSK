class ClientCollection:
    
    def __init__(self, clients):
        self.clients = clients

    
    def get_client_by_id(self, id_buscado):
        resultado = [c for c in self.clients if c.client_id == id_buscado]
        return resultado[0] if resultado else None

    
    def clients_by_country(self, pais):
        return [c for c in self.clients if c.country == pais]
