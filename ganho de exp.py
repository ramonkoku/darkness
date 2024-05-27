import logging

logging.basicConfig(level=logging.INFO)

class Jogador:
    EXPERIENCIA_PARA_NIVEL = 100
    VIDA_INICIAL = 100

    def __init__(self, nome):
        self.nome = nome
        self.__vida = self.VIDA_INICIAL
        self.nivel = 1
        self.experiencia = 0

    def ganhar_experiencia(self, pontos):
        self.experiencia += pontos
        logging.info(f"{self.nome} ganhou {pontos} pontos de experiência.")

        if self.experiencia >= self.EXPERIENCIA_PARA_NIVEL:
            self.subir_de_nivel()

    def subir_de_nivel(self):
        self.nivel += 1
        self.experiencia = 0
        logging.info(f"{self.nome} subiu para o nível {self.nivel}!")

    def status(self):
        print(f"Nome: {self.nome}")
        print(f"Nível: {self.nivel}")
        print(f"Vida: {self.__vida}/{self.VIDA_INICIAL}")
        print(f"Experiência: {self.experiencia}/{self.EXPERIENCIA_PARA_NIVEL}")


jogador1 = Jogador("zero")

print("Status inicial do jogador:")
jogador1.status()
print()

jogador1.ganhar_experiencia(100)
jogador1.ganhar_experiencia(100)

print("\nStatus após ganhar experiência:")
jogador1.status()
print()
