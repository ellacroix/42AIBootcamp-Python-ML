import sys

if len(sys.argv) == 1: exit()

if len(sys.argv) == 2 and sys.argv[1].isnumeric():
    if int(sys.argv[1]) == 0:
        print("I'm Zero.")
    elif int(sys.argv[1])%2:
        print("I'm Odd.")
    else:
        print("I'm Even.")
else:
    print("ERROR")