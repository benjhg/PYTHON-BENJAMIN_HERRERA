class CuentaBancaria:
    def __init__(self, tasa_interes=0.01, balance=0):
        self.tasa_interes = tasa_interes
        self.balance = balance
    
    def deposito(self, amount):
        self.balance += amount
        print(f"Se han depositado {amount} pesos. Su saldo actual es {self.balance} pesos.")
    
    def retiro(self, amount):
        if amount > self.balance:
            print("Fondos insuficientes. No se puede realizar la transacción.")
        else:
            self.balance -= amount
            print(f"Se han retirado {amount} pesos. Su saldo actual es {self.balance} pesos.")
    
    def mostrar_info_cuenta(self):
        print(f"Tasa de interés: {self.tasa_interes}")
        print(f"Saldo actual: {self.balance} pesos.")
    
    def generar_interes(self):
        interes_generado = self.balance * self.tasa_interes
        self.balance += interes_generado
        print(f"Se ha generado {interes_generado} pesos de interés. Su saldo actual es {self.balance} pesos.")

