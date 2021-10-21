n1 = abs(int(input('Please enter your first Number: ')))
n2 = abs(int(input('Please enter your second Number: ')))
while n1 == 0 or n2 == 0:
    print('Please enter correct numbers for both (0 is forbidden)')
    n1 = abs(int(input('Please enter your first Number: ')))
    n2 = abs(int(input('Please enter your second Number: ')))
gcd_result = 0
smaller_n = min(n1,n2)
for i in range(1, smaller_n + 1):
    if (n1 % i == 0) and (n2 % i == 0):
        gcd_result = i
print('Their GCD should be : ', gcd_result)