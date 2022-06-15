import sys

if len(sys.argv) == 3 and sys.argv[1].isnumeric() and sys.argv[2].isnumeric():
    number1 = int(sys.argv[1])
    number2 = int(sys.argv[2])
    print("Sum:\t\t", number1 + number2)
    print("Difference:\t", number1 - number2)
    print("Product:\t", number1 * number2)
    if number2 == 0:
        print("Quotient:\t ERROR (div by zero)")
        print("Remainder:\t ERROR (modulo by zero)")
    else:
        print("Quotient:\t", number1 / number2)
        print("Remainder:\t", number1 % number2)
else:
    if len(sys.argv) > 3:
        print("InputError: too many arguments\n")
    elif sys.argv[1].isnumeric()==False or sys.argv[2].isnumeric()==False:
        print("InputError: only numbers\n")
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("   python operations.py 10 3")