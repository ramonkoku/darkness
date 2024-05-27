class Jogador:
    
    def __init__(self, nome, vida_inicial=100):
        self.nome = nome
        self.__vida = vida_inicial
        self.inventario = []

    def adicionar_item(self, item):
        self.inventario.append(item)
        print(f"{self.nome} pegou o item '{item}'.")

    def usar_item(self, item):
        if item in self.inventario:
            print(f"{self.nome} usou o item '{item}'.")
        else:
            print(f"{self.nome} não possui o item '{item}' no inventário.")
class Jogador:
    def __init__(self, nome, vida_inicial=100):
       
        self.nome = nome
        self.__vida = vida_inicial
        self.__inventario = []

    def adicionar_item(self, item):

        self.__inventario.append(item)
        print(f"{self.nome} pegou o item '{item}'.")

    def usar_item(self, item):
        
        if item in self.__inventario:
            print(f"{self.nome} usou o item '{item}'.")
        else:
            print(f"{self.nome} não possui o item '{item}' no inventário.")

    def remover_item(self, item):
        
        if item in self.__inventario:
            self.__inventario.remove(item)
            print(f"{self.nome} removeu o item '{item}' do inventário.")
        else:
            print(f"{self.nome} não possui o item '{item}' no inventário.")

    def status_inventario(self):

        print(f"Inventário de {self.nome}: {', '.join(self.__inventario)}")

#uso
jogador1 = Jogador("zero")
jogador1.adicionar_item("foice")
jogador1.adicionar_item("pedra")
jogador1.adicionar_item("Poção de Cura")
jogador1.status_inventario()
jogador1.usar_item("Poção de Cura")
jogador1.remover_item("pedra")
jogador1.status_inventario()
