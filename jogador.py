class Jogador:

    def __init__(self, nome, andar, nivel, hp, mana, força, inteligencia, destreza, resistência, sabetoria, carisma, reflexo):
        self.nome = nome
        self.andar = andar
        self.nivel = nivel
        self.hp = hp
        self.mana = mana
        self.forca = força
        self.inteligencia = inteligencia
        self.destreza = destreza
        self.resistência = resistência
        self.sabetoria = sabetoria
        self.carisma = carisma
        self.reflexo = reflexo

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"andar: {self.andar}")
        print(f"Nível: {self.nivel}")
        print(f"HP: {self.hp}")
        print(f"Mana: {self.mana}")
        print(f"Força: {self.forca}")
        print(f"Inteligência: {self.inteligencia}")
        print(f"destreza: {self.destreza}")
        print(f"Defesa: {self.resistência}")
        print(f"sabetoria: {self.sabetoria}")
        print(f"carisma: {self.carisma}")
        print(f"reflexo: {self.reflexo}")   

jogador1 = Jogador("Beatrix", 1, 80, 1700, 3000, 20, 40, 60, 30, 30, 80, 25)
jogador2 = Jogador("Makeda", 6, 100, 1500, 999999, 40, 80, 50, 30, 100, 10, 40)
jogador3 = Jogador("yzma", 7, 100, 6666, 10000, 60, 60, 70, 50, 70, 35, 50)
jogador4 = Jogador("Marack", 5, 100, 4500, 1000, 80, 70, 75, 50, 70, 60, 80)
jogador5 = Jogador("")
jogador6 = Jogador("")
jogador7 = Jogador("")
jogador8 = Jogador("")

jogador1.exibir_informacoes()
print()
jogador2.exibir_informacoes()
print()
jogador3.exibir_informacoes()
print()
jogador4.exibir_informacoes()
print()