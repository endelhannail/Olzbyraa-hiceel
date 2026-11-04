# task_1
# arr = [5, 2, 8, 1, 4]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
# print(arr)
# task_2
# arr = [8, 3, 6, 1, 7, 2]
# for i in range(3):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
# print(arr)
# task_3
# arr = [4, 9, 1, 7, 3]
# for i in range(len(arr)):
#     max_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] > arr[max_index]:
#             max_index = j
#     temp = arr[i]
#     arr[i] = arr[max_index]
#     arr[max_index] = temp
# print(arr)
# task_4
# arr = [3, -2, 7, -5, 1]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
# print(arr)
# task_5
# arr = [4, 2, 4, 1, 2, 3]
# unique = []
# for i in range(len(arr)):
#     if arr[i] not in unique:
#         unique.append(arr[i])
# for i in range(len(unique)):
#     min_index = i
#     for j in range(i + 1, len(unique)):
#         if unique[j] < unique[min_index]:
#             min_index = j
#     temp = unique[i]
#     unique[i] = unique[min_index]
#     unique[min_index] = temp
# print(unique)
# task_6
# arr = [8, 5, 3, 9, 2]
# min_index = 0
# for j in range(1, len(arr)):
#     if arr[j] < arr[min_index]:
#         min_index = j
# temp = arr[0]
# arr[0] = arr[min_index]
# arr[min_index] = temp
# print(arr)
# task_7
# arr = [7, 4, 9, 2, 5]
# min_index = 0
# for j in range(1, len(arr)):
#     if arr[j] < arr[min_index]:
#         min_index = j
# temp = arr[0]
# arr[0] = arr[min_index]
# arr[min_index] = temp
# print(arr)
# task_8
# arr = [6, 3, 8, 1, 5]
# for i in range(2):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
#     print(arr)
# task_9
# arr = [4, 1, 3, 2]
# count = 0
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     if min_index != i:
#         temp = arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index] = temp
#         count += 1
# print(count)
# task_10
# a = [2, 4, 1, 5, 3]
# b = [1, 2, 3, 4, 5]
# c = [3, 1, 2, 5, 4]
# for i in range(len(b) - 1):
#     if b[i] > b[i + 1]:
#         print("Эрэмбэлэгдээгүй")
#         break
# else:
#     print("b жагсаалт эрэмбэлэгдсэн")
# task_11
# def selection_sort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         temp = arr[i]
#         arr[i] = arr[min_index]
#         arr[min_index] = temp
#     return arr
# arr = [5, 2, 8, 1, 4]
# print(selection_sort(arr))
# task_12
# def selection_sort_desc(arr):
#     for i in range(len(arr)):
#         max_index = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] > arr[max_index]:
#                 max_index = j
#         temp = arr[i]
#         arr[i] = arr[max_index]
#         arr[max_index] = temp
#     return arr
# arr = [5, 2, 8, 1, 4]
# print(selection_sort_desc(arr))
# task_13
# arr = [8, 6, 3, 9, 4]
# min_index = 0
# for j in range(1, len(arr)):
#     if arr[j] < arr[min_index]:
#         min_index = j
# print(min_index)
# task_14
# arr = [5, 3, 4, 1, 2]
# for i in range(len(arr)):
#     min_index = i
#     for j in range(i + 1, len(arr)):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     temp = arr[i]
#     arr[i] = arr[min_index]
#     arr[min_index] = temp
#     print(arr)
# task_15
# arr1 = [5, 1, 4, 2, 3]
# arr2 = [5, 1, 4, 2, 3]
# for i in range(len(arr1)):
#     for j in range(len(arr1) - 1 - i):
#         if arr1[j] > arr1[j + 1]:
#             temp = arr1[j]
#             arr1[j] = arr1[j + 1]
#             arr1[j + 1] = temp
# for i in range(len(arr2)):
#     min_index = i
#     for j in range(i + 1, len(arr2)):
#         if arr2[j] < arr2[min_index]:
#             min_index = j
#     temp = arr2[i]
#     arr2[i] = arr2[min_index]
#     arr2[min_index] = temp
# print("Bubble Sort:", arr1)
# print("Selection Sort:", arr2)
# if arr1 == arr2:
#     print("Ижил")
# else:
#     print("Өөр")
