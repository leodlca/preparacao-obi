# 1min e 49s
# Complexidade linear O(n) (podia ser reduzido a O(1) mas é desnecessário)

limit = int(input(""))
n_of_students = int(input(""))

trips = 0

while n_of_students > 0:
    n_of_students -= limit - 1
    trips += 1

print(str(trips))