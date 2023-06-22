def f():
    x = 42
    print('local:', x)

    print(locals())
    print(globals())

x = 666
f()
print('global:', x)
