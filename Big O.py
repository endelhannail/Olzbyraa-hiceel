############################################
#task_1
# numbers = [1, 2, 3, 4, 5]
# print(numbers[0])
# ** Big O = O(1)
# task_2
# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     print(number)
# ** Big O = O(n)
# task_3
# numbers = [10, 20, 30, 40, 50]
# print(numbers[-1])
# # ** Big O = O(1)
# task_4
# n = int(input("n: "))
# for i in range(n):
#     print(i)
# ** Big O = O(n)
# task_5
# for i in range(n):
#     print(i)
# ** Big O = O(n)
# task_6
# for i in range(n):
#     for j in range(n):
#         print(i, j)
# ** Big O = O(n^2)
# task_7
# n = 5
# for i in range(n):
#     for j in range(n):
#         print(i, j)
# ** print(25) udaa ajillana.
# task_8
# n = 10
# for i in range(n):
#     for j in range(n):
#         print(i, j)
# ** print(100) udaa ajillana.
# task_9
# for i in range(n):
#     print(i)
# for j in range(n):
#     print(j)
# ** Big O = O(n)
# task_10
# O(2n) = O(n)
# ** Big O = O(n)
# task_11
# O(log n)
# task_12
# Uchir ni too 2 dahin bagasaj baina. Iimerhuu huvaagc bagasdag uildel ni ihevclen O(log n) baidag.
# task_13
# numbers = [1, 2, 3, 4, 5]
# print(numbers[0])            #Big O
# for number in numbers:
#     print(number)
# task_14
# for i in range(n):       # O(n)
#     print(i)
# print("Hello")
# task_15
# for i in range(n):             # n udaa
#     for j in range(n):          # n udaa
#         print(i, j)             # O(n²)
# print("Done")

# BONUS:


# task_16
# ** O(1) → O(log n) → O(n) → O(n²)
# task_17
# A                                             
# print(numbers[0])
# # B
# for x in numbers:
#     print(x)
# # C
# for x in numbers:
#     for y in numbers:
#       print(x, y)
# D
# 1000 → 500 → 250 → 125 → 
# A → O(1)                                      
# B → O(n)
# C → O(n²)
# D → O(log n)
# Neg uidel → O(1)
# Neg loop → O(n)
# Davhar loop → O(n²)
# 2 dahin huvaagdah → O(log n)

###############################################################
# 1


# task_1
# age = int(input())
# if age >= 18:
#     print("Орох боломжтой")
# else:
#     print("Орох боломжгүй")
# task_2
# x = int(input())
# if x % 2 == 0:
#     print("Тэгш")
# else:
#     print("Сондгой")
# task_3
# a = int(input())
# b = int(input())
# if a > b:
#     print(a)
# elif b > a:
#     print(b)
# else:
#     print("Тэнцүү")
# task_4
# day = int(input())
# if day == 1:
#     print("Даваа")
# elif day == 2:
#     print("Мягмар")
# elif day == 3:
#     print("Лхагва")
# elif day == 4:
#     print("Пүрэв")
# elif day == 5:
#     print("Баасан")
# elif day == 6 or day == 7:
#     if day == 6:
#         print("Бямба (Амралтын өдөр)")
#     else:
#         print("Ням (Амралтын өдөр)")
# else:
#     print("Буруу тоо")
# task_5
# km = int(input())
# hour = int(input())
# if km <= 2:
#     price = 3000
# else:
#     price = 3000 + (km - 2) * 1500
# if hour >= 22 or hour < 6:
#     price = int(price * 1.2)

# print(price)
# task_6
# kwh = int(input())
# if kwh <= 150:
#     price = kwh * 100
# elif kwh <= 300:
#     price = 150 * 100 + (kwh - 150) * 150
# else:
#     price = 150 * 100 + 150 * 150 + (kwh - 300) * 200

# print(price)
# task_7
# username = input()
# password = input()
# is_blocked = input() == "True"
# failed_attempts = int(input())

# if is_blocked:
#     print("Таны эрх хаагдсан байна")
# elif username == "" or password == "":
#     print("Мэдээллээ бүрэн оруулна уу")
# elif username != "admin":
#     print("Хэрэглэгч олдсонгүй")
# elif password != "1234":
#     if failed_attempts >= 2:
#         print("Эрх хаагдлаа")
#     else:
#         print("Нууц үг буруу")
# else:
#     print("Амжилттай нэвтэрлээ")


# 2


# task_1
# N = int(input())
# for i in range(1, N + 1):
#     print(i)
# task_2
# N = int(input())
# sum = 0
# for i in range(1, N + 1):
#     if i % 2 == 0:
#         sum += i

# print(sum)
# task_3
# n = int(input())
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")
# task_4
# money = 1000000
# year = 0
# while money < 2000000:
#     money = money * 1.12
#     year += 1

