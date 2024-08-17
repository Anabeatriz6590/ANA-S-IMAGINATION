import sqlite3

#conectando ao bd
def conectar_db():
    return sqlite3.connect("notas.db")

def criar_tabela():
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudantes (
            nome TEXT PRIMARY KEY,
            nota REAL
        )
        """)
        conn.commit()

def registrar_notas(nome, nota):
    with conectar_db() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO estudantes (nome, nota) VALUES (?, ?)", (nome,nota))
            conn.commit()
            print(f"A nota {nota} foi registrada com sucesso para {nome}.")
        except sqlite3.IntegrityError:
            print(f"As notas existentes para {nome}. Use a função Editar Notas para conseguir modificar.")

def editar_notas(nome, nova_nota):
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE estudantes SET nota = ? WHERE nome = ?", (nova_nota, nome))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"A nota de {nome}, foi atualizada para {nova_nota}.")
        else:
            print(f"{nome} não encontrado. Use a função Registrar Notas para conseguir adicionar.")

def visualizar_notas():
    with conectar_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT nome, nota FROM estudantes")
        notas = cursor.fetchall()
        if notas:
            for nome, nota in notas:
                print(f"Estudante: {nome} - Nota: {nota}")
        else:
            print("Nenhuma nota registrada.")

def menu():
    criar_tabela()
    while True:
        print("\nMenu: ")
        print("1. Registrar Notas")
        print("2. Editar Notas")
        print("3. Visualizar Notas")
        print("4. Sair do Sistema")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do Estudante: ")
            try:
                nota = float(input("Nota: "))
                registrar_notas(nome, nota)
            except ValueError:
                print("Nota inválida. PRECISA ser um número (1, 2, 3...).")

        elif escolha == "2":
            nome = input("Nome do Estudante: ")
            try:
                nova_nota = float(input("Nova Nota: "))
                editar_notas(nome, nova_nota)
            except ValueError:
                print("Nota inválida. PRECISA ser um número (1, 2, 3...).")

        elif escolha == "3":
            visualizar_notas()

        elif escolha == "4":
            print("Saindo do sistema. Aguarde...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
