# task_1
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     left = []
#     right = []
#     for i in range(1, len(arr)):
#         if arr[i] < pivot:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
#     return quick_sort(left) + [pivot] + quick_sort(right)
# numbers = [8, 3, 1, 7, 4]
# print(quick_sort(numbers))
# task_2
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     left = []
#     right = []
#     for i in range(1, len(arr)):
#         if arr[i] > pivot:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
#     return quick_sort(left) + [pivot] + quick_sort(right)
# numbers = [5, 2, 9, 1, 7]
# print(quick_sort(numbers))
# task_3
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     left = []
#     right = []
#     for i in range(1, len(arr)):
#         if arr[i] < pivot:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
#     return quick_sort(left) + [pivot] + quick_sort(right)
# numbers = [4, 2, 4, 1, 2, 3, 1]
# print(quick_sort(numbers))
# task_4
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     left = []
#     right = []
#     for i in range(1, len(arr)):
#         if arr[i] < pivot:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
#     return quick_sort(left) + [pivot] + quick_sort(right)
# numbers = [3, -5, 0, 8, -2, 1]
# print(quick_sort(numbers))
# task_5
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     left = []
#     right = []
#     for i in range(1, len(arr)):
#         if arr[i] < pivot:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
#     return quick_sort(left) + [pivot] + quick_sort(right)
# numbers = [9, 2, 7, 1, 5, 3]
# numbers = quick_sort(numbers)
# print(numbers[:3])
# task_6
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     left = []
#     right = []
#     for i in range(1, len(arr)):
#         if arr[i] < pivot:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
#     return quick_sort(left) + [pivot] + quick_sort(right)
# numbers = [4, 9, 1, 7, 3, 8]
# numbers = quick_sort(numbers)
# print(numbers[-1:-3:-1])
# task_7
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     left = []
#     right = []
#     for i in range(1, len(arr)):
#         if arr[i][1] < pivot[1]:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
#     return quick_sort(left) + [pivot] + quick_sort(right)
# students = [("Bat", 85), ("Bold", 70), ("Saraa", 95), ("Anu", 60)]
# print(quick_sort(students))
# task_8
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     left = []
#     right = []
#     for i in range(1, len(arr)):
#         if len(arr[i]) < len(pivot):
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
#     return quick_sort(left) + [pivot] + quick_sort(right)
# words = ["banana", "cat", "apple", "hi", "dog"]
# print(quick_sort(words))
# task_9
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     left = []
#     right = []
#     for i in range(1, len(arr)):
#         if arr[i] < pivot:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
#     return quick_sort(left) + [pivot] + quick_sort(right)
# numbers = [7, 1, 5, 3, 9]
# numbers = quick_sort(numbers)
# n = len(numbers)
# if n % 2 == 1:
#     print(numbers[n // 2])
# else:
#     print((numbers[n // 2 - 1] + numbers[n // 2]) / 2)
# task_10
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[0]
#     left = []
#     right = []
#     for i in range(1, len(arr)):
#         if arr[i] < pivot:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
#     return quick_sort(left) + [pivot] + quick_sort(right)
# a = [8, 3, 5]
# b = [2, 9, 1]
# numbers = a + b
# print(quick_sort(numbers))