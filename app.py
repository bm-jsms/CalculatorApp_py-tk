import tkinter as tk

root = tk.Tk()


class Calculator:
    def __init__(self, main):
        self.main = main
        self.display = tk.Entry(main, width=15, font=(
            "Arial", 16), bg="#01145d", fg="white", bd=10, insertwidth=1, justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

        row = 1
        col = 0

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", ".", "+", "="
        ]

        for button in buttons:
            print(f"Button: {button}")
            self.build_button(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def clear_display(self):
        self.display.delete(0, "end")

    def build_button(self, value, row, col):
        if value == "C":
            b = tk.Button(self.main, text=value, width=5, command=self.clear_display, bg="#ff0018", fg="white", bd=3)
        else:
            b = tk.Button(self.main, text=value, width=5, bg="#0563af", fg="white",bd=5)

        b.grid(row=row, column=col)


root.title("Calculator")

my_calc = Calculator(root)


root.mainloop()
