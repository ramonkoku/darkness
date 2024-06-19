class Bosses:
    def __init__(self, player, nome, andar, nivel, hp, mana, forca, inteligencia, destreza, resistencia, sabedoria, carisma, reflexo):
        self.player = player
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
        print(f"player: {self.player}")
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


Boss1 = Bosses("Yasmin", "Beatrix ", 1, 80, 1700, 3000, 20, 40, 60, 30, 30, 80, 25)
boss2 = Bosses("Julia", "nickta", 5, 100, 1500, 999999, 40, 80, 50, 30, 100, 10, 40)
boss3 = Bosses("Bianca", "Yzma", 7, 100, 6666, 10000, 60, 60, 70, 50, 70, 35, 50)
boss4 = Bosses("Matheus", "Marack", 6, 100, 4500, 1000, 80, 70, 75, 50, 70, 60, 80)

def mostrar_informacao(opcao):
    if opcao == 1: Boss1.exibir_informacoes()
    elif opcao == 5: boss2.exibir_informacoes()
    elif opcao == 7: boss3.exibir_informacoes()
    elif opcao == 6: boss4.exibir_informacoes()
    else: print("Opção inválida. Por favor, escolha entre 1 e 8.")

def main():
    while True:
        try:
            opcao = int(input("Digite o numero do andar:"))
            if opcao in [1, 5, 7, 6]:
                mostrar_informacao(opcao)
                break
            else:
                print("Opção inválida. Por favor, escolha entre 1 e 8.")
        except ValueError:
            print("Por favor, digite um número válido.")


def tela_incial():
     while True:
          inicio = (input("""
digite sim para voltar 
digite não para encerrar"""))
          if inicio in ["sim"]:
               main()
          elif inicio in["não"]:
              print("encerrando")
              break
          else:
              print("Opção inválida.")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    tela_incial()
