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

    def aumentar_atributo(self, atributo):
        if atributo in self.atributos:
            self.atributos[atributo] += 1

    def mostrar_atributos(self):
        for atributo, valor in self.atributos.items():
            print(f"{atributo}: {valor}")
# area dos jogadores
jogador1 = Personagem()



for atributo in jogador1.atributos:
    jogador1.aumentar_atributo(atributo)


tributo = 'Carisma'
valor_desejado = 12
while True:
    jogador1.aumentar_atributo(atributo)
    if jogador1.atributos[atributo] >= valor_desejado:
        break

jogador1.mostrar_atributos()
