def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# main function
def main():
    check = 1
    print("Welcome to calculator")
    while check >= 1:        
        print("0: exit, 1: plus, 2: minus, 3: multiply, 4: divide")
        check = int(input())
        if check == 1:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", add(x, y))
        elif check == 2:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", subtract(x, y))
        elif check == 3:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", multiply(x, y))
        elif check == 4:
            print("First Number")
            x = float(input())
            print("Second Number")
            y = float(input())
            print("answer : ", divide(x, y))
        else:
            print("Thank you")

if __name__ == "__main__":
    main()
