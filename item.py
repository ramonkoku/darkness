class Jogador:
    def __init__(self, nome,):
       
        self.nome = nome
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
jogador1 = Jogador("Beatrix")
jogador2 = Jogador("makeda")
jogador3 = Jogador("Yzma")
jogador4 = Jogador("Marack")

# jogador1
jogador1.adicionar_item("rosas vermelhas")

# jogador2
jogador2.adicionar_item("cajado da atrofia")
jogador2.adicionar_item("livro da verdade")
jogador2.adicionar_item("3 pergaminho de água")
jogador2.adicionar_item("1 pergaminho de ar")
jogador2.adicionar_item("2 pergaminho de fogo")

# jogador3
jogador3.adicionar_item("chicote (cauda da medusa)")

# status dos inventarios
jogador1.status_inventario()
jogador2.status_inventario()
jogador3.status_inventario()