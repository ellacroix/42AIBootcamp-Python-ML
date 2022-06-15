import sys
import string

def text_analyzer(*args):
    if len(args) == 0:
        text = str(input("What is the text to analyse?\n"))
    elif len(args) > 1:
        print("ERROR")
        exit()
    else:
        text = args[0]
    if text == "":
        print("Text is empty.")
    else:
        print("The text contains", len(text), "characters:")
        print("-", sum(c.isupper() for c in text), "upper letters")
        print("-", sum(c.islower() for c in text), "lower letters")
        print("-", sum(c in string.punctuation for c in text), "punctuation marks")
        print("-", sum(c.isspace() for c in text), "spaces")
