class Electrodomestico:
    def __init__(self, precio_base, color, consumo_energetico, peso):
        self.precio_base = precio_base
        self.color = self.comprobarColor(color)
        self.consumo_energetico = self.comprobarConsumoEnergetico(consumo_energetico)
        self.peso = peso
    
    def comprobarConsumoEnergetico(self, letra):
        letras_validas = ['A', 'B', 'C', 'D', 'E', 'F']
        if letra.upper() in letras_validas:
            return letra.upper()
        else:
            return 'A'  
    
    def comprobarColor(self, color):
        colores_validos = ['blanco', 'negro', 'rojo', 'azul']
        if color.lower() in colores_validos:
            return color.lower()
        else:
            return 'blanco'  



