def curry(func, max_args):
    if max_args <= 0:
        raise ValueError('max_args must be a positive integer')

    def arg(*args):
        if len(args) == max_args:
            return func(*args)

        def new_arg(*new_args):
            return arg(*(args + new_args))

        return new_arg

    return arg


def uncurry(curried_func, max_args):
    def uncurry_next(*args):
        current_func = curried_func
        for arg in args:
            current_func = current_func(arg)

        return current_func

    return uncurry_next


def f4(x, y, z, t):
    return x + y + z + t


f_curry = curry(f4, 4)
f_uncurry = uncurry(f_curry, 4)
print(f_curry(3)(4)(5)(6))
print(f_uncurry(3, 4, 5, 6))
