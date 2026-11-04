# task_1
# name = input()
# print("Сайн уу, " + name + "!")
# task_2
# a, b = map(int, input().split())
# print(a + b)
# task_3
# price = float(input())
# total = price * 2
# print("Нийт үнэ: " + str(total))
# task_4
# a = input()
# print(type(a))
# b = int(a)
# print(type(b))
# task_5
# s = input()
# print(len(s))
# task_6
# s = input()
# print(s[0])
# print(s[-1])
# task_7
# n = int(input())
# for i in range(1, n + 1):
#     print(i)
# task_8
# numbers = input().split()
# nums = []
# for x in numbers:
#     nums.append(int(x))
# print(sum(nums))
# task_9
# nums = list(map(int, input().split()))
# print(min(nums), max(nums))
# task_10
# nums = list(map(int, input().split()))
# average = sum(nums) / len(nums)
# print(round(average, 2))
# task_11
# animals = input().split()
# name = input()
# animals.append(name)
# print(animals)
# task_12
# names = input().split()
# name = input()
# names.insert(1, name)
# print(names)
# task_13
# names = input().split()
# name = input()
# names.remove(name)
# print(names)
# task_14
# names = input().split()
# index = int(input())
# removed = names.pop(index)
# print(removed)
# print(",".join(names))
# task_15
# nums = list(map(int, input().split()))
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
# task_16
# nums = list(map(int, input().split()))
# nums.reverse()
# print(nums)
# task_17
# x = "   hello   "
# print("[" + x.strip() + "]")
# print("[" + x.lstrip() + "]")
# print("[" + x.rstrip() + "]")
# task_18
# s = input()
# words = s.split()
# print(len(words))
# task_19
# s = input().lower()
# letter = input().lower()
# print(s.count(letter))
# task_20
# s = input()
# word = input()
# print(s.find(word))
# if s.find(word) != -1:
#     print(s.index(word))
# else:
#     print("Олдсонгүй")
# task_21
# files = input().split()
# found = False
# for file in files:
#     if file.startswith("report") and file.endswith(".pdf"):
#         print(file)
#         found = True
# if found == False:
#     print("Олдсонгүй")
# task_22
# s = input()
# old = input()
# new = input()
# s = s.replace(old, new)
# print(s)
# task_23
# names = input().lower().split()
# name = input().lower()
# if name in names:
#     print("YES")
# else:
#     print("NO")
# task_24
# s = input()
# print(s[:3])
# print(s[-3:])
# task_25
# s = input()
# s = s.strip().lower()
# if s == s[::-1]:
#     print("YES")
# else:
# print("NO")
# task_26
# words = input().split()
# longest = words[0]
# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print(longest)
# task_27
# data = input().split(",")
# name = data[0].strip()
# age = int(data[1].strip())
# city = data[2].strip()
# age += 1
# print(name + " | Ирэх жил: " + str(age) + " | " + city)
# task_28
# words = input().lower().split()
# result = []
# for word in words:
#     if word not in result:
#         result.append(word)
# result.sort()
# print(" ".join(result))
# task_29
# nums = list(map(int, input().split()))
# result = []
# for x in nums:
#     if x not in result:
#         result.append(x)
# result.sort(reverse=True)
# print(result[1])
# task_30
# n = int(input())
# names = []
# scores = []
# for i in range(n):
#     data = input().split(",")
#     name = data[0].strip()
#     score = int(data[1].strip())

#     names.append(name)
#     scores.append(score)
# average = round(sum(scores) / len(scores), 2)
# highest = max(scores)
# index = scores.index(highest)
# print("Дундаж:", average)
# print("Хамгийн өндөр:", names[index], highest)
# names.sort()
# print("Нэрс:", ", ".join(names))