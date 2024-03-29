x = 10
stmt = "x**2 + 2 * x + 1"
stmt2 = "x + 5"
result = eval(stmt, globals(), locals())
print(result)
result2 = eval(stmt2)
print(result2)
print(locals())
print(globals())


def bax():
    test = 100
    print(locals())
    print(globals())


bax()
