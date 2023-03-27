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

    def mostrar_balance(self):
        print("tu saldo es", self.balance)

    def hacer_deposito(self, amount):
        self.balance += amount
        print("Depósito exitoso. Saldo actual:", self.balance)     

    def tranferencia(self, amount,user):
        if amount > self.balance:
            print("Error: no hay suficiente saldo en la cuenta")
        else:
            self.balance -= self.balance
            user.balance += self.balance
            print("tu deposito fue exitoso y tu saldo quedo en", )
            print


juan = Usuario("Juan", 0)
benjamin = Usuario("benjamin", 999999)

juan.hacer_deposito(10)
juan.hacer_retiro(0)
juan.hacer_deposito(100)
juan.mostrar_balance()
juan.tranferencia(110,benjamin)