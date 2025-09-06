""" Simple Calculator Module.
Basic arithmetic operations
"""

def add(x, y):
    """Return the sum of x and y."""
    return x + y


def sub(x, y):
    """Return the difference of x and y."""
    return x - y


def mul(x, y):
    """Return the product of x and y."""
    return x * y


def div(x, y):
    """Return the division of x by y. If y is 0, return an error message."""
    if y == 0:
        return "Cannot divide by 0"
    return x / y


def main():
    """Run the interactive calculator menu."""
    while True:
        # show menu
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
