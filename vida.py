class Jogador:
  
  def __init__(self, nome, vida_inicial=100):
    self.nome = nome
    self.__vida = vida_inicial

  def get_vida(self):
    return self.__vida

  def tomar_dano(self, pontos):
    self.__vida = max(0, self.__vida - pontos)  

jogador1 = Jogador("zero")

vida_atual = jogador1.get_vida()
print(f"{jogador1.nome} tem {vida_atual} pontos de vida")

jogador1.tomar_dano(50)
vida_atual = jogador1.get_vida()
print(f"{jogador1.nome} tomou dano e tem {vida_atual} pontos de vida")

print(f"{jogador1.nome} tem {jogador1.get_vida()} pontos de vida após o dano")
