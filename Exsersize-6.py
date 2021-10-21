nums = []
arr_size = abs(int(input('Please enter the number of Array : ')))
while arr_size == 0:
    arr_size = abs(int(input('Please enter the number of Array(it can\'t be zero) : ')))
for i in range(arr_size):
    print('Please enter ', i + 1, 'th number : ', end ='')
    nums.append(int(input()))
sorted = True
prev_num = nums[0]
for number in nums:
    if number < prev_num:
        sorted = False
    prev_num = number
if sorted:
    print('Yes(it\'s sorted array)')
else:
    print('No(it isn\t sorted array)')