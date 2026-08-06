fruit = input("Enter the fruit name: ")

color = input("Enter the color of the fruit: ")

if color == "green":
    print(f"{fruit} is unripe")
elif color == "yellow":
    print(f"{fruit} is ripe")
elif color == "brown":
    print(f"{fruit} is overripe")
else:
    print("Unknown color")

