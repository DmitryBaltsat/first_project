# nums = [987, 18567, 15, 34, 23, 43, 13, 54, 768, 99, 1024, 547, 1, 5617, 1567]
# max_one = 0
# max_two = 0
#
# for num in range(len(nums)):
#     if nums[num] > max_one:
#         max_two = max_one
#         max_one = nums[num]
#         #max_two = temp
#     elif nums[num] > max_two:
#         max_two = nums[num]
# print(max_one, max_two)
# print((len(nums)))
# print(nums[int(len(nums)/2)])


# n = input()
# # a = '9'
# # c = str(9 - int(n))
# # print(f'{n}{a}{c}')

# numbers = [56, 5, 1, 26, 7, 6, 4]
# max = 0
# for num in range(len(numbers)):
#     if numbers[num] > max:
#         max = numbers[num]
# for num in range(len(numbers)):
#     if numbers[num] == max:
#         temp = numbers[num]
#         numbers[num] = numbers[len(numbers) - 1]
#         numbers[len(numbers) - 1] = temp
#
# print(numbers)

numbers = [2, 5, 13, 7, 6, 4]
sum = 0
count = 0
while count < len(numbers):
    sum += numbers[count]
    count += 1
result = sum / len(numbers)
print(result)








