n1 = abs(int(input('Please enter your first Number: ')))
n2 = abs(int(input('Please enter your second Number: ')))
while n1 == 0 or n2 == 0:
    print('Please enter correct numbers for both (0 is forbidden)')
    n1 = abs(int(input('Please enter your first Number: ')))
    n2 = abs(int(input('Please enter your second Number: ')))
lcm_result = 0
bigger_n = max(n1, n2)
for i in range(bigger_n, n1 * n2 + 1):
    if (i % n1 == 0) and (i % n2 == 0):
        lcm_result = i
        break
print('Their LCM should be : ', lcm_result)