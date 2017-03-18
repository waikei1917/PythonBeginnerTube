colours = {'blue','red','black','white','orange','pink','red'}
print(colours)

if 'black' in colours:
    print('you have black')
else:
    print('you dont have black')

x = set('spam')
y = set(['h','y','s','m'])
print(x,y)

print(x&y)
print(x|y)
print(x-y)

a = [22,33,5,42,6,22]
b = set(a)
print(b)
c = [i for i in b]
print(c)

print(b)
b.add('h')
b.update([12,34,78,54,32])
print(b)
