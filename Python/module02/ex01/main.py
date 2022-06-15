def what_are_the_vars(*args, **kwargs):
    count = 0
    object = ObjectC()
    for a in kwargs:
        setattr(object, a, kwargs[a])
    for a in args:
        setattr(object, "var_"+str(count), a)
        count += 1
    return object


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)

#A verifier si les reponses de l'enoncé correspondent bien au main