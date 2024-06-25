class Personagem:
    def __init__(self):
        self.atributos = {
            "sanidade": 0,
            'força': 0,
            'inteligencia': 0,
            'destreza': 0,
            'resistencia': 0,
            'sabedoria': 0,
            'Carisma': 0,
            'reflexo': 0
        }
    def aumentar_atributo(self, atributo, pontos=1):
        if atributo in self.atributos:
            self.atributos[atributo] += pontos

    def diminuir_atributo(self, atributo, pontos=1):
        if atributo in self.atributos:
            self.atributos[atributo] -= pontos
            if self.atributos[atributo] < 0:
                self.atributos[atributo] = 0

    def mostrar_atributos(self):
        print("Atributos do personagem:")
        for atributo, valor in self.atributos.items():
            print(f"  {atributo.capitalize()}: {valor}")

# area dos jogadores
jogador1 = Personagem()

jogador1.aumentar_atributo("força", 5)
jogador1.diminuir_atributo("força", 6)
jogador1.mostrar_atributos()
