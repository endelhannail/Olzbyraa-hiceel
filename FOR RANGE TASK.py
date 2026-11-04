# task_1
# for i in range(5):
#     print("Сайн уу")
# task_2
# for i in range(10):
#     print(i)
# task_3
# for i in range(1, 11):
#     print(i)
# task_4
# for i in range(10, 0, -1):
#     print(i)
# task_5
# name = input()
# for i in range(5):
#     print(name)
# task_6
# sum = 0
# for i in range(1, 11):
#     sum = sum + i
# print(sum)
# task_7
# sum = 0
# for i in range(1, 101):
#     sum = sum + i
# print(sum)
# task_8
# sum = 0
# for i in range(2, 21, 2):
#     sum = sum + i
# print(sum)
# task_9
# sum = 0
# for i in range(3, 31, 3):
#     sum = sum + i
# print(sum)
# task_10
# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     sum = sum + i
# print(sum)
# task_11
# count = 0
# for i in range(1, 21):
#     if i % 2 == 0:
#         count = count + 1
# print(count)
# task_12
# count = 0
# for i in range(1, 101):
#     if i % 5 == 0:
#         count = count + 1
# print(count)
# task_13
# count = 0
# for i in range(1, 51):
#     if i % 3 == 0:
#         count = count + 1
# print(count)
# task_14
# even = 0
# odd = 0
# for i in range(1, 21):
#     if i % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1
# print("Tegsh:", even, "Sondgoi:", odd)
# task_15
# n = int(input())
# count = 0
# for i in range(1, n + 1):
#     if i % 7 == 0:
#         count = count + 1
# print(count)
# task_16
# sum = 0
# count = 0
# for i in range(2, 101, 2):
#     sum = sum + i
#     count = count + 1
# print("Niit:", sum, "Too:", count)
# task_17
# count = 0
# for i in range(1, 101):
#     if i % 3 == 0 or i % 5 == 0:
#         count = count + 1
# print(count)
# task_18
# sum = 0
# for i in range(3, 101, 3):
#     sum = sum + i
# print(sum)
# task_19
# n = int(input())
# sum = 0
# count = 0
# high = 0
# for i in range(n):
#     score = int(input())
#     sum = sum + score
#     count = count + 1
#     if score > 80:
#         high = high + 1
# print("Niit:", sum, "dundaj:", sum / count, "80-aas deesh:", high)
# task_20
# n = int(input())
# best = 0
# for i in range(n):
#     dun = int(input())
#     if dun > best:
#         best = dun
# print("hamgiin ondor:", best)
# task_21
# n = int(input())
# small = 999999
# for i in range(n):
#     too = int(input())
#     if too < small:
#         small = too
# print("hamgiin baga:", small)
# task_22
# n = int(input())
# sum = 0
# while n > 0:
#     sum = sum + n % 10
#     n = n // 10
# print(sum)
# task_23
# n = int(input())
# result = 1
# for i in range(1, n + 1):
#     result = result * i
# print(result)
# task_24
# n = int(input())
# sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum = sum + i
# if sum == n:
#     print("YES")
# else:
#     print("NO")
# task_25
# n = int(input())
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         count = count + 1
# if count == 2:
#     print("YES")
# else:
#     print("NO")
# task_26
# a = 0
# b = 0
# c = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         a = a + 1
#     if i % 3 == 0:
#         b = b + 1
#     if i % 5 == 0:
#         c = c + 1
# print("2t:", a)
# print("3t:", b)
# print("5t:", c)
# task_27
# for i in range(1, 31):
#     if i % 2 == 0:
#         print(i, "2t huvaagdana")
#     else:
#         print(i, "2t huvaagdahgui")
# task_28
# count = 0
# sum = 0
# for i in range(1, 101):
#     if i % 5 == 0:
#         count = count + 1
#         sum = sum + i
# print("too:", count, "niit:", sum)
# task_29
# n = int(input())
# sum = 0
# for i in range(n):
#     too = int(input())
#     sum = sum + too
# print("nillber:", sum)
# print("too shirheg:", n)
# print("dundaj:", sum / n)
# task_30
# n = int(input())
# even = 0
# odd = 0
# even_sum = 0
# odd_sum = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         even = even + 1
#         even_sum = even_sum + i
#     else:
#         odd = odd + 1
#         odd_sum = odd_sum + i
# print("tegsh too:", even)
# print("sondgoi too:", odd)
# print("tegsh nii lb:", even_sum)
# print("sondgoi nii lb:", odd_sum)
# print("hamgiin ih:", n)
# print("hamgiin baga:", 1)

