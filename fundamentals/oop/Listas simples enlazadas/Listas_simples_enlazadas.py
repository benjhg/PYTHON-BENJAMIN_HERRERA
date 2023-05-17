'''class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node	# FIJA el encabezado de la lista AL nodo que creamos en el último paso
        return self	# return self para permitir el encadenamiento
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next 	# establece runner a su vecino
        return self# una vez terminado el ciclo, devuelve self para permitir el encadenamiento
    def add_to_back(self, val):
        if self.head == None:	# si la lista está vacía
            self.add_to_front(val)	# ejecuta el método add_to_front
            return self	# asegurémonos de que el resto de esta función no suceda si agregamos al comienzo
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node	# incrementa runner al siguiente nodo de la lista
        return self # return self para permitir el encadenamiento

    def remove_from_front(self):
        if self.head is None:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        return removed_value

    def remove_from_back(self):
        if self.head is None:
            return None
        if self.head.next is None:
            removed_value = self.head.value
            self.head = None
            return removed_value
        runner = self.head
        while runner.next.next is not None:
            runner = runner.next
        removed_value = runner.next.value
        runner.next = None
        return removed_value

    def remove_val(self, val):
        if self.head is None:
            return False
        if self.head.value == val:
            self.head = self.head.next
            return True
        runner = self.head
        while runner.next is not None:
            if runner.next.value == val:
                runner.next = runner.next.next
                return True
            runner = runner.next
        return False

    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        for _ in range(n - 1):
            if runner is None:
                return None
            runner = runner.next
        if runner is None:
            return None
        new_node.next = runner.next
        runner.next = new_node
        return self



my_list = SList()
my_list.add_to_front(3).add_to_front(2).add_to_front(1)
my_list.print_values() # Debería imprimir: 1 2 3

removed_value = my_list.remove_from_front()
print(f"Removed value: {removed_value}") # Debería imprimir: "Removed value: 1"
my_list.print_values() # Debería imprimir: 2 3

removed_value = my_list.remove_from_back()
print(f"Removed value: {removed_value}") # Debería imprimir: "Removed value: 3"
my_list.print_values() # Debería imprimir: 2

my_list.remove_val(2)
my_list.print_values() # Debería imprimir nada (la lista está vacía)

my_list.add_to_front(3).add_to_front(2).add_to_front(1)
my_list.insert_at(0, 0) # insertar al principio
my_list.insert_at(4, 4) # insertar al final
my_list.insert_at(2.5, 3) # insertar en el medio
my_list.print_values() # Debería imprimir: 0 1 2 2.5 3 4'''

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        if not self.head:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        return removed_value

    def remove_from_back(self):
        if not self.head:
            return None
        if not self.head.next:
            removed_value = self.head.value
            self.head = None
            return removed_value
        runner = self.head
        while runner.next.next:
            runner = runner.next
        removed_value = runner.next.value
        runner.next = None
        return removed_value

    def remove_val(self, val):
        if not self.head:
            return False
        if self.head.value == val:
            self.head = self.head.next
            return True
        runner = self.head
        while runner.next:
            if runner.next.value == val:
                runner.next = runner.next.next
                return True
            runner = runner.next
        return False

    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        for _ in range(n - 1):
            if not runner:
                return None
            runner = runner.next
        if not runner:
            return None
        new_node.next = runner.next
        runner.next = new_node
        return self
    

my_list = SList()
my_list.add_to_front(3).add_to_front(2).add_to_front(1)
my_list.print_values() # Debería imprimir: 1 2 3

removed_value = my_list.remove_from_front()
print(f"Removed value: {removed_value}") # Debería imprimir: "Removed value: 1"
my_list.print_values() # Debería imprimir: 2 3

removed_value = my_list.remove_from_back()
print(f"Removed value: {removed_value}") # Debería imprimir: "Removed value: 3"
my_list.print_values() # Debería imprimir: 2

my_list.remove_val(2)
my_list.print_values() # Debería imprimir nada (la lista está vacía)

my_list.add_to_front(3).add_to_front(2).add_to_front(1)
my_list.insert_at(0, 0) # insertar al principio
my_list.insert_at(4, 4) # insertar al final
my_list.insert_at(2.5, 3) # insertar en el medio
my_list.print_values() # Debería imprimir: 0 1 2 2.5 3 4
