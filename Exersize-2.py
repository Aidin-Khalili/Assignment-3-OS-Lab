from random import randint
numbers = []
n = randint(1, 50)
for i in range(n):
    unique_number = randint(0, 100)
    if unique_number not in numbers:
        numbers.append(unique_number)
print('Numbers count is: ', n,'\nThere are : ', numbers)