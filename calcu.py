import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.result_var = tk.StringVar()

        # Entry widget to display the result
        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Helvetica", 16), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Define buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create buttons dynamically
        row_val = 1
        col_val = 0
        for button in buttons:
            cmd = lambda x=button: self.on_button_click(x)
            tk.Button(root, text=button, width=5, height=2, command=cmd).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:  # Move to the next row after 4 buttons
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            # Calculate the expression
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            # Append the character to the entry
            self.result_var.set(self.result_var.get() + char)

# Create the main window
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
