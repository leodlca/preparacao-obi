nPos = int(input(""))
dPos = int(input(""))
aPos = int(input(""))

pressCont = 0

if dPos > aPos:
    for i in range(aPos, dPos):
        pressCont += 1
elif dPos < aPos:
    for i in range(aPos, nPos):
        pressCont += 1
    for i in range(0, dPos):
        pressCont += 1

print(pressCont)