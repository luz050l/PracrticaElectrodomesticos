A=100
B=80
C=60
D=50
E=30
F=10

# TENGO ENTENDIDO QUE DEPENDIENDO DE LA LETRA QUE ESCOJAN, VA A TENER SUS PRECIOS Y A ESTO SE LE DEBE SUMAR EL PRECIO DE SU TAMAÑO (SUMA DE LETRA+TAMAÑO)

class Electrodomestico:
    def __init__(self,Precio,Color,Peso,Consumo,letra_upper):
        self.Precio= Precio
        self.Color= Color           
        self.Consumo= Consumo
        self.Peso= Peso 
        self.letra_upper= letra_upper

    def letras_upper(self,A,B,C,D,E,F):
        if self.letra_upper==A:
            print("Letra Correcta.upper"+4)
        elif self.letra_upper==B:
            print("Letra Correcta.upper"+B)
        elif self.letra_upper==C:
            print("Letra Correcta.upper"+C)
        elif self.letra_upper==D:
            print("Letra Correcta.upper"+D)
        elif self.letra_upper==E:
            print("Letra Correcta.upper"+E)
        elif self.letra_upper==F:
            print("Letra Correcta.upper"+F)
        else:
            return self.letra_upper (A)
        print("A")

    def Color(self,rojo,azul,blanco,negro):
        if self.Color==A:
            print("Letra Correcta.upper"+4)
        elif self.Color==B:
            print("Letra Correcta.upper"+B)
        elif self.Color==C:
            print("Letra Correcta.upper"+C)
        elif self.Color==D:
            print("Letra Correcta.upper"+D)
        elif self.Color==E:
            print("Letra Correcta.upper"+E)
        elif self.Color==F:
            print("Letra Correcta.upper"+F)
        else:
            return self.letra_upper (A)
        print("A")
#ESTO ES LO QUE AGREGUE!!!!1
   def precio(self):
        if 0 and 19==10:
            print("operacion")
        elif 20 and 49==50:
            print("2 operacion")
        elif 50 and 79==80:
            print("3 operacion")
        elif 80 and 100000000000000000000==100:
            print("4 operacion")
