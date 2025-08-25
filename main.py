"""Simple Calculator ."""

def add(x, y):
    """Adding  x and y."""
    return x + y

def sub(x, y):
    """Subtracting x and y."""
    return x - y

def mul(x, y):
    """Multiplying x and y."""
    return x * y

def div(x, y):
    """Dividing x by y."""
    if y == 0:
        return "Cannot divide by 0"
    return x / y

def main():
   
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        ch = input("Choose (1-5): ")

        if ch == "5":
            print("Goodbye")
            break

        if ch in ["1", "2", "3", "4"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if ch == "1":
                print("Ans:", add(a, b))
            elif ch == "2":
                print("Ans:", sub(a, b))
            elif ch == "3":
                print("Ans:", mul(a, b))
            elif ch == "4":
                print("Ans:", div(a, b))
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()
