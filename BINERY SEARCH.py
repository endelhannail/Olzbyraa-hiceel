# task_1
# numbers = [3, 7, 12, 18, 25, 31, 40]
# target = int(input())
# left = 0
# right = len(numbers) - 1
# found = False
# while left <= right:
#     mid = (left + right) // 2
#     if numbers[mid] == target:
#         found = True
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# if found:
#     print("Олдлоо")
# else:
#     print("Олдсонгүй")
# task_2
# numbers = [5, 10, 15, 20, 25, 30]
# target = int(input())
# left = 0
# right = len(numbers) - 1
# index = -1
# while left <= right:
#     mid = (left + right) // 2
#     if numbers[mid] == target:
#         index = mid
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# print(index)
# task_3
# numbers = [4, 9, 14, 19, 24, 29, 34]
# target = 4
# left = 0
# right = len(numbers) - 1
# while left <= right:
#     mid = (left + right) // 2
#     if numbers[mid] == target:
#         print(mid)
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# task_4
# numbers = [6, 12, 18, 24, 30, 36, 42]
# target = 42
# left = 0
# right = len(numbers) - 1
# while left <= right:
#     mid = (left + right) // 2
#     if numbers[mid] == target:
#         print(mid)
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# task_5
# numbers = [10, 20, 30, 40, 50, 60]
# target = int(input())
# left = 0
# right = len(numbers) - 1
# found = False
# while left <= right:
#     mid = (left + right) // 2
#     if numbers[mid] == target:
#         found = True
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# if found:
#     print("Олдлоо")
# else:
#     print("Хайж буй тоо байхгүй")
# task_6
# numbers = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32]
# target = int(input())
# left = 0
# right = len(numbers) - 1
# count = 0
# while left <= right:
#     mid = (left + right) // 2
#     count += 1
#     if numbers[mid] == target:
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# print(count)
# task_7
# scores = [45, 50, 58, 65, 72, 80, 88, 95]
# target = int(input())
# left = 0
# right = len(scores) - 1
# index = -1
# while left <= right:
#     mid = (left + right) // 2
#     if scores[mid] == target:
#         index = mid
#         break
#     elif scores[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# if index != -1:
#     print(index)
# else:
#     print(-1)
# task_8
# codes = [101, 105, 112, 120, 135, 148, 160, 175]
# target = int(input())
# left = 0
# right = len(codes) - 1
# found = False
# while left <= right:
#     mid = (left + right) // 2
#     if codes[mid] == target:
#         found = True
#         break
#     elif codes[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# if found:
#     print("Бараа бүртгэлтэй")
# else:
#     print("Бараа бүртгэлгүй")
# task_9
# book_ids = [1002, 1015, 1028, 1040, 1055, 1072, 1090]
# target = int(input())
# left = 0
# right = len(book_ids) - 1
# index = -1
# while left <= right:
#     mid = (left + right) // 2
#     if book_ids[mid] == target:
#         index = mid
#         break
#     elif book_ids[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# print(index)
# task_10
# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# target = int(input())
# left = 0
# right = len(numbers) - 1
# index = -1
# while left <= right:
#     mid = (left + right) // 2
#     print("left:", left, "right:", right, "mid:", mid)
#     if numbers[mid] == target:
#         index = mid
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# if index != -1:
#     print(index)
# else:
#     print("Олдсонгүй")
# task_11
# numbers = [2, 4, 4, 4, 6, 8, 10, 10]
# target = int(input())
# left = 0
# right = len(numbers) - 1
# index = -1
# while left <= right:
#     mid = (left + right) // 2
#     if numbers[mid] == target:
#         index = mid
#         right = mid - 1
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# print(index)
# task_12
# numbers = [1, 3, 3, 3, 5, 7, 7, 9]
# target = int(input())
# left = 0
# right = len(numbers) - 1
# index = -1
# while left <= right:
#     mid = (left + right) // 2
#     if numbers[mid] == target:
#         index = mid
#         left = mid + 1
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# print(index)
# task_13
# numbers = [10, 20, 30, 40, 50, 60]
# target = int(input())
# left = 0
# right = len(numbers)
# while left < right:
#     mid = (left + right) // 2
#     if numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid
# print(left)
# task_14
# numbers = [5, 12, 19, 26, 33, 40, 47]
# target = int(input())
# left = 0
# right = len(numbers) - 1
# answer = -1
# while left <= right:
#     mid = (left + right) // 2
#     if numbers[mid] < target:
#         answer = numbers[mid]
#         left = mid + 1
#     else:
#         right = mid - 1
# if answer == -1:
#     print("Байхгүй")
# else:
#     print(answer)
# task_15
# numbers = [5, 12, 19, 26, 33, 40, 47]
# target = int(input())
# left = 0
# right = len(numbers) - 1
# answer = -1
# while left <= right:
#     mid = (left + right) // 2
#     if numbers[mid] > target:
#         answer = numbers[mid]
#         right = mid - 1
#     else:
#         left = mid + 1
# if answer == -1:
#     print("Байхгүй")
# else:
#     print(answer)
# task_16
# numbers = [3, 8, 13, 18, 23, 28, 33, 38, 43]
# a = int(input())
# b = int(input())
# for target in [a, b]:
#     left = 0
#     right = len(numbers) - 1
#     index = -1
#     while left <= right:
#         mid = (left + right) // 2
#         if numbers[mid] == target:
#             index = mid
#             break
#         elif numbers[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     print(index)
# task_17
# numbers = [95, 82, 70, 61, 49, 35, 20, 11]
# target = int(input())
# left = 0
# right = len(numbers) - 1
# index = -1
# while left <= right:
#     mid = (left + right) // 2
#     if numbers[mid] == target:
#         index = mid
#         break
#     elif numbers[mid] > target:
#         left = mid + 1
#     else:
#         right = mid - 1
# print(index)
# task_18
# def binary_search(numbers, target):
#     left = 0
#     right = len(numbers) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if numbers[mid] == target:
#             return mid
#         elif numbers[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# numbers = [3, 7, 12, 18, 25, 31, 40]
# target = int(input())
# print(binary_search(numbers, target))
# task_19
# numbers = [1, 2, 2, 2, 2, 4, 5, 5, 7, 8]
# target = int(input())
# left = 0
# right = len(numbers) - 1
# first = -1
# while left <= right:
#     mid = (left + right) // 2
#     if numbers[mid] == target:
#         first = mid
#         right = mid - 1
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# left = 0
# right = len(numbers) - 1
# last = -1
# while left <= right:
#     mid = (left + right) // 2
#     if numbers[mid] == target:
#         last = mid
#         left = mid + 1
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# if first == -1:
#     print(0)
# else:
#     print(last - first + 1)
# task_20
# numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
# target = 38
# count = 0
# for i in range(len(numbers)):
#     count += 1
#     if numbers[i] == target:
#         print("Linear Search:", i)
#         print("Алхам:", count)
#         break
# left = 0
# right = len(numbers) - 1
# count = 0
# while left <= right:
#     mid = (left + right) // 2
#     count += 1
#     if numbers[mid] == target:
#         print("Binary Search:", mid)
#         print("Алхам:", count)
#         break
#     elif numbers[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
