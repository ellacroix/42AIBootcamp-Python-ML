from functools import reduce

def ft_reduce(function_to_apply, iterable):
    result = iterable[0]
    for i in range(0, len(iterable) - 1):
        try:
            result = function_to_apply(result, iterable[i+1])
        except TypeError:
            return None
    return result

lst = ['H', 'e', 'l', 'l', 'o', ' ',  'W']
num = [1, 2, 3, 4]
print(reduce(lambda u, v: u + v, lst))
print(ft_reduce(lambda u, v: u + v, lst))
print(reduce(lambda u, v: u + v, num))
print(ft_reduce(lambda u, v: u + v, num))

"""Apply function of two arguments cumulatively.
Args:
function_to_apply: a function taking an iterable.
iterable: an iterable object (list, tuple, iterator).
Returns:
A value, of same type of elements in the iterable parameter.
None if the iterable can not be used by the function.
"""