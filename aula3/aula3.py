
'''
Você deverá criar uma classe Lampada com os métodos ligar e desligar.
Crie também um algoritmo onde o usuário possa ligar e desligar essa lâmpada inúmeras vezes.
'''

class Lampada:
    def __init__(self):
        self.estado = False  # False = desligada, True = ligada
    
    def ligar(self):
        self.estado = True
        print("A lâmpada foi ligada.")
    
    def desligar(self):
        self.estado = False
        print("A lâmpada foi desligada.")
    
    def verificar_estado(self):
        if self.estado:
            return "Ligada"
        else:
            return "Desligada"




