data = [int(x) for x in input("").split(" ")]

initialState = [x for x in data[0:2]]
finalState = [x for x in data[2:4]]

if finalState[0] == 0 and finalState[1] == 1:
    print('2')
elif finalState[0] == 1 and finalState[1] == 0:
    print('1')
elif finalState[0] == 1 and finalState[1] == 1:
    print('1')
else:
    print('0')