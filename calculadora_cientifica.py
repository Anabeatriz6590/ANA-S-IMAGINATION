import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")
        self.root.configure(bg='gray15')

        self.expression = ""

        self.input_text = tk.StringVar()
        self.input_frame = self.create_input_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.create_input_field()
        self.create_buttons()

    def create_input_frame(self):
        frame = tk.Frame(self.root, bg='gray15')
        frame.pack(pady=20)
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.root, bg='gray15')
        frame.pack()
        return frame

    def create_input_field(self):
        input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('arial', 18), width=25, borderwidth=2, relief='solid')
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '√',
            '1', '2', '3', '-', 'x²',
            '0', '.', '+', '=', 'π',
            'sin', 'cos', 'tan', 'log', 'ln'
        ]

        row = 0
        col = 0
        for button in buttons:
            button_command = lambda x=button: self.on_button_click(x)
            tk.Button(self.buttons_frame, text=button, width=5, height=2, command=button_command, bg='white').grid(row=row, column=col, pady=5, padx=5)

            col += 1
            if col > 4:
                col = 0
                row += 1

    def on_button_click(self, button):
        if button == 'C':
            self.expression = ""
            self.input_text.set(self.expression)
        elif button == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Erro na aplicação.")
                self.expression = ""
        elif button == '√':
            self.expression = str(math.sqrt(eval(self.expression)))
            self.input_text.set(self.expression)
        elif button == 'x²':
            self.expression = str(eval(self.expression) ** 2)
            self.input_text.set(self.expression)
        elif button == 'π':
            self.expression += str(math.pi)
            self.input_text.set(self.expression)
        elif button in ('sin', 'cos', 'tan', 'log', 'ln'):
            try:
                if button == 'sin':
                    self.expression = str(math.sin(math.radians(eval(self.expression))))
                elif button == 'cos':
                    self.expression = str(math.cos(math.radians(eval(self.expression))))
                elif button == 'tan':
                    self.expression = str(math.tan(math.radians(eval(self.expression))))
                elif button == 'log':
                    self.expression = str(math.log10(eval(self.expression)))
                elif button == 'ln':
                    self.expression = str(math.log(eval(self.expression)))
                self.input_text.set(self.expression)
            except:
                self.input_text.set("Erro na aplicação.")
                self.expression = ""
        else:
            self.expression += str(button)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
