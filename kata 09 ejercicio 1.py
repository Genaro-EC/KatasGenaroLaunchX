def reporte(tanque_1, tanque_2, tanque_3):
    calculo = (tanque_1 + tanque_2 + tanque_3) / 3
    return f"""Reporte de gasolina:
    Promedio: {calculo}%
    Tanque 1: {tanque_1}%
    Tanque 2: {tanque_2}%
    Tanque 3: {tanque_3}% 
    """
print(reporte(45, 55, 65))

def promedio (valor):
    total = sum(valor)
    num_valor = len(valor)
    return total / num_valor

promedio ([95, 75, 99]) 

def generar_reporte(tanque_1, tanque_2, tanque_3):
    return f"""Fuel Report:
    promedio total: {promedio([tanque_1, tanque_2, tanque_3])}%
    Tanque 1: {tanque_1}%
    Tanque 2: {tanque_2}%
    Tanque 3: {tanque_3}% 
    """

print(generar_reporte (100, 100, 100))