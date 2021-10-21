nums = (input('Please enter nums: '))
Sum = 0
numbers = []
for digit in nums:
    Sum += int(digit) ** len(nums)
    numbers.append(int(digit))
if Sum == int(nums):
    print('Yes')
    for i in range(len(numbers)):
        print(numbers[i], '^', len(nums), end=' ')
        if i < len(numbers) - 1:
            print('+', end=' ')
    print('=', Sum)
else:
    print('No')