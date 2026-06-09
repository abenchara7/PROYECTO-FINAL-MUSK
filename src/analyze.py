import json
import csv
import pandas as pd

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

    # Cálculos avanzados con Pandas
    df_ventas = pd.DataFrame([v.to_dict() for v in ventas])
    df_clientes = pd.DataFrame([c.to_dict() for c in clientes])
    df_combinado = df_ventas.merge(df_clientes, on="client_id")

    # Cálculo 6: cliente con mayor gasto por país
    gasto_por_pais = df_combinado.groupby(["country", "name"])["amount"].sum().reset_index()
    indices_max = gasto_por_pais.groupby("country")["amount"].idxmax()
    top_por_pais = gasto_por_pais.loc[indices_max]
    top_cliente_por_pais = dict(zip(top_por_pais["country"], top_por_pais["name"]))

    # Cálculo 7: total por categoría
    ventas_por_categoria = df_ventas.groupby("category")["amount"].sum()
    total_por_categoria = {cat: round(float(total), 2) for cat, total in ventas_por_categoria.items()}

    # Cálculo 9: clientes que superan 500 de gasto total
    clientes_alto_gasto = [c["name"] for c in lista_clientes if c["total_spent"] > 500]

    # Cálculo 10: ventas acumuladas por mes
    df_ventas["date"] = pd.to_datetime(df_ventas["date"])
    ventas_por_mes = df_ventas.groupby(df_ventas["date"].dt.to_period("M"))["amount"].sum()
    ventas_mensuales = {str(mes): round(float(total), 2) for mes, total in ventas_por_mes.items()}

    return {
        "summary": {
            "total_clients": len(clientes),
            "total_sales": len(ventas),
            "total_revenue": round(ingreso_total, 2)
        },
        "clients": lista_clientes,
        "top_client_by_country": top_cliente_por_pais,
        "sales_by_category": total_por_categoria,
        "high_spending_clients": clientes_alto_gasto,
        "monthly_sales": ventas_mensuales
    }

if __name__ == "__main__":
    import json as _json
    reporte = generate_report()
    with open("final_report.json", "w", encoding="utf-8") as archivo:
        _json.dump(reporte, archivo, indent=4, ensure_ascii=False)
