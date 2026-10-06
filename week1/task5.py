customer_name = str(input("Enter your name: "))
product_name = str(input("Enter your product name: "))
price = float(input("Enter the price per unit: "))
quantity = float(input("Enter the amount you buy: "))
line = "========================================" 
total = price * quantity

print(line + "\n" + "\t" + "RECEIPT "+ "\n" + line + "\n")
print(f"Customer: {customer_name} \n")
print(f"Product\t Price \t Quantity")
print("-------------------------------")
print(f"{product_name}\t {price}ETB \t {quantity}")
print(f"Total:\t {total} \n")
print("Thank you for shopping!")
print(line)

