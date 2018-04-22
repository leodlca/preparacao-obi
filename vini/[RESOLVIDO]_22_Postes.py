nPostes = input("")
tamPostes = input("").split(" ")

tamPostesInt = []
subPostes = 0
fixPostes = 0


for i in tamPostes:
    tamPostesInt.append(int(i))

for i in tamPostesInt:
    if i < 50:
        subPostes += 1
    elif i >= 50 and i < 85:
        fixPostes += 1

print(str(subPostes) + " " + str(fixPostes))
