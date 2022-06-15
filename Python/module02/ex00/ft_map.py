def ft_map(function_to_apply, iterable):
    for i in iterable:
        try:
            yield function_to_apply(i)
        except TypeError:
            return None

x = [1, 2, 3, 4, 5]
d = {32: 12, "name": "Arthur"}
a = [1, "a"]
print(map(lambda dum: dum + 1, x))
print(ft_map(lambda dum: dum + 1, x))
print(list(map(lambda dum: dum + 1, x)))
print(list(ft_map(lambda dum: dum + 1, x)))
"""Map the function to all elements of the iterable.
Args:
function_to_apply: a function taking an iterable.
iterable: an iterable object (list, tuple, iterator).
Returns:
An iterable.
None if the iterable can not be used by the function.
"""