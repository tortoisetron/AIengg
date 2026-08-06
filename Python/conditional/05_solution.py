weather  = input("Enter the weather: ")

match weather:
    case w if w == "sunny":
        print('go for a walk')
    case w if w == "rainy":
        print('read a book')
    case w if w == "cloudy":
        print('go to the beach')
    case _:
        print('stay at home')