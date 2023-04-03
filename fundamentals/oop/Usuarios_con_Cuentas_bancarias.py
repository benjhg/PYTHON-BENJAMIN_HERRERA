class CuentaBancaria:
    def __init__(self, num_de_cuenta,name, tasa_interes=0.01,balance=0,):
        self.tasa_interes = tasa_interes
        self.balance = balance
        self.name = name
        self.numero_cuenta = num_de_cuenta
        
    def numero_cuenta(self):
        print([])       

    def deposito(self, amount):
        self.balance += amount
        print(f"Se han depositado {amount} pesos a {self.name} Su saldo actual es {self.balance} pesos.")
        return self

    def retiro(self, amount):
        if amount > self.balance:
            self.balance -=5
            print("Fondos insuficientes. No se puede realizar la transacción.")
            return self
        else:
            self.balance -= amount
            self.balance -=5
            print(f"Se han retirado {amount} pesos. Su saldo actual es {self.balance} pesos.")
            return self
    
    def mostrar_info_cuenta(self):
        print(f"Tasa de interes: {self.tasa_interes}")
        print(f"Saldo actual: {self.balance} pesos.")
        return self

    def generar_interes(self):
        interes_generado = self.balance * self.tasa_interes
        self.balance += interes_generado
        print(f"Se ha generado {interes_generado} pesos de interes. Su saldo actual es {self.balance} pesos.")
        return self

    def mostrar_todas_las_instancias(self):
        interes_generado = self.balance * self.tasa_interes
        print(f"{self.name} Tu saldo actual: {self.balance} pesos.")
        print(f"{self.name} Tu tasa de interes: {self.tasa_interes}")
        print(f"{self.name} Tu interes generado: {interes_generado}")
class Usuario:
    def __init__(self, nombre, email, cuenta):
        self.nombre = nombre
        self.emeil = email
        cuenta = CuentaBancaria("tasa_interes,balance")




juan = CuentaBancaria( 1234,"Juan",)
isa = CuentaBancaria(123,"isa",)
pedro = CuentaBancaria(321,"Pedro",)
'''
pedro.deposito(1000).deposito(2000).deposito(2000).retiro(500).generar_interes()
juan.deposito(1000).deposito(2000).retiro(100).retiro(400).retiro(300).retiro(200).generar_interes().mostrar_info_cuenta()

juan.mostrar_todas_las_instancias()
pedro.mostrar_todas_las_instancias()
'''
juan.numero_cuenta()