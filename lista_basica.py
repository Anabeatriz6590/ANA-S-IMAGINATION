class ListaDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"{item} foi adicionado à lista.")

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            print(f"{item} foi removido da sua lista.")
        else:
            print(f"{item} não está na sua lista.")

    def mostrar_lista(self):
        if self.itens:
            print("----Lista de Compras----:")
            for item in self.itens:
                print(f"- {item}")
        else:
            print("A sua lista de compras está vazia.")


if __name__ == "__main__":
    lista = ListaDeCompras()

    while True:
        print("\n1. Adicionar novo Item")
        print("2. Remover Item")
        print("3. Mostrar Lista")
        print("4. Sair")

        escolha = input("Escolha uma opção para prosseguir: ")

        if escolha == "1":
            item = input("Digite o item a ser adicionado: ")
            lista.adicionar_item(item)
        elif escolha == "2":
            item = input("Digite o item a ser removido: ")
            lista.remover_item(item)
        elif escolha == "3":
            lista.mostrar_lista()
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.Por favor, tente novamente.")
