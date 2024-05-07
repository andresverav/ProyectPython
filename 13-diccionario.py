#Diccionarios
edades={"Andres":45, "Debo":44, "Seba":20, "Samanta":14}
print(edades.get("Samanta"))

#Agregar clave
edades["Samuel"]=8
print(edades)

#Actualiza
edades["Andres"]=25
print(edades)

#Elimina
del edades["Andres"]
print(edades)

