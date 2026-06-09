class ClientCollection:
    # Recibe una lista de objetos Client
    def __init__(self, clients):
        self.clients = clients

    # Devuelve el cliente que tenga ese id, o None si no existe
    def get_client_by_id(self, id_buscado):
        resultado = [c for c in self.clients if c.client_id == id_buscado]
        return resultado[0] if resultado else None

    # Devuelve la lista de clientes de un país concreto
    def clients_by_country(self, pais):
        return [c for c in self.clients if c.country == pais]
