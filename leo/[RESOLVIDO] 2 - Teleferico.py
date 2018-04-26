#1min 49s

limit = int(input(""))
n_of_students = int(input(""))

trips = 0

while n_of_students > 0:
    n_of_students -= limit - 1
    trips += 1

print(str(trips))