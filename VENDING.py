prices_inr = [
    124.50, 83.00, 53.95, 83.00, 166.00,
    249.00, 207.50, 145.25, 99.60, 207.50,
    83.00, 166.00, 124.50, 103.75, 145.25,
    290.50, 166.00, 249.00, 186.75, 207.50,
    124.50, 103.75
]

items = [
    "Soda", "Chips", "Candy", "Water", "Juice",
    "Energy Drink", "Protein Bar", "Sparkling Water",
    "Granola Bar", "Cookies", "Gummy Bears", "Ice Tea",
    "Lemonade", "Chocolate Bar", "Potato Skins", "Beef Jerky",
    "Pretzels", "Almonds", "Trail Mix", "Coconut Water",
    "Herbal Tea", "Root Beer"
]

stock = [5] * len(items)

def display_items():
    print("\nItems available in the vending machine (Prices in INR):")
    for i in range(len(items)):
        print(f"{i+1} : {items[i]} - ₹{prices_inr[i]:.2f} (Stock: {stock[i]})")

def vending_machine_process():
    cart = []
    total_cost = 0.0

    while True:
        display_items()

        choice = input("\nEnter the number of the item you want to buy, or 'done' to proceed to payment: ").lower()

        if choice == 'done':
            if not cart:
                print("Your cart is empty. Please select at least one item.")
                continue
            break

        if choice.isdigit() and 1 <= int(choice) <= len(items):
            idx = int(choice) - 1
            item = items[idx]
            price = prices_inr[idx]

            if stock[idx] == 0:
                print(f"Sorry, {item} is sold out.")
                continue

            quantity = int(input(f"How many {item}(s) would you like? "))
            if quantity > stock[idx]:
                print(f"Sorry, only {stock[idx]} {item}(s) available.")
                continue

            stock[idx] -= quantity

            cart.append((item, price, quantity))
            total_cost += price * quantity

            print(f"Added {quantity} {item}(s) to your cart. Stock updated. Current total: ₹{total_cost:.2f}")
        else:
            print("Invalid selection.")

    print("\nYour Cart:")
    for item, price, quantity in cart:
        print(f"{quantity} x {item} - ₹{price:.2f} each")

    print(f"\nTotal cost: ₹{total_cost:.2f}")

    total_inserted = 0.0
    while total_inserted < total_cost:
        remaining_amount = total_cost - total_inserted
        print(f"Remaining balance: ₹{remaining_amount:.2f}")
        inserted_money = float(input(f"Please insert ₹{remaining_amount:.2f}: ₹"))
        total_inserted += inserted_money

    change = total_inserted - total_cost
    if change > 0:
        print(f"\nPurchase complete! Dispensing items and returning change: ₹{change:.2f}")
    else:
        print("\nPurchase complete! Dispensing items...")

def main():
    print("Welcome to the Vending Machine!")
    vending_machine_process()

main()


