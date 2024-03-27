class ListaDeCompras:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, categoria, item):
        if categoria not in self.itens:
            self.itens[categoria] = []
        self.itens[categoria].append(item)
        print(f"{item} foi adicionado à lista de {categoria}.")

    def mostrar_lista(self):
        if self.itens:
            print("Lista de Compras:")
            for categoria, itens in self.itens.items():
                print(f"\n{categoria}:")
                for item in itens:
                    print(f"- {item}")
        else:
            print("A sua lista de compras está vazia.")


if __name__ == "__main__":
    lista = ListaDeCompras()

    while True:
        print("\n1. Adicionar Item")
        print("2. Mostrar Lista")
        print("3. Sair")

        escolha = input("Escolha uma opção para prosseguir: ")

        if escolha == "1":
            categoria = input("Qual é categoria do item: ")
            item = input("Qual é o item a ser adicionado: ")
            lista.adicionar_item(categoria, item)
        elif escolha == "2":
            lista.mostrar_lista()
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
