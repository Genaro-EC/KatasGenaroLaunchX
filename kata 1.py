from datetime import date
print("Today's date is: " + str (date.today()))

print ("Convertidor de unidades")
parsec = input("Introduzca los parsec: ")
lightyears = 3.26156
conversion= int(parsec) * int(lightyears)
print(str(parsec) + " parsec, is " + str(conversion) + " lightyears")