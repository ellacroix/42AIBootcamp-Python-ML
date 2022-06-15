def ft_filter(function_to_apply, iterable):
    for i in iterable:
        try:
            if function_to_apply(i):
                yield i
        except TypeError:
            return None


x = [1, 2, 3, 4, 5]
print(filter(lambda dum: not (dum % 2), x))
print(ft_filter(lambda dum: not (dum % 2), x))
print(list(filter(lambda dum: not (dum % 2), x)))
print(list(ft_filter(lambda dum: not (dum % 2), x)))


"""Filter the result of function apply to all elements of the iterable.
Args:
function_to_apply: a function taking an iterable.
iterable: an iterable object (list, tuple, iterator).
Returns:
An iterable.
None if the iterable can not be used by the function.
"""