# print(year, "жил")
# task_5
# n = int(input())
# if n == 1:
#     print("1 анхны тоо биш")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print(f"{n} анхны тоо биш, {i}-т хуваагдана")
#             break
#     else:
#         print(f"{n} анхны тоо")
# task_6
# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     print(i, end=" ")
# task_7
# N = int(input())
# for i in range(1, N + 1):
#     for j in range(i):
#         print("*", end="")
#     print()
#  task_8
# secret = 42
# guesses = [50, 30, 42, 10]
# for i in range(5):
#     guess = guesses[i]

#     if guess > secret:
#         print(f"{guess}: Их байна")
#     elif guess < secret:
#         print(f"{guess}: Бага байна")
#     else:
#         print(f"{guess}: Зөв! {i + 1} дахь оролдлогоор таалаа")
#         break
# else:
#     print(f"Ялагдлаа. Нууц тоо: {secret}")
# task_9
# n = int(input())
# while n >= 10:
#     sum = 0
#     while n > 0:
#         sum += n % 10
#         n //= 10
#     n = sum
# print(n)


# 3


# task_1
# scores = [80, 90, 70, 60]
# sum = 0
# count = 0
# for score in scores:
#     sum += score
#     count += 1
# average = sum / count

# print(f"Нийлбэр: {sum}, Дундаж: {average}")
# task_2
# nums = [45, 89, 72, 89, 30]
# max_num = nums[0]
# max_index = 0
# for index, num in enumerate(nums):
#     if num > max_num:
#         max_num = num
#         max_index = index
# print(f"Хамгийн их: {max_num}, индекс: {max_index}")
# task_3
# names = ["Бат", "Сараа", "Дорж"]
# name = input()
# if name in names:
#     print(f"Олдлоо, индекс: {names.index(name)}")
# else:
#     print("Олдсонгүй")
# task_4
# prices = [1000, 2500, 8000]
# new_prices = list(map(lambda p: int(p * 0.9), prices))
# print(new_prices)
# task_5
# scores = [45, 78, 60, 30, 92]
# passed = list(filter(lambda score: score >= 60, scores))
# print(passed)
# print(f"Тэнцсэн: {len(passed)}")
# task_6
# orders = [1200, 45000, 8000, 23000, 500]
# total = 0
# for order in orders:
#     if order >= 5000:
#         total += order + 2000
# print(total)
# orders = [1200, 45000, 8000, 23000, 500]
# total = sum(order + 2000 for order in orders if order >= 5000)
# print(total)
# task_7
# names = ["Бат", "Сараа", "Дорж"]
# subjects = ["Математик", "Физик", "Англи", "Түүх"]
# scores = [
#     [80, 90, 70, 60],
#     [95, 85, 75, 65],
#     [50, 60, 70, 80]
# ]
# # 1. Оюутан бүрийн дундаж
# for i in range(len(names)):
#     average = sum(scores[i]) / len(scores[i])
#     print(f"{names[i]}: {average}")

# print()
# # 2. Хичээл бүрийн хамгийн өндөр оноо
# for subject, score_list in zip(subjects, zip(*scores)):
#     max_score = max(score_list)
#     index = score_list.index(max_score)
#     print(f"{subject}: {names[index]} ({max_score})")


# 4


# task_1
# name = input()
# name = name.capitalize()
# print(name, "(", len(name), "үсэг)")
# task_2
# word = input()
# letter = input()
# count = 0
# for char in word:
#     if char == letter:
#         count += 1
# print(count)
# print(word.count(letter))
# task_3
# email = input()
# if email.count("@") != 1:
#     print("Буруу имэйл")
# elif email[0] == "@":
#     print("Буруу имэйл")
# elif "." not in email.split("@")[1]:
#     print("Буруу имэйл")
# elif email[-1] == ".":
#     print("Буруу имэйл")
# else:
#     username, domain = email.split("@")
#     print(f"Username: {username}, Domain: {domain}")
# task_4
# bad_words = ["муу", "тэнэг"]
# sentence = input()
# words = sentence.split()
# for i in range(len(words)):
#     if words[i].lower() in bad_words:
#         words[i] = "*" * len(words[i])
# sentence = " ".join(words)
# print(sentence)
# task_5
# text = input()
# clean = ""
# for char in text:
#     if char.isalnum():
#         clean += char.lower()
# print(clean == clean[::-1])


# 5


