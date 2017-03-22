item = ['Dec 25, 2015', 'bread', 8.51]
print(item[0])

date, name, price = ['Dec 25, 2015', 'bread', 8.51]
print(name)

def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle)/len(middle)
    print(avg)

drop_first_last([65,76,98,54,21])
drop_first_last([65,76,98,54,21,54,65,99,88,78])

print(30*'=')

def foo(*args, **kwargs):
    for item in args:
        print(item)

    for k,v in kwargs.items():
        print(k,v)

    print(30*'=')

foo(1,2,3)
foo(1,2,3,a=4,b=5)
foo(2,3,a=4,b=5,c=1)

v = (1,2,3)
v2 = [11,15,23]
d = {'a':1, 'b':12}

foo(v)
foo(v,v2)
foo(*v)
foo(*v2)
foo(d)
foo(*d)

foo(v,d)
foo(*v,*d)
foo(*v, **d)
foo(*v2)

