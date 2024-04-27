import turtle

class ShapeDrawer:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)

    def draw_shape(self, sides, length, color):
        self.pen.color(color)
        angle = 360 / sides
        for _ in range(sides):
            self.pen.forward(length)
            self.pen.right(angle)

    def draw_square(self, length, color):
        self.draw_shape(4, length, color)

    def draw_triangle(self, length, color):
        self.draw_shape(3, length, color)

    def draw_circle(self, radius, color):
        self.pen.color(color)
        self.pen.circle(radius)

    def clear_screen(self):
        self.pen.clear()

    def exit_program(self):
        turtle.bye()

def main():
    turtle.bgcolor("lightgray")  # Define a cor de fundo da janela
    drawer = ShapeDrawer()
    while True:
        print('Escolha uma opção:')
        print("1. Desenhar um quadrado")
        print("2. Desenhar um triângulo")
        print("3. Desenhar um círculo")
        print("4. Limpar a tela")
        print("5. Sair do programa")
        choice = input("Opção: ")
        
        if choice == '1':
            length = int(input("Digite o tamanho do quadrado: "))
            color = input("Digite a cor do quadrado: ")
            drawer.draw_square(length, color)
        elif choice == '2':
            length = int(input("Digite o tamanho do triângulo: "))
            color = input("Digite a cor do triângulo: ")
            drawer.draw_triangle(length, color)
        elif choice == '3':
            radius = int(input("Digite o raio do círculo: "))
            color = input("Digite a cor do círculo: ")
            drawer.draw_circle(radius, color)
        elif choice == '4':
            drawer.clear_screen()
        elif choice == '5':
            drawer.exit_program()
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida para continuar.")

if __name__ == '__main__':
    main()
