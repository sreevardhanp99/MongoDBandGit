def update(x):
    print(id(x))
    x = 8
    print(x)
    print(id(x))

a = 10
print(id(a))
print(a)
update(a)