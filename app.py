import tkinter as tk

root = tk.Tk()


class Calculator:
    def __init__(self, main):
        self.main = main
        self.display = tk.Entry(main, width=15, font=("Arial", 16), bg="#01145d", fg="white", bd=10, insertwidth=1, justify="right")
        self.display.grid(row=0, column=0, columnspan=4)
        self.op_verification = False
        self.current = ""
        self.op = ""
        self.total = 0

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

    def calculate(self):
        print(f"Calculate: {self.current}")
        
    
    def click(self, button):

        if self.op_verification:
            self.op_verification = False

        self.display.insert("end", button)

        if button in "0123456789" or button == ".":
            self.current += button
        else:
            if self.current:
                if not self.op:
                    self.total = float(self.current)
            self.current = ""

            self.op_verification = True
            self.op = button    
            
        print(f"\n[+] You press: {button}")
        print(f"[+] Current: {self.current}")
        print(f"[+] Op Verification: {self.op_verification}")
        print(f"[+] Op: {self.op}")
        print(f"[+] Total: {self.total}")

    def build_button(self, value, row, col):
        if value == "C":
            b = tk.Button(self.main, text=value, width=5, command=lambda: self.clear_display(), bg="#ff0018", fg="white", bd=3)
        elif value == "=":
            b = tk.Button(self.main, text=value, width=5, bg="#1f8a0f", fg="white", bd=5, command=lambda: self.calculate())
        else:
            b = tk.Button(self.main, text=value, width=5, bg="#0563af", fg="white",bd=5, command=lambda: self.click(value))

        b.grid(row=row, column=col)


root.title("Calculator")

my_calc = Calculator(root)


root.mainloop()
