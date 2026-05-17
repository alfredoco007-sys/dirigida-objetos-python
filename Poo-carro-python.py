class Auto:
    def __init__(self, marca, color):
        self.marca=marca
        self.color=color
        self.estado=False
    
    def arrancar(self):
        if self.estado:
            print("\nel auto esta encendido")

        else: 
            self.estado = True
            print("\nel auto arranco")

    def acelerar(self):
        if self.estado:
            print("\nel auto acelera")

        else:
            print("\nel auto esta apagado")
    
    def estacionar(self):
        if self.estado:
            print("\nel auto estaciona")
            self.estado = False
        
        else:
            print("esta apagado el auto")

Auto1 = Auto("nissan", "negro")

print(Auto1.marca, Auto1.color)

est=input("el auto esta listo, arrancamos?")

if (est=="s"):
    Auto1.arrancar()


ac=input("quieres acelerar el auto?\n \ns/n")

if ac=="s":
    Auto1.acelerar()
    
est=input("quieres estacionar el carro?\n \ns/n")
if (est=="s"):
        Auto1.estacionar()