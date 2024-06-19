class Jogador:
    def __init__(self, nome,):
       
        self.nome = nome
        self.__inventario = []

    def item_atuais (self, item):

        self.__inventario.append(item)

    def itens_adicionados(self):
        for item in self.__inventario:
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
        if self.__inventario:
            print(f"Inventário de {self.nome}: {', '.join(self.__inventario)}")
        else:
            print(f"Inventário de {self.nome} está vazio.")

#uso
jogador1 = Jogador("Beatrix")
jogador2 = Jogador("makeda")
jogador3 = Jogador("Yzma")
jogador4 = Jogador("Marack")


# Adicionar itens sem exibir mensagens
jogador1.item_atuais("rosas vermelhas")
jogador2.item_atuais("cajado da atrofia")
jogador2.item_atuais("livro da verdade")
jogador2.item_atuais("3 pergaminhos de água")
jogador2.item_atuais("1 pergaminho de ar")
jogador2.item_atuais("2 pergaminhos de fogo")
jogador3.item_atuais("chicote (cauda da medusa)")
jogador4.item_atuais("orbe (dominio das armas)")
jogador4.item_atuais("foice (sede de sangue)")

# Status dos inventários
print()
jogador1.status_inventario()
jogador2.status_inventario()
jogador3.status_inventario()
jogador4.status_inventario()