class Values:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        try:
            if all(isinstance(x, float) for x in value):
                setattr(obj, self.private_name, value)
                return ()
        except TypeError:
            pass
        if isinstance(value, int):
            lst = []
            for f in range(0, value):
                lst.append([float(f)])
            setattr(obj, self.private_name, lst)
            return ()
        elif isinstance(value, range):
            lst = []
            for f in value:
                lst.append([float(f)])
            setattr(obj, self.private_name, lst)
            return ()
        try:
            for lst in value:
                if all(isinstance(x, float) for x in lst):
                    setattr(obj, self.private_name, value)
                    return ()
        except TypeError:
            pass
        print("Not valid values.")


class Vector:
    values = Values()

    def __init__(self, values):
        self.values = values
        try:
            if all(isinstance(x, float) for x in self.values):
                self.shape = (1, len(self.values))
            else:
                self.shape = (len(self.values), 1)
        except TypeError:
            pass

    def T(self):
        v = []
        try:
            if all(isinstance(x, float) for x in self.values):
                for x in self.values:
                    v.append([float(x)])
            else:
                for lst in self.values:
                    v.append(lst[0])
        except TypeError:
            pass
        vec = Vector(v)
        return vec

    def __add__(self, other):
        v = []
        try:
            if all(isinstance(x, float) for x in other.values) and all(isinstance(x, float) for x in self.values):
                for i in range(0, len(self.values)):
                    v.append(float(self.values[i]) + float(other.values[i]))
                return v
            elif all(isinstance(x, float) for x in other.values):
                other = other.T()
            elif all(isinstance(x, float) for x in self.values):
                self = self.T()
        except TypeError:
            pass
        for i in range(0, len(self.values)):
            v.append([float(self.values[i][0]) + float(other.values[i][0])])
        return v

    def __sub__(self, other):
        v = []
        try:
            if all(isinstance(x, float) for x in other.values) and all(isinstance(x, float) for x in self.values):
                for i in range(0, len(self.values)):
                    v.append(float(self.values[i]) - float(other.values[i]))
                return v
            if all(isinstance(x, float) for x in other.values):
                other = other.T()
            elif all(isinstance(x, float) for x in self.values):
                self = self.T()
        except TypeError:
            pass
        for i in range(0, len(self.values)):
            v.append([float(self.values[i][0]) - float(other.values[i][0])])
        return v


# A faire: Les autres operations, les radd,rsub... et dotproduct
v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = Vector([[0.0], [1.0], [2.0], [3.0]])
v3 = Vector(4)
v4 = Vector(range(10, 15))
print("Result ", v1 - v1)
print("Result ", v2 - v2)
print("Result ", v1 + v1)
print("Result ", v2 + v2)
