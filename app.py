import tkinter as tk

root = tk.Tk()


class Calculator:
    def __init__(self, main):
        self.main = main
        self.display = tk.Entry(main, width=15, font=("Arial", 16), bg="#000105", fg="white", borderwidth=2)
        self.display.grid(row=0, column=0)


root.geometry("400x600")
root.title("Calculator")

my_calc = Calculator(root)


root.mainloop()
