score = int(input("Enter your score: "))

match score:
    case s if s >= 90:
        print("A")
    case s if s >= 80:
        print("B")
    case s if s >= 70:
        print("C")
    case _:
        print("Fail")
        
    