######################################################
# NEMELT 10 BODLOGO
# task_1
# for i in range(10, 51):
#     if i % 3 == 0:
#         print(i)
# task_2
# n = int(input())
# for i in range(2, n + 1, 2):
#     print(i)
# task_3
# sum = 0
# for i in range(1, 51, 2):
#     sum = sum + i
# print(sum)
# task_4
# count = 0
# for i in range(1, 101):
#     if i % 4 == 0:
#         count = count + 1
# print(count)
# task_5
# sum = 0
# for i in range(10):
#     n = int(input())
#     if n > 0:
#         sum = sum + n
# print(sum)
# task_6
# sum = 0
# for i in range(10, 101, 5):
#     sum = sum + i
# print(sum)
# task_7
# n = input()
# sum = 0
# for i in n:
#     sum = sum + int(i)
# print(sum)
# task_8
# count = 0
# for i in range(1, 101):
#     if i % 7 == 0:
#         print(i)
#         count = count + 1
#     if count == 5:
#         break
# task_9
# for i in range(1, 51):
#     if i % 2 == 0:
#         best = i
# print(best)
# task_10
# small = 999999
# for i in range(10):
#     n = int(input())
#     if n > 0 and n < small:
#         small = n
# print(small)

################################################################################
# WHILE TASK.PY

# task_1
# n = int(input())
# i = 1
# while i <= n:
#     print(i)
#     i = i + 1
# task_2
# n = int(input())
# while n >= 1:
#     print(n)
#     n = n - 1
# task_3
# n = int(input())
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i = i + 1
# task_4
# n = int(input())
# i = 1
# while i <= n:
#     if i % 2 != 0:
#         print(i)
#     i = i + 1
# task_5
# n = int(input())
# i = 1
# total = 0
# while i <= n:
#     total = total + i
#     i = i + 1
# print(total)
# task_6
# n = int(input())
# i = 1
# total = 0
# while i <= n:
#     if i % 2 == 0:
#         total = total + i
#     i = i + 1
# print(total)
# task_7
# n = int(input())
# i = 1
# while i <= n:
#     if i % 3 == 0:
#         print(i)
#     i = i + 1
# task_8
# n = int(input())
# i = 0
# positive = 0
# negative = 0
# zero = 0
# while i < n:
#     x = int(input())
#     if x > 0:
#         positive = positive + 1
#     elif x < 0:
#         negative = negative + 1
#     else:
#         zero = zero + 1
#     i = i + 1
# print("eyreg:", positive)
# print("sorog:", negative)
# print("teg:", zero)
# task_9
# n = int(input())
# i = 0
# total = 0
# while i < n:
#     x = int(input())
#     if x > 0:
#         total = total + x
#     i = i + 1
# print(total)
# task_10
# n = int(input())
# i = 0
# while i < n:
#     x = int(input())
#     if i == 0:
#         biggest = x
#     elif x > biggest:
#         biggest = x
#     i = i + 1
# print(biggest)
# task_11
# n = int(input())
# i = 0
# while i < n:
#     x = int(input())
#     if i == 0:
#         smallest = x
#     elif x < smallest:
#         smallest = x
#     i = i + 1
# print(smallest)
# task_12
# n = int(input())
# i = 1
# while i <= n:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#     i = i + 1
# task_13
# n = int(input())
# if n < 0:
#     n = -n
# count = 0
# if n == 0:
#     count = 1
# while n > 0:
#     count = count + 1
#     n = n // 10
# print(count)
# task_14
# n = int(input())
# total = 0
# while n > 0:
#     total = total + n % 10
#     n = n // 10
# print(total)
# task_15
# n = int(input())
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
# print(reverse)
# task_16
# n = int(input())
# original = n
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10
# if original == reverse:
#     print("YES")
# else:
#     print("NO")
# task_17
# n = int(input())
# i = 2
# count = 0
# while i < n:
#     if n % i == 0:
#         count = count + 1
#     i = i + 1
# if n > 1 and count == 0:
#     print("YES")
# else:
#     print("NO")
# task_18
# n = int(input())
# num = 2
# while num <= n:
#     i = 2
#     count = 0
#     while i < num:
#         if num % i == 0:
#             count = count + 1
#         i = i + 1
#     if count == 0:
#         print(num)
#     num = num + 1
# task_19
# n = int(input())
# i = 1
# while i <= 10:
#     print(n, "*", i, "=", n * i)
#     i = i + 1
# task_20
# password = input()
# while password != "python123":
#     print("dahin oroldlono uu")
#     password = input()
# print("zov nuuts ug oruul:")