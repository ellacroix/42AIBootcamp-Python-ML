import numpy as np

class NumPyCreator():
    
    def from_list(self, lst):
        return np.array(lst)
    
    def from_tuple(self, tpl):
        return np.array(tpl)
    
    def from_iterable(self, itr):
        return np.array(itr)

    def from_shape(self, tpl, val=0):
        return np.full(tpl, val)

    def random(self, tpl):
        return np.random.random(tpl)

    def identity(self, n):
        return np.identity(n)


npc = NumPyCreator()
print(npc.from_list([[1,2,3],[6,3,4]]))
print(npc.from_list([[1,2,3],['a','b','c'],[6.0,4.1,7.2]]))
shape=(3,5)
print(npc.from_shape(shape))
print(npc.random(shape))
print(npc.identity(4))