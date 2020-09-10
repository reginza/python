def my_func(x, y):
    c = x ** y
    return c


print(my_func(4, -5))


def my_func2(x, y):
    z = 1
    for i in range(abs(y)):
        z *= x
    return 1 / z


out2 = my_func2(2, -2)
print(out2)
