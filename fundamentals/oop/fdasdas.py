class Usuario:
    def __init__(self, nombre, saldo_inicial):
        self.nombre = nombre
        self.balance = 0

    def hacer_retiro(self, amount):
        if amount > self.balance:
            print("Error: no hay suficiente saldo en la cuenta")
        else:
            self.balance -= amount
            print("Retiro exitoso. Saldo restante:", self.balance)
 
    def hacer_deposito(self, amount):
        self.balance += amount
        print("Depósito exitoso. Saldo actual:", self.balance)                    

juan = Usuario("Juan", 0)
benjamin = Usuario("benjamin", 999999)

juan.hacer_deposito(10)
juan.hacer_retiro(500)