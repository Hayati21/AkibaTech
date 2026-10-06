dollar_value = float(input("Enter the amount in dollars: "))
exchange_rate = float(input("Enter the exchange rate (1 USD to ETB): "))
line = "=================================="
birr_value = dollar_value * exchange_rate
print(f"{line} \n \t CURRENCY EXCHANGE \n{line} \n ")
print(f"USD Amount: {dollar_value} \n")
print(f"Exchange Rate: {exchange_rate} \n")
print(f"ETB Amount: {birr_value} \n{line}")
