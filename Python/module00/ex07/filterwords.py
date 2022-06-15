import sys
import string

if len(sys.argv) == 3 and isinstance(sys.argv[1], str) and sys.argv[2].isnumeric():
    number = int(sys.argv[2])
    str = sys.argv[1]
    split = str.split(" ")
    list = []
    for word in split:
        if not word in string.punctuation and len(word) > number:
            list += [word]
    print(list)
else:
    print("ERROR")
    exit()

#Comment verifier que 300 n'est pas une string ?