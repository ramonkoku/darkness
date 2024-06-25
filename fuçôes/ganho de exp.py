import logging

logging.basicConfig(level=logging.INFO)

class Jogador:
    EXPERIENCIA_PARA_NIVEL = 100

    def __init__(self, nome):
        self.nome = nome
        self.nivel = 1
        self.experiencia = 0
        self.experiencia_para_proximo_nivel = self.EXPERIENCIA_PARA_NIVEL

    def ganhar_experiencia(self, pontos):
        self.experiencia += pontos
        logging.info(f"{self.nome} ganhou {pontos} pontos de experiência. Total: {self.experiencia}")

        while self.experiencia >= self.experiencia_para_proximo_nivel:
            self.experiencia -= self.experiencia_para_proximo_nivel
            self.subir_de_nivel()

    def subir_de_nivel(self):
        self.nivel += 1
        logging.info(f"{self.nome} subiu para o nível {self.nivel}!")
        self.experiencia_para_proximo_nivel = int(self.EXPERIENCIA_PARA_NIVEL * 2**(self.nivel - 1))
        logging.info(f"Experiência para o próximo nível: {self.experiencia_para_proximo_nivel}")

    def status(self):
        print(f"Nome: {self.nome}")
        print(f"Nível: {self.nivel}")
        print(f"Experiência: {self.experiencia}/{self.EXPERIENCIA_PARA_NIVEL}")


jogador1 = Jogador("zero")

jogador1.ganhar_experiencia(100)

print("\n")
jogador1.status()
print()
