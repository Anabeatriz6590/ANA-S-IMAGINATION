class GerenciadorLivros:
    def __init__(self):
        self.livros = {}
        print("Seja Bem-vindo(a) ao seu Gerenciador de Livros Pessoal. Qual ação você deseja executar?")

    def adicionar_livros(self, titulo, autor, ano, categoria):
        if titulo in self.livros:
            print(f"O livro '{titulo}' já existe na biblioteca.")
            return
        self.livros[titulo] = {
            'Autor' : autor,
            'Ano' : ano,
            'Categoria' : categoria
        }
        print(f"O livro '{titulo}' foi adicionado com sucesso!")


    def editar_livros(self, titulo, novo_titulo=None, novo_autor=None, novo_ano=None, nova_categoria=None):
        if titulo not in self.livros:
            print(f"O livro '{titulo}' NÃO foi encontrado na biblioteca. Tente um diferente.")
            return
        if novo_titulo:
            self.livros[novo_titulo] = self.livros.pop(titulo)
            titulo = novo_titulo
        if novo_autor:
            self.livros[titulo]['Autor'] = novo_autor
        if novo_ano:
            self.livros[titulo]['Ano'] = novo_ano
        if nova_categoria:
            selfl.livros[titulo]['Categoria'] = nova_categoria

        print(f"O livro '{titulo}' foi editado com sucesso.")


    def excluir_livros(self, titulo):
        if titulo in self.livros:
            del self.livros[titulo]
            print(f"O livro '{titulo}' foi REMOVIDO com sucesso.")
        else:
            print(f"O livro '{titulo}' NÃO foi encontrado na sua biblioteca.")


    def listar_livros(self):
        if not self.livros:
            print("A biblioteca está VAZIA.")
            return
        print("Lista de livros na biblioteca: ")
        for titulo, info in self.livros.items():
            print(f"- {titulo} por {info['autor']} ({info['ano']}), Categoria: {info['categoria']}")


    def pesquisar_por_categoria(self, categoria):
        livros_encontrados = [titulo for titulo, info in self.livros.items() if info['categoria'].lower() == categoria.lower()]
        if not livros_encontrados:
            print(f"Nenhum livro encontrado nessa categoria - {categoria}. Tente novamente.")
        else:
            print(f"Livros na categoria '{categoria}': ")
            for titulo in livros_encontrados:
                print(f"- {titulo}")


    def menu(self):
        while True:
            print("\n--- Menu de Opções ---")
            print("1. Adicionar livro")
            print("2. Editar livro")
            print("3. Excluir livro")
            print("4. Listar TODOS os livros")
            print("5. Pesquisar livros por CATEGORIA")
            print("6. Sair")
            opcao = input("Escolha uma opção para continuar: ")

            if opcao == '1':
                titulo = input("Digite o título do livro: ")
                autor = input("Digite o autor do livro: ")
                ano = input("Digite o ano de publicação: ")
                categoria = input("Digite a categoria do livro: ")
                self.adicionar_livros(titulo, autor, ano, categoria)
            elif opcao == '2':
                titulo = input("Digite o título do livro que deseja editar: ")
                novo_titulo = input("Digite o novo título (ou pressione Enter para manter o atual): ")
                novo_autor = input("Digite o novo autor (ou pressione Enter para manter o atual): ")
                novo_ano = input("Digite o novo ano (ou pressione Enter para manter o atual): ")
                nova_categoria = input("Digite a nova categoria (ou pressione Enter para manter a atual): ")
                self.editar_livros(titulo, novo_titulo if novo_titulo else None,
                                  novo_autor if novo_autor else None,
                                  novo_ano if novo_ano else None,
                                  nova_categoria if nova_categoria else None)
            elif opcao == '3':
                titulo = input("Digite o título do livro que deseja excluir: ")
                self.excluir_livros(titulo)
            elif opcao == '4':
                self.listar_livros()
            elif opcao == '5':
                categoria = input("Digite a categoria para pesquisa: ")
                self.pesquisar_por_categoria(categoria)
            elif opcao == '6':
                print("Saindo do gerenciador de livros... Até logo.")
                break
            else:
                print("Opção inválida. Tente novamente.")


biblioteca = GerenciadorLivros()
biblioteca.menu()

