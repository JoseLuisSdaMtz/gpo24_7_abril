class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
        
    def area(self):
        return self.lado**2
##################################################################

lado= int(input("ingresa el lado: "))
cuadrado1 = Cuadrado(lado)
r=cuadrado1.area()

print(f"codigo tedioso... el area es: {r}")
