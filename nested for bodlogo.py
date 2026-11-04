# task_1
# n = int(input())
# m = int(input())
# for i in range(1, n + 1):
#     total = 0
#     for j in range(1, m + 1):
#         score = int(input())
#         total += score
#     average = total / m
#     if average >= 60:
#         result = "Тэнцсэн"
#     else:
#         result = "Тэнцээгүй"
#     print(f"{i}-р сурагч: нийт {total}, дундаж {average} {result}")
# task_2
# n = int(input())

# for i in range(1, n + 1):
#     m = int(input())
#     total = 0
#     for j in range(1, m + 1):
#         price = int(input())
#         count = int(input())
#         total += price * count
#     money = int(input())
#     print(f"{i}-р хүний төлөх дүн: {total}")
#     if money >= total:
#         print(f"Хариулт: {money - total}")
#     else:
#         print(f"Дутуу мөнгө: {total - money}")
# task_3
# n = int(input())

# for i in range(1, n + 1):
#     salary = 0
#     for j in range(1, 6):
#         hours = int(input())
#         if hours <= 8:
#             salary += hours * 5000
#         else:
#             salary += 8 * 5000 + (hours - 8) * 7500
#     print(f"{i}-р ажилчны нийт цалин: {salary}")
# task_4
# n, m = map(int, input().split())

# for i in range(1, n + 1):
#     debt = int(input())
#     total = 0
#     for j in range(1, m + 1):
#         payment = int(input())
#         debt -= payment
#         total += payment
#         print(f"{i}-р хүн, {j}-р сарын дараах үлдэгдэл: {debt}")
#     print(f"Нийт төлсөн: {total}")
# task_5
# n, m = map(int, input().split())

# for i in range(1, n + 1):
#     total = 0
#     for j in range(1, m + 1):
#         product = int(input())
#         total += product
#     print(f"{i}-р өдөр: нийт {total}, бүтэн хайрцаг {total // 12}, үлдэгдэл {total % 12}")
# task_6
# n, m = map(int, input().split())

# for i in range(1, n + 1):
#     passengers = 0
#     total = 0
#     for j in range(1, m + 1):
#         off = int(input())
#         on = int(input())
#         passengers = passengers - off + on
#         total += on
#         print(f"{i}-р аяллын {j}-р буудлын дараа: {passengers} хүн")
#     print(f"{i}-р аялалд нийт суусан: {total}")
#     print(f"Аяллын орлого: {total * 1000}")
# task_7
# n = int(input())

# for i in range(1, n + 1):
#     count = 0
#     total = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#             total += j
#     print(f"{i}: {count} хуваагчтай, нийлбэр {total}")
# task_8
# n = int(input())
# count = 0

# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         if i + j == n:
#             print(f"{i} + {j} = {n}")
#             count += 1

# print(f"Нийт: {count} хос")
# task_9
# n = int(input())
# count = 0

# for i in range(n // 2000, -1, -1):
#     for j in range(n // 1000 + 1):
#         if i * 2000 + j * 1000 == n:
#             print(f"1000₮: {j} ширхэг, 2000₮: {i} ширхэг")
#             count += 1

# print(f"Нийт: {count} хувилбар")
# task_10
# n = int(input())
# count = 0

# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         if i * j == n:
#             print(f"{i} x {j} = {n}, ялгавар {j - i}")
#             count += 1

# print(f"Нийт: {count} хос")