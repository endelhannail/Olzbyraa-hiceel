#task_1
# numbers = list(map(int, input().split()))
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers)
# task_2
# numbers = list(map(int, input().split()))
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1):
#         if numbers[j] < numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers)
# task_3
# numbers = list(map(int, input().split()))
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers)
# task_4
# numbers = list(map(int, input().split()))
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers)
# task_5
# numbers = list(map(int, input().split()))
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers)
# task_6
# names = input().split()
# for i in range(len(names)):
#     for j in range(len(names) - 1):
#         if names[j] > names[j + 1]:
#             temp = names[j]
#             names[j] = names[j + 1]
#             names[j + 1] = temp
# print(names)
# task_7
# scores = list(map(int, input().split()))
# for i in range(len(scores)):
#     for j in range(len(scores) - 1):
#         if scores[j] > scores[j + 1]:
#             temp = scores[j]
#             scores[j] = scores[j + 1]
#             scores[j + 1] = temp
# print(scores)
# task_8
# numbers = [6, 2, 9, 1, 5]
# for j in range(len(numbers) - 1):
#     if numbers[j] > numbers[j + 1]:
#         temp = numbers[j]
#         numbers[j] = numbers[j + 1]
#         numbers[j + 1] = temp
# print(numbers)
# task_9
# numbers = list(map(int, input().split()))
# for i in range(len(numbers) - 1):
#     for j in range(len(numbers) - 1):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(len(numbers) - 1)
# print(numbers)
# task_10
# numbers = list(map(int, input().split()))
# swap_count = 0
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
#             swap_count += 1
# print(numbers)
# print(swap_count)
# task_11
# numbers = list(map(int, input().split()))
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1):
#         if numbers[j] < numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers[1])
# task_12
# numbers = list(map(int, input().split()))
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1):
#         if numbers[j] < numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers[1])
# task_13
# numbers = list(map(int, input().split()))
# for i in range(len(numbers) - 1):
#     for j in range(len(numbers) - 1):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
#     print(numbers)
# print("Эцсийн жагсаалт:", numbers)
# task_14
# numbers = list(map(int, input().split()))
# for i in range(len(numbers) - 1):
#     swap = False
#     for j in range(len(numbers) - 1):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
#             swap = True
#     if swap == False:
#         break
# print(numbers)
# task_15
# numbers = [1, 2, 3, 5, 4]
# round_count = 0
# for i in range(len(numbers) - 1):
#     swap = False
#     round_count += 1
#     for j in range(len(numbers) - 1):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
#             swap = True
#     if swap == False:
#         break
# print(numbers)
# print("Зөв эрэмбэлэгдсэн:", numbers == sorted(numbers))
# print("Тойргийн тоо:", round_count)
# task_16
# n = int(input())
# students = []
# for i in range(n):
#     name = input()
#     score = int(input())
#     students.append([name, score])
# for i in range(len(students)):
#     for j in range(len(students) - 1):
#         if students[j][1] > students[j + 1][1]:
#             temp = students[j]
#             students[j] = students[j + 1]
#             students[j + 1] = temp
# print(students)
# task_17
# n = int(input())
# people = []
# for i in range(n):
#     name = input()
#     age = int(input())
#     people.append([name, age])
# for i in range(len(people)):
#     for j in range(len(people) - 1):
#         if people[j][1] > people[j + 1][1]:
#             temp = people[j]
#             people[j] = people[j + 1]
#             people[j + 1] = temp
# print(people)
# print(people[0][0])
# print(people[n - 1][0])
# task_18
# numbers = [4, 2, 4, 1, 2, 4, 3]
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# count = 0
# for num in numbers:
#     if num == 4:
#         count += 1
# print(numbers, "4 too", count, "udaa bn.")
# task_19
# n = int(input())
# products = []
# for i in range(n):
#     name = input()
#     price = int(input())
#     products.append([name, price])
# for i in range(len(products)):
#     for j in range(len(products) - 1):
#         if products[j][1] < products[j + 1][1]:
#             temp = products[j]
#             products[j] = products[j + 1]
#             products[j + 1] = temp
# for i in range(3):
#     print(products[i][0], products[i][1])
# task_20
# n = int(input())
# numbers = list(map(int, input().split()))
# compare = 0
# swap = 0
# rounds = 0
# for i in range(n - 1):
#     rounds += 1
#     for j in range(n - 1):
#         compare += 1
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
#             swap += 1
# print("Compare:", compare)
# print("Swap:", swap)
# print("Rounds:", rounds)
# print("Final List:", numbers)
# task_21
# numbers = [7, 4, 9, 2, 6, 1, 8, 3]
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers)
# task_22
# words = ["apple", "hi", "banana", "cat", "python"]
# for i in range(len(words)):
#     for j in range(len(words) - 1 - i):
#         if len(words[j]) > len(words[j + 1]):
#             temp = words[j]
#             words[j] = words[j + 1]
#             words[j + 1] = temp
# print(words)
# task_23
# numbers = [14, 6, 11, 3, 9, 2]
# for j in range(len(numbers) - 1, 0, -1):
#     if numbers[j] < numbers[j - 1]:
#         temp = numbers[j]
#         numbers[j] = numbers[j - 1]
#         numbers[j - 1] = temp
# print(numbers)
# task_24
# numbers = [7, 4, 9, 2, 5, 8, 1, 6]
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1 - i):
#         if numbers[j] % 2 == 1 and numbers[j + 1] % 2 == 0:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers)
# task_25
# a = [8, 3, 6]
# b = [2, 9, 1, 5]
# numbers = a + b
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers)
# task_26
# numbers = [6, 2, 5, 1, 4]
# total = 0
# for i in range(len(numbers) - 1):
#     count = 0
#     for j in range(len(numbers) - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
#             count += 1
#             total += 1
#     print(i + 1, "-р тойрог:", count, "солилцоо")
# print("Нийт солилцоо:", total)
# print(numbers)
# task_27
# numbers = [18, 5, 12, 3, 25, 9, 7]
# for i in range(len(numbers)):
#     for j in range(len(numbers) - 1 - i):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
# print(numbers[2])
# task_28
# students = [["Bat", 85], ["Anu", 92], ["Bold", 85], ["Saraa", 70], ["Temuulen", 92]]
# for i in range(len(students)):
#     for j in range(len(students) - 1 - i):
#         if students[j][1] < students[j + 1][1]:
#             temp = students[j]
#             students[j] = students[j + 1]
#             students[j + 1] = temp
# print(students)
# task_29
# numbers = [3, 1, 4, 2, 5]
# compare_count = 0
# swap_count = 0
# no_swap = False
# for i in range(len(numbers) - 1):
#     swapped = False
#     for j in range(len(numbers) - 1 - i):
#         compare_count += 1
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
#             swap_count += 1
#             swapped = True
#     if swapped == False:
#         no_swap = True
#         break
# print("Харьцуулалт:", compare_count)
# print("Солилцоо:", swap_count)
# print("Солилцоо хийгдээгүй тойрог:", no_swap)
# print(numbers)
# task_30
# products = [["Mouse", 25000, 12], ["Keyboard", 65000, 5], ["USB", 12000, 20], ["Headphone", 65000, 8], ["Webcam", 40000, 3]]
# for i in range(len(products)):
#     for j in range(len(products) - 1 - i):
#         if products[j][1] < products[j + 1][1] or (products[j][1] == products[j + 1][1] and products[j][2] > products[j + 1][2]):
#             temp = products[j]
#             products[j] = products[j + 1]
#             products[j + 1] = temp
# print(products)