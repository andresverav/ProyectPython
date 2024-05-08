numero1 = int(input("Ingrese valor 1:"))
numero2 = int(input("Ingrese valor 2:"))

try:
    resultado = numero1 / numero2
    print("Resultado", resultado)
except ZeroDivisionError as e:
    print("Error ZeroDivisionError:", e)
except :
    print("Error:")
    
    