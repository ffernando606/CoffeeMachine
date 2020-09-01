def closest_higher_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        y = abs((x % 5) - 5)
        return x + y

