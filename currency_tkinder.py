import tkinter as tk
from tkinter import ttk, messagebox

# Predefined exchange rates (as of a specific date)
exchange_rates = {
    'USD': {'EUR': 0.85, 'GBP': 0.75, 'INR': 83.0, 'JPY': 149.5},
    'EUR': {'USD': 1.18, 'GBP': 0.88, 'INR': 97.5, 'JPY': 175.0},
    'GBP': {'USD': 1.33, 'EUR': 1.14, 'INR': 110.0, 'JPY': 198.0},
    'INR': {'USD': 0.012, 'EUR': 0.010, 'GBP': 0.009, 'JPY': 1.8},
    'JPY': {'USD': 0.0067, 'EUR': 0.0057, 'GBP': 0.0050, 'INR': 0.56}
}

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        rate = exchange_rates[from_currency][to_currency]
        return amount * rate
    else:
        return None

# Function to perform conversion when the button is clicked
def on_convert():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combobox.get()
        to_currency = to_currency_combobox.get()

        result = convert_currency(amount, from_currency, to_currency)
        if result is not None:
            result_label.config(text=f"Result: {result:.2f} {to_currency}")
        else:
            messagebox.showerror("Error", "Conversion rate not available.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid amount.")

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Amount input
amount_label = tk.Label(root, text="Enter amount:")
amount_label.pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

# From currency selection
from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.pack(pady=5)
from_currency_combobox = ttk.Combobox(root, values=list(exchange_rates.keys()))
from_currency_combobox.pack(pady=5)
from_currency_combobox.current(0)  # Set default selection

# To currency selection
to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.pack(pady=5)
to_currency_combobox = ttk.Combobox(root, values=list(exchange_rates.keys()))
to_currency_combobox.pack(pady=5)
to_currency_combobox.current(1)  # Set default selection

# Convert button
convert_button = tk.Button(root, text="Convert", command=on_convert)
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
