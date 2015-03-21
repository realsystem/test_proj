def my_gen(x):
    i=0
    while i<x:
        yield i
        i+=1
for i in my_gen(5):
    print i
