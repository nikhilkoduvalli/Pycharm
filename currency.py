
exchange_rates = {
    'USD': {'EUR': 0.85, 'GBP': 0.75, 'INR': 83.0, 'JPY': 149.5},
    'EUR': {'USD': 1.18, 'GBP': 0.88, 'INR': 97.5, 'JPY': 175.0},
    'GBP': {'USD': 1.33, 'EUR': 1.14, 'INR': 110.0, 'JPY': 198.0},
    'INR': {'USD': 0.012, 'EUR': 0.010, 'GBP': 0.009, 'JPY': 1.8},
    'JPY': {'USD': 0.0067, 'EUR': 0.0057, 'GBP': 0.0050, 'INR': 0.56}
}



def convert_currency(amount, from_currency, to_currency):

    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        rate = exchange_rates[from_currency][to_currency]
        return amount * rate
    else:
        print("Conversion rate not available for the selected currency pair.")
        return None



def main():
    print("Welcome to Currency Converter!")


    from_currency = input("Enter the currency you have (e.g., USD): ").upper()
    to_currency = input("Enter the currency you want (e.g., EUR): ").upper()

    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return


    result =convert_currency(amount, from_currency, to_currency)
    if result is not None:
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
    else:
        print("Conversion failed.")


if __name__ == "__main__":
    main()
