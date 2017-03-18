numberTaken = [2,5,12,13,15]

print("Here are the numbers still available")

for n in range(1, 20):
    if n in numberTaken:
        continue #skip this round
    print(n)

