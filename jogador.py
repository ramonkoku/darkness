class Jogador:
    def __init__(self, nome, andar, nivel, hp, mana, forca, inteligencia, destreza, resistencia, sabedoria, carisma, reflexo):
        self.nome = nome
        self.andar = andar
        self.nivel = nivel
        self.hp = hp
        self.mana = mana
        self.forca = forca
        self.inteligencia = inteligencia
        self.destreza = destreza
        self.resistencia = resistencia
        self.sabedoria = sabedoria
        self.carisma = carisma
        self.reflexo = reflexo

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Andar: {self.andar}")
        print(f"Nível: {self.nivel}")
        print(f"HP: {self.hp}")
        print(f"Mana: {self.mana}")
        print(f"Força: {self.forca}")
        print(f"Inteligência: {self.inteligencia}")
        print(f"Destreza: {self.destreza}")
        print(f"Defesa: {self.resistencia}")
        print(f"Sabedoria: {self.sabedoria}")
        print(f"Carisma: {self.carisma}")
        print(f"Reflexo: {self.reflexo}")


jogador1 = Jogador("Beatrix", 1, 80, 1700, 3000, 20, 40, 60, 30, 30, 80, 25)
jogador2 = Jogador("Makeda", 6, 100, 1500, 999999, 40, 80, 50, 30, 100, 10, 40)
jogador3 = Jogador("Yzma", 7, 100, 6666, 10000, 60, 60, 70, 50, 70, 35, 50)
jogador4 = Jogador("Marack", 5, 100, 4500, 1000, 80, 70, 75, 50, 70, 60, 80)

def mostrar_informacao(opcao):
    if opcao == 1:
        jogador1.exibir_informacoes()
    elif opcao == 2:
        jogador2.exibir_informacoes()
    elif opcao == 3:
        jogador3.exibir_informacoes()
    elif opcao == 4:
        jogador4.exibir_informacoes()
    else:
        print("Opção inválida. Por favor, escolha entre 1 e 4.")

def main():
    while True:
        try:
            opcao = int(input("Digite seu numero de personagem:"))
            if opcao in [1, 2, 3, 4]:
                mostrar_informacao(opcao)
                break
            else:
                print("Opção inválida. Por favor, escolha entre 1 e 4.")
        except ValueError:
            print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
