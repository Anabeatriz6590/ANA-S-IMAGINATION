class CalculadoraDespesas:
    def __init__(self):
        self.despesas = {}

    def adicionar_despesa(self, categoria, valor):
        if categoria not in self.despesas:
            self.despesas[categoria] = []
        self.despesas[categoria].append(valor)
        print(f"Despesa de R${valor} na categoria '{categoria}' adicionada com sucesso.")

    def calcular_total_categoria(self, categoria):
        if categoria in self.despesas:
            total = sum(self.despesas[categoria])
            return total
        else:
            return 0

    def calcular_total_geral(self):
        total = sum(sum(values) for values in self.despesas.values())
        return total


if __name__ == "__main__":
    calculadora = CalculadoraDespesas()

    while True:
        print("\n1. Adicionar Despesa")
        print("2. Calcular Total por Categoria")
        print("3. Calcular Total Geral")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            categoria = input("Digite a categoria da despesa: ").upper()
            valor = float(input("Digite o valor da despesa: "))
            calculadora.adicionar_despesa(categoria, valor)
        elif escolha == "2":
            categoria = input("Digite a categoria para calcular o total: ").upper()
            total_categoria = calculadora.calcular_total_categoria(categoria)
            print(f"Total de despesas na categoria '{categoria}': R${total_categoria}")
        elif escolha == "3":
            total_geral = calculadora.calcular_total_geral()
            print(f"Total de despesas geral: R${total_geral}")
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


