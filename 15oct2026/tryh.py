try:
    a = input("enter number 1:")
    b = input("enter number 2:")
    print(int(a)/int(b))
except valueerror:
    print("Give the numbers as a input")
except ZerodivisionError:
    print("cannot divide by zero:")