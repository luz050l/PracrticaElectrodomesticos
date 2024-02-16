

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
        if self.Color==rojo:
            print("color Correcta.upper")
        elif self.Color==azul:
            print("color Correcta.upper")
        elif self.Color==blanco:
            print("color Correcta.upper")
        elif self.Color==negro:
            print("color Correcta.upper")
        else:
            return self.Color (blanco)
        print("blanco")

    def precio(self):
