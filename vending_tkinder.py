
import tkinter as tk
from tkinter import ttk, messagebox

# Prices and inventory for items
items = [
    "Soda", "Chips", "Candy", "Water", "Juice",
    "Gum", "Chocolate", "Nuts", "Cookies", "Energy Drink",
    "Tea", "Coffee", "Sports Drink", "Granola Bar", "Ice Tea",
    "Fruit Snacks", "Beef Jerky", "Dried Fruit", "Pretzels", "Popcorn",
    "Mints", "Fruit Juice"
]

prices_usd = [
    1.50, 1.00, 0.65, 1.00, 2.00,
    0.75, 1.25, 1.50, 1.00, 2.50,
    1.00, 1.50, 1.75, 1.25, 1.50,
    1.00, 1.75, 1.25, 0.99, 1.00,
    1.50, 1.52
]

# Exchange rate (USD to INR)
usd_to_inr = 83
prices_inr = [price * usd_to_inr for price in prices_usd]
stock = [5] * len(items)  # Inventory for each item
# Create the main window
root = tk.Tk()
root.title("Vending Machine")
root.geometry("480x320")  # Set smaller window size
root.configure(bg="#F0F0F0")  # Set background color

# Apply ttk styling for a modern look
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 10), padding=5)

# Cart to store selected items
cart = []
total_cost = 0.0
selected_item_index = None  # Keep track of selected item


# Function to select an item
def select_item(index):
    global selected_item_index
    selected_item_index = index
    selected_item_label.config(text=f"Selected Item: {items[index]} - ₹{prices_inr[index]:.2f} (Stock: {stock[index]})")
    quantity_entry.delete(0, tk.END)  # Clear the quantity entry


# Function to add the selected item and quantity to the cart
def add_to_cart():
    global total_cost
    if selected_item_index is None:
        messagebox.showwarning("No Item Selected", "Please select an item first.")
        return
    quantity_str = quantity_entry.get()

    if not quantity_str.isdigit():
        messagebox.showwarning("Invalid Quantity", "Please enter a valid quantity.")
        return

    quantity = int(quantity_str)
    if quantity <= 0:
        messagebox.showwarning("Invalid Quantity", "Quantity must be at least 1.")
        return

    if quantity > stock[selected_item_index]:
        messagebox.showwarning("Insufficient Stock",
                               f"Only {stock[selected_item_index]} {items[selected_item_index]}(s) available.")
        return

    # Deduct from stock and add to cart
    stock[selected_item_index] -= quantity
    item = items[selected_item_index]
    price = prices_inr[selected_item_index]
    cart.append((item, price, quantity))
    total_cost += price * quantity

    update_cart_display()
    update_total_label()
    update_stock_display()  # Update stock after adding to the cart
    messagebox.showinfo("Added to Cart", f"Added {quantity} {item}(s) to your cart.")

# Function to update the cart display
def update_cart_display():
    cart_listbox.delete(0, tk.END)
    for item, price, quantity in cart:
        cart_listbox.insert(tk.END, f"{quantity} x {item} - ₹{price:.2f} each")


# Function to update the total cost label
def update_total_label():
    total_label.config(text=f"Total: ₹{total_cost:.2f}")


# Function to update stock display on the buttons
def update_stock_display():
    for i, button in enumerate(item_buttons):
        button.config(text=f"{items[i]} - ₹{prices_inr[i]:.2f} (Stock: {stock[i]})")


# Function to handle payment
def proceed_to_payment():
    global total_cost
    if total_cost == 0:
        messagebox.showwarning("Empty Cart", "Your cart is empty. Please add at least one item.")
        return

    # Simulate payment process
    inserted_money_str = insert_money_entry.get()
    try:
        inserted_money = float(inserted_money_str)
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please insert a valid amount of money.")
        return

    if inserted_money < total_cost:
        messagebox.showwarning("Insufficient Funds", f"Please insert at least ₹{total_cost:.2f}.")
    else:
        change = inserted_money - total_cost
        messagebox.showinfo("Payment Complete", f"Payment successful! Your change is ₹{change:.2f}.")
        reset_vending_machine()


# Function to reset the machine after purchase
def reset_vending_machine():
    global total_cost, cart, selected_item_index
    cart = []
    total_cost = 0.0
    selected_item_index = None
    update_cart_display()  # Clear the cart display
    update_total_label()  # Reset total cost to 0
    quantity_entry.delete(0, tk.END)
    insert_money_entry.delete(0, tk.END)
    selected_item_label.config(text="Selected Item: None")
    update_stock_display()  # Update stock on buttons

# Header
header_label = tk.Label(root, text="Vending Machine", font=("Helvetica", 16, "bold"), bg="#F0F0F0", pady=10)
header_label.pack()

# Create the layout of the GUI
item_frame = ttk.Frame(root)
item_frame.pack(pady=5)

item_buttons = []  # Store buttons to update stock dynamically

def update_button_style(button, stock):
    if stock == 0:
        button.config(state="disabled", style="TButton.TDisabled")
    else:
        button.config(state="normal", style="TButton")

def update_button_style(button, stock):
    """Update the button style based on the item's stock."""
    if stock == 0:
        button.config(state="disabled")  # Disable button if out of stock
    else:
        button.config(state="normal")  # Enable button if in stock


# Create buttons for each item and display stock
for i, item in enumerate(items):
    btn = ttk.Button(item_frame, text=f"{item} - ₹{prices_inr[i]:.2f} (Stock: {stock[i]})",
                     command=lambda i=1: select_item(i))
    btn.grid(row=i // 4, column=i % 4, padx=3, pady=3)
    item_buttons.append(btn)
    update_button_style(btn, stock[i])  # Update button style based on stock

# Selected item display
selected_item_label = tk.Label(root, text="Selected Item: None", font=("Helvetica", 10), bg="#F0F0F0")
selected_item_label.pack(pady=5)

# Quantity selection
quantity_frame = ttk.Frame(root)
quantity_frame.pack(pady=5)

quantity_label = ttk.Label(quantity_frame, text="Quantity:")
quantity_label.grid(row=0, column=0, padx=5)
quantity_entry = ttk.Entry(quantity_frame, width=5)
quantity_entry.grid(row=0, column=1)

# Add to cart button
add_to_cart_button = ttk.Button(root, text="Add to Cart", command=add_to_cart)
add_to_cart_button.pack(pady=5)

# Cart display
cart_label = ttk.Label(root, text="Your Cart")
cart_label.pack()

cart_listbox = tk.Listbox(root, width=45, height=6)
cart_listbox.pack(pady=5)

# Total cost
total_label = tk.Label(root, text="Total: ₹0.00", font=("Helvetica", 10, "bold"), bg="#F0F0F0")
total_label.pack(pady=5)

# Insert money input
insert_money_frame = ttk.Frame(root)
insert_money_frame.pack(pady=5)

insert_money_label = ttk.Label(insert_money_frame, text="Insert Money:")
insert_money_label.grid(row=0, column=0, padx=5)

insert_money_entry = ttk.Entry(insert_money_frame, width=10)
insert_money_entry.grid(row=0, column=1)
# Payment button
payment_button = ttk.Button(root, text="Proceed to Payment", command=proceed_to_payment)
payment_button.pack(pady=10)

# Run the GUI
root.mainloop()