# task_1
# def square(n):
#     return n * n
# print(square(5))
# print(square(-3))
# task_2
# def greet(name = "Зочин"):
#     return "Сайн уу, " + name + "!"
# print(greet("Бат"))
# print(greet())
# task_3
# def is_adult(age):
#     return age >= 18
# print(is_adult(20))
# print(is_adult(16))
# task_4
# def calculate_bmi(weight, height):
#     bmi = weight / (height * height)
#     return round(bmi, 2)
# def get_category(bmi):
#     if bmi < 18.5:
#         return "Туранхай"
#     elif bmi < 25:
#         return "Хэвийн"
#     elif bmi < 30:
#         return "Илүүдэл жинтэй"
#     else:
#         return "Таргалалттай"
# bmi = calculate_bmi(70, 1.75)
# category = get_category(bmi)
# print(f"BMI: {bmi}, {category}")
# task_5
# def calc_insurance(gross):
#     return gross * 0.115
# def calc_tax(gross):
#     insurance = calc_insurance(gross)
#     return (gross - insurance) * 0.10
# def calc_net(gross):
#     insurance = calc_insurance(gross)
#     tax = calc_tax(gross)
#     return gross - insurance - tax
# gross = 2000000
# insurance = calc_insurance(gross)
# tax = calc_tax(gross)
# net = calc_net(gross)
# print("НДШ:", int(insurance))
# print("Татвар:", int(tax))
# print("Гарт:", int(net))
# task_6
# def make_counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     def decrement():
#         nonlocal count
#         count -= 1
#         return count
#     def reset():
#         nonlocal count
#         count = 0
#         return count
#     return {
#         "increment": increment,
#         "decrement": decrement,
#         "reset": reset
#     }
# c1 = make_counter()
# c2 = make_counter()
# print(c1["increment"]())
# print(c1["increment"]())
# print(c2["increment"]())
# print(c1["decrement"]())
# print(c1["reset"]())


# 6

# task_1
# student = {
#     "name": "Бат",
#     "age": 20,
#     "city": "Улаанбаатар"
# }
# print(student)
# student["age"] += 1
# student["email"] = "bat@mail.com"
# del student["city"]
# print(student)
# task_2
# prices = {"талх": 2500, "сүү": 3800, "мах": 18000}
# for name, price in prices.items():
#     print(f"{name} — {price}₮")
# task_3
# prices = {"талх": 2500, "сүү": 3800, "мах": 18000, "өндөг": 6500}
# max_name = ""
# max_price = 0
# total = 0
# for name, price in prices.items():
#     total += price
#     if price > max_price:
#         max_price = price
#         max_name = name
# print(f"Хамгийн үнэтэй: {max_name} — {max_price}₮")
# print(f"Нийт: {total}₮")
# task_4
# votes = ["Бат", "Сараа", "Бат", "Дорж", "Бат", "Сараа"]
# counts = {}
# for name in votes:
#     counts[name] = counts.get(name, 0) + 1
# winner = ""
# max_votes = 0
# for name, count in counts.items():
#     if count > max_votes:
#         max_votes = count
#         winner = name
# print(counts)
# print(f"Ялагч: {winner} ({max_votes} санал)")
# task_5
# students = [
#     {"name": "Бат", "class": "10А", "score": 85},
#     {"name": "Сараа", "class": "10Б", "score": 92},
#     {"name": "Дорж", "class": "10А", "score": 70},
#     {"name": "Нараа", "class": "10Б", "score": 78},
#     {"name": "Тэмүүлэн", "class": "10А", "score": 95}
# ]
# # groups = {}
# # for student in students:
# #     class_name = student["class"]
# #     name = student["name"]
# #     if class_name not in groups:
# #         groups[class_name] = []
# #     groups[class_name].append(name)
# # print(groups)
# task_6
# students = [
#     {"name": "Бат", "class": "10А", "score": 85},
#     {"name": "Сараа", "class": "10Б", "score": 92},
#     {"name": "Дорж", "class": "10А", "score": 70},
#     {"name": "Нараа", "class": "10Б", "score": 78},
#     {"name": "Тэмүүлэн", "class": "10А", "score": 95}
# ]
# classes = {}
# for student in students:
#     class_name = student["class"]
#     if class_name not in classes:
#         classes[class_name] = []
#     classes[class_name].append(student)
# for class_name, students_list in classes.items():
#     total = 0
#     best_name = ""
#     best_score = 0
#     for student in students_list:
#         total += student["score"]
#         if student["score"] > best_score:
#             best_score = student["score"]
#             best_name = student["name"]
#     average = total / len(students_list)
#     print(f"{class_name} — дундаж: {average:.2f}, шилдэг: {best_name} ({best_score})")
# task_7
# from turtle import title
# books = {"Харри Поттер": 1, "Шерлок Холмс": 2}
# loans = {}
# def borrow(person, title):
#     if title not in books:
#         return "Ийм ном байхгүй"
#     if books[title] == 0:
#         return "Бүх хувь зээлэгдсэн байна"
#     if person not in loans:
#         loans[person] = []
#     if len(loans[person]) >= 3:
#         return "Хамгийн ихдээ 3 ном зээлнэ"
#     books[title] -= 1
#     loans[person].append(title)
#     return "Амжилттай зээллээ"
# def return_book(person, title):
#     if person not in loans or title not in loans[person]:
#         return "Энэ номыг зээлээгүй байна"
#     books[title] += 1
#     loans[person].remove(title)
#     return "Амжилттай буцаалаа"
# print(borrow("Бат", "Харри Поттер"))
# print(borrow("Сараа", "Харри Поттер"))
# print(borrow("Бат", "Хобби"))
# print(return_book("Сараа", "Шерлок Холмс"))
# print(return_book("Бат", "Харри Поттер"))
# print(borrow("Сараа", "Харри Поттер"))