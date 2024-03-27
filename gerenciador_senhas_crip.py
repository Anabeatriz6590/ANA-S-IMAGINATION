import hashlib

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.passwords[website] = {"username": username, "password": hashed_password}
        print(f"Senha para {website} adicionada com sucesso.")

    def get_password(self, website):
        if website in self.passwords:
            return self.passwords[website]
        else:
            return None

    def list_websites(self):
        print("Websites com suas senhas salvas:")
        for website in self.passwords:
            print(website)

if __name__ == "__main__":
    manager = PasswordManager()

    while True:
        print("\n1. Adicionar uma Senha")
        print("2. Obter Senha")
        print("3. Listar Websites")
        print("4. Sair")

        choice = input("Escolha uma opção para prosseguir: ")

        if choice == "1":
            website = input("Insira o nome do website: ").upper()
            username = input("Digite o seu nome de usuário: ")
            password = input("Digite a sua senha: ")
            manager.add_password(website, username, password)
        elif choice == "2":
            website = input("Digite o nome do website para obter a senha: ").upper()
            stored_password = manager.get_password(website)
            if stored_password:
                print(f"Username: {stored_password['username']}")
                print("Password: *****")
            else:
                print("Senha não encontrada para esse website.")
        elif choice == "3":
            manager.list_websites()
        elif choice == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")