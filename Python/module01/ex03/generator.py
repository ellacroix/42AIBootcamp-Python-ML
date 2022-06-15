import random

def generator(text, sep=" ", option=None):
    if not isinstance(text, str) or option not in ["shuffle", "ordered", "unique", None]:
        print("ERROR")
        return "ERROR"
    rand = []
    lst = text.split(sep)
    if option is None:
        for w in lst:
            yield w
    elif option == "shuffle":
        rand = random.sample(range(0, len(lst)), len(lst))
        for i in range(0, len(lst)):
            yield lst[rand[i]]
    elif option == "ordered":
        lst.sort()
        for w in lst:
            yield w
    elif option == "unique":
        printed = []
        for w in lst:
            if w in printed:
                pass
            else:
                yield w
            printed.append(w)


text = "Le Lorem Ipsum est est simplement du faux texte Lorem Lorem."
error = (12, 65)
for word in generator(text, sep=" ", option="shuffle"):
    print(word)
