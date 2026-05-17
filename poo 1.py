class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 

    def saludar(self):
     print(f"hola soy {self.nombre} tengo {self.edad} años")

persona1 = persona("alfredo",20)
persona2 = persona("luis",30)

persona1.saludar()
persona2.saludar()