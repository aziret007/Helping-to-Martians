import random

array = range(7)
location = random.sample(array, k=3)
weight = 713

while True:
    print(location)
    enterLocation= list(map(int, input('Enter the location 3 numbers with space: ').split()))
    enterWeight = sum(list(map(int, input('Enter the weight 3 numbers with space: ').split())))
    if location == enterLocation and weight == enterWeight:
        print('u won my brother')
        break
    else:
        print('Wrong')
        location = random.sample(a, k=3)