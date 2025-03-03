dollar = float(input("How much dollar do you have? "))
currency = input("What currency you want to have? ").upper()

print("\nDollar:", dollar, "USD")

if currency == "PHP":
    php = dollar * 54.81
    print("Philippine Peso:", php)
else:
    print("Currency not available.")