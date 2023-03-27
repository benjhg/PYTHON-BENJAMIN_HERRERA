class Usuario:
    # declarando un atributo de clase
    nombre_banco = "Primer Dojo Nacional"		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 100000
        def hacer_retiro(self, amount):
            self.balance_cuenta -= amount
guido = Usuario()
monty = Usuario()
guido.nombre_banco = "Dojo Credit Union"
monty.hacer_retiro(2002)
print(guido.bank_name) # salida: Dojo Credit Union 
print(monty.bank_name) 
