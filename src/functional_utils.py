from functools import reduce

def filtrar_por_categoria(ventas, categoria):
    return list(filter(lambda v: v.category == categoria, ventas))

def filtrar_por_fecha(ventas, fecha_inicio, fecha_fin):
    return list(filter(lambda v: fecha_inicio <= v.date <= fecha_fin, ventas))

def obtener_importes(ventas):
    return list(map(lambda v: v.amount, ventas))

def sumar_importes(ventas):
    importes = obtener_importes(ventas)
    return reduce(lambda acum, importe: acum + importe, importes, 0)
