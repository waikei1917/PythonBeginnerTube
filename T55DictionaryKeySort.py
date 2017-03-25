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