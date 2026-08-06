age = int(input("Enter your age: \n"))

wed = bool(input("Is it Wednesday?[True/False] \n"))
Price = 12 if age >= 18 else 8

if wed == True:
    Price -= 2

print("The price of the ticket is", Price)
