class CuentaBancaria:
    def __init__(self, num_cuenta, nombre_cuenta, balance) :
        self.num_cuenta = num_cuenta
        self.nombre_cuenta = nombre_cuenta
        self.balance = balance
    
    def generar_balance(self):
        print(self.balance)
    
    def generar_nombre(self):
        print(self.nombre_cuenta)

    def depositar(self, monto):
        if monto>0:
            self.balance += monto
    
mi_cuenta= CuentaBancaria("102-203-405", "Juan Andres", 1023)
mi_cuenta.generar_nombre() 
mi_cuenta.generar_balance()
        
