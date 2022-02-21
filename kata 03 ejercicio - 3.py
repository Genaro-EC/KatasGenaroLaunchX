# kata 3 ejercicio 3: advertencia de asteroide
veloaster = input("¿Qué velocidad (km/s) tiene el asteroide? ")
tamaaster = input ("¿Qué tamaño tiene el asteroide? ")
velmax = 25
tammax = 40
# comparativa
if int (veloaster) > velmax and int (tamaaster) > tammax :
    print ("HOLA DIOS, SOY YO DE NUEVO")
elif int (veloaster) >= 20 :
    print ("LOCALICEN EL ASTEROIDE EN EL CIELO")
elif int (tamaaster) < tammax :
    print ("VAMO A CALMARNO")
else :
    print ("VAMO A CALMARNO")