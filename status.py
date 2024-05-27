class Personagem:
    def __init__(self):
        self.atributos = {
            'Agilidade': 15,
            'Inteligência': 12,
            'Sabedoria': 14,
            'Destreza': 18,
            'Constituição': 10,
            'Carisma': 8,
            'Percepção': 16
        }

    def aumentar_atributo(self, atributo):
        if atributo in self.atributos:
            self.atributos[atributo] += 1

    def diminuir_atributo(self, atributo):
        if atributo in self.atributos and self.atributos[atributo] > 0:
            self.atributos[atributo] -= 1

    def mostrar_atributos(self):
        for atributo, valor in self.atributos.items():
            print(f"{atributo}: {valor}")

meu_personagem = Personagem()

for atributo in meu_personagem.atributos:
    meu_personagem.aumentar_atributo(atributo)

while meu_personagem.atributos['Agilidade'] > 10:
    meu_personagem.diminuir_atributo('Agilidade')


while meu_personagem.atributos['Inteligência'] > 10:
    meu_personagem.diminuir_atributo('Inteligência')


atributo = 'Carisma'
valor_desejado = 12
while True:
    meu_personagem.aumentar_atributo(atributo)
    if meu_personagem.atributos[atributo] >= valor_desejado:
        break

meu_personagem.mostrar_atributos()
