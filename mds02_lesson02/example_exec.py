stmt = """
x = 10
result = x**2 + 2 * x + 1
print(result)
"""

exec(stmt)
print(locals())
print(globals())
print(result)  # noqa

x = 100
stmt2 = """
r = x + 4
print(r)
"""


def baz():
    x = 10
    exec(stmt2)
    local = locals()
    print(local["r"])


baz()
