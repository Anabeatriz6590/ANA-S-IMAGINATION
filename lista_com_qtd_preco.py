class ListaDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item, quantidade, preco_unitario):
        self.itens.append({
            "item": item,
            "quantidade": quantidade,
            "preco_unitario": preco_unitario
        })
        print(f"{quantidade} {item}(s) adicionado(s) à lista por R${preco_unitario} cada.")

    def calcular_total(self):
        total = sum(item["quantidade"] * item["preco_unitario"] for item in self.itens)
        return total

    def mostrar_lista(self):
        if self.itens:
            print("Lista de Compras:")
            for item in self.itens:
                print(f"{item['quantidade']} {item['item']}(s) - R${item['preco_unitario']} cada")
            print("Total: R$", self.calcular_total())
        else:
            print("A sua lista de compras está vazia.")


if __name__ == "__main__":
    lista = ListaDeCompras()

    while True:
        print("\n1. Adicionar Item")
        print("2. Mostrar Lista")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            item = input("Qual é o nome do item: ")
            quantidade = int(input("Digite a quantidade: "))
            preco_unitario = float(input("Digite o preço unitário: "))
            lista.adicionar_item(item, quantidade, preco_unitario)
        elif escolha == "2":
            lista.mostrar_lista()
        elif escolha == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")
