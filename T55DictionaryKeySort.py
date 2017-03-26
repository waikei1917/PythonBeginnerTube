from operator import itemgetter

users =[
    {'fname':'Bucky','lname':'Roberts'},
    {'fname':'Tom','lname':'Roberts'},
    {'fname':'Bernie','lname':'Zunks'},
    {'fname':'Jenna','lname':'Roberts'},
    {'fname':'Sally','lname':'Hayes'},
    {'fname':'Amanda','lname':'Jones'},
    {'fname':'Tom','lname':'Roberts'},
    {'fname':'Dean','lname':'Williams'},
    {'fname':'Bernie','lname':'Barbie'},
    {'fname':'Tom','lname':'Jones'},
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

print(30*'=')

for x in sorted(users, key=itemgetter('lname')):
    print(x)
    
print(30*'=')

for x in sorted(users,key=itemgetter('fname','lname')):
    print(x)

print(30*'=')

a = [1,2,3]
b = itemgetter(1)
print(b(a))
b = itemgetter(1,0)
print(b(a))
#要注意，operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值。

print(30*'=')

students = [('john','A',15),('jane','B',12),('dave','B',10)]
print(sorted(students,key=lambda student:student[2]))
