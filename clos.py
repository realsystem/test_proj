def f(x):
    def f1(y):
        return x+y
    return f1
F=f(1)
FF=f(2)
print F(1)
print FF(1)
