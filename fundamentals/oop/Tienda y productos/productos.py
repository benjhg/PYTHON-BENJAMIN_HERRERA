

class producto():
    def __init__(self, nombre, precio, categoria, id):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.id = id
        
    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado:
            self.precio += self.precio * cambio_porcentaje / 100
        else:
            self.precio -= self.precio * cambio_porcentaje / 100    

    def Print_info(self):
        print(f"{self.nombre}, Categoria:{self.categoria}, Precio:{self.precio}")






