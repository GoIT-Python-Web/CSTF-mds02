import ast

code = "print('Hello, World!')"

tree = ast.parse(code)
result = ast.dump(tree, annotate_fields=False)
print(result)

with open("test.py", 'r', encoding="utf-8") as f:
    code = f.read()
    tree = ast.parse(code)
    exec(compile(tree, filename='test.py', mode='exec'))
