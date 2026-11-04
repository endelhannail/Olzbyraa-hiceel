# task_1
# for i in range(1, 11):
#     print(i)
# task_2
# for i in range(2, 21, 2):
#     print(i)
# task_3
# for i in range(1, 21, 2):
#     print(i)
# task_4
# for i in range(1, 11):
#     print("5 x", i, "=", 5 * i)
# task_5
# n = int(input())
# for i in range(1, n + 1):
#     print(i)
# task_6
# n = int(input())
# for i in range(n, 0, -1):
#     print(i)
# task_7
# for i in range(1, 51):
#     if i % 3 == 0:
#         print(i)
# task_8
# for i in range(1, 31):
#     if i % 5 != 0:
#         print(i)
# task_9
# count = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         count = count + 1
# print(count)
# task_10
# count = 0
# for i in range(1, 101):
#     if i % 7 == 0:
#         count = count + 1
# print(count)
# task_11
# total = 0
# for i in range(1, 101):
#     total = total + i
# print(total)
# task_12
# total = 0
# for i in range(2, 51, 2):
#     total = total + i
# print(total)
# task_13
# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1
# task_14
# i = 10
# while i >= 1:
#     print(i)
#     i = i - 1
# task_15
# i = 2
# while i <= 20:
#     print(i)
#     i = i + 2
# task_16
# n = int(input())
# i = 1
# total = 0
# while i <= n:
#     total = total + i
#     i = i + 1
# print(total)
# task_17
# n = int(input())
# count = 0
# while n > 0:
#     count = count + 1
#     n = n // 10
# print(count)
# task_18
# n = int(input())
# total = 0
# while n > 0:
#     total = total + n % 10
#     n = n // 10
# print(total)
# task_19
# for i in range(1, 21):
#     if i == 5:
#         break
#     print(i)
# task_20
# for i in range(10, 101):
#     if i % 7 == 0:
#         print(i)
#         break
# task_21
# secret = 8
# while True:
#     n = int(input())
#     if n == secret:
#         break
# task_22
# while True:
#     n = int(input())
#     if n == 0:
#         break
# task_23
# total = 0
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     total = total + n
# print(total)
# task_24
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)
# task_25
# for i in range(1, 21):
#     if i % 2 == 0:
#         continue
#     print(i)
# task_26
# for i in range(1, 31):
#     if i % 3 == 0:
#         continue
#     print(i)
# task_27
# total = 0
# for i in range(5):
#     n = int(input())
#     if n < 0:
#         continue
#     total = total + n
# print(total)
# task_28
# count = 0
# i = 1
# while True:
#     if i % 7 == 0:
#         print(i)
#         count = count + 1
#     if count == 5:
#         break
#     i = i + 1
# task_29
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     if n < 0:
#         continue
#     if n % 2 != 0:
#         continue
#     print(n)
# task_30
# secret = 17
# while True:
#     n = int(input())
#     if n < 0:
#         print("sorog too oruulahgui")
#         continue
#     if n < secret:
#         print("baga bn")
#     elif n > secret:
#         print("ih bn")
#     else:
#         print("zov taalaa")
#         break

##############################################################################

# bodlogo_1
# davhar, orts, haalga = map(int, input().split())
# n = int(input())
# neg_orts = davhar * haalga
# ortsiin_dugaar = (n - 1) // neg_orts + 1
# davhriin_dugaar = ((n - 1) % neg_orts) // haalga + 1
# haalgiin_dugaar = (n - 1) % haalga + 1
# print(ortsiin_dugaar, davhriin_dugaar, haalgiin_dugaar)