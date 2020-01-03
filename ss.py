def foo(i, x):
    x.append(i)
    x.append(i*2)
    return x
for i in range(3):
    y = foo(i, ​[])
print(y)