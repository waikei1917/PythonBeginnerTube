fishes = {'Salmon':'fuck', 'Tuna':'crack', 'Gar':'smells'}

print(fishes)
print(fishes['Salmon'])
print(fishes['Tuna'])
print('\n')

for k, v in fishes.items():
    print(k + ' ' + v)

print('\n')

for s,r in fishes.items():
    print(s + ' ' + r)

for a in fishes.items():
    print(a)

