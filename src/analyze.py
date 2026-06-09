import json
import csv

from src.client import Client
from src.sale import Sale
from src.client_collection import ClientCollection
from src.sales_collection import SalesCollection

def cargar_clientes():
    with open("data/clients.json", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return [Client(d["client_id"], d["name"], d["country"], d["signup_date"]) for d in datos]

def cargar_ventas():
    ventas = []
    with open("data/sales.csv", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            ventas.append(Sale(
                fila["sale_id"],
                int(fila["client_id"]),
                fila["product"],
                fila["category"],
                float(fila["amount"]),
                fila["date"]
            ))
    return ventas

def generate_report():
    clientes = cargar_clientes()
    ventas = cargar_ventas()
    coleccion_ventas = SalesCollection(ventas)

    lista_clientes = []
    for cliente in clientes:
        total_gastado = coleccion_ventas.total_amount_by_client(cliente.client_id)
        num_ventas = len(coleccion_ventas.sales_by_client(cliente.client_id))
        promedio = coleccion_ventas.average_amount_by_client(cliente.client_id)

        lista_clientes.append({
            "client_id": cliente.client_id,
            "name": cliente.name,
            "total_spent": round(total_gastado, 2),
            "sale_count": num_ventas,
            "average_sale": promedio
        })

    ingreso_total = sum(v.amount for v in ventas)

    return {
        "summary": {
            "total_clients": len(clientes),
            "total_sales": len(ventas),
            "total_revenue": round(ingreso_total, 2)
        },
        "clients": lista_clientes
    }
