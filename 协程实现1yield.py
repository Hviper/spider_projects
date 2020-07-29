def run1():
    yield 1
    yield  run2()
    yield 2
    yield run2()

def run2():
    yield 3
    yield run1()
    yield 4


a = run1()
for i in a:
    if i in [1,2]:
        print(i)
    else:
        print(next(i))