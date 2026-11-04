# task_1
# age = int(input())
# if age >= 18:
#     print("Орох боломжтой")
# else:
#     print("Орох боломжгүй")
# task_2
# n = int(input())
# if n % 2 == 0:
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
# n = int(input())
# if n == 1:
#     print("Даваа")
# elif n == 2:
#     print("Мягмар")
# elif n == 3:
#     print("Лхагва")
# elif n == 4:
#     print("Пүрэв")
# elif n == 5:
#     print("Баасан")
# elif n == 6 or n == 7:
#     if n == 6:
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
#     price = price * 1.2
# print(int(price))
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
# task_8
# n = int(input())
# for i in range(1, n + 1):
#     print(i)
# task_9
# n = int(input())
# total = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         total += i
# print(total)
# task_10
# n = int(input())
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")
# task_11
# money = 1000000
# year = 0
# while money < 2000000:
#     money = money * 1.12
#     year += 1
# print(year, "жил")
# task_12
# n = int(input())
# if n < 2:
#     print(n, "анхны тоо биш")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print(f"{n} анхны тоо биш, {i}-т хуваагдана")
#             break
#     else:
#         print(f"{n} анхны тоо")
# task_13
# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     print(i, end=" ")
# task_14
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(i):
#         print("*", end="")
#     print()
# task_15
# guesses = [50, 30, 42, 10]
# secret = 42
# count = 0
# won = False
# for guess in guesses:
#     if count == 5:
#         break
#     count += 1
#     if guess > secret:
#         print(f"{guess}: Их байна")
#     elif guess < secret:
#         print(f"{guess}: Бага байна")
#     else:
#         print(f"{guess}: Зөв! {count} дахь оролдлогоор таалаа")
#         won = True
#         break
# if not won:
#     print(f"Ялагдлаа. Нууц тоо: {secret}")
# task_16
# secret = 42
# won = False
# for i in range(1, 6):
#     guess = int(input())
#     if guess > secret:
#         print(f"{guess}: Их байна")
#     elif guess < secret:
#         print(f"{guess}: Бага байна")
#     else:
#         print(f"{guess}: Зөв! {i} дахь оролдлогоор таалаа")
#         won = True
#         break
# if not won:
#     print(f"Ялагдлаа. Нууц тоо: {secret}")
# task_17
# n = int(input())
# while n >= 10:
#     total = 0
#     while n > 0:
#         total += n % 10
#         n = n // 10
#     n = total
# print(n)
# task_18
# scores = [80, 90, 70, 60]
# total = 0
# count = 0
# for score in scores:
#     total += score
#     count += 1
# average = total / count
# print("Нийлбэр:", total)
# print("Дундаж:", average)
# task_19
# scores = [45, 89, 72, 89, 30]
# highest = scores[0]
# index = 0
# for i, score in enumerate(scores):
#     if score > highest:
#         highest = score
#         index = i
# print("Хамгийн их:", highest)
# print("Индекс:", index)
# task_20
# names = ["Бат", "Сараа", "Дорж"]
# name = input()
# if name in names:
#     print("Олдлоо, индекс:", names.index(name))
# else:
#     print("Олдсонгүй")
# task_21
# prices = [1000, 2500, 8000]
# new_prices = [p * 0.9 for p in prices]
# print(new_prices)
# task_22
# scores = [45, 78, 60, 30, 92]
# passed = [score for score in scores if score >= 60]
# print(passed)
# print("Тэнцсэн:", len(passed))
# task_23
# orders = [1200, 45000, 8000, 23000, 500]
# total = 0
# for order in orders:
#     if order >= 5000:
#         total += order + 2000
# print(total)
# task_24
# names = ["Бат", "Сараа", "Дорж"]
# subjects = ["Математик", "Физик", "Англи", "Түүх"]
# scores = [
#     [80, 90, 70, 60],
#     [95, 85, 75, 65],
#     [50, 60, 70, 80]
# ]
# for i in range(len(names)):
#     total = 0
#     for score in scores[i]:
#         total += score
#     average = total / len(scores[i])
#     print(f"{names[i]}: {average}")
# task_25
# name = input()
# name = name.capitalize()
# print(name, f"({len(name)} үсэг)")
# task_26
# word = input()
# letter = input()
# count = 0
# for ch in word:
#     if ch == letter:
#         count += 1
# print(count)
# task_27
# email = input()
# if email.count("@") == 1:
#     parts = email.split("@")
#     username = parts[0]
#     domain = parts[1]
#     if username != "" and "." in domain and not domain.endswith("."):
#         print("Username:", username)
#         print("Domain:", domain)
#     else:
#         print("Буруу имэйл")
# else:
#     print("Буруу имэйл")
# task_28
# bad_words = ["муу", "тэнэг"]
# sentence = input()
# words = sentence.split()
# result = []
# for word in words:
#     if word.lower() in bad_words:
#         result.append("*" * len(word))
#     else:
#         result.append(word)
# print(" ".join(result))
# task_29
# text = input()
# clean = ""
# for ch in text.lower():
#     if ch.isalnum():
#         clean += ch
# if clean == clean[::-1]:
#     print(True)
# else:
#     print(False)
# task_30
# def square(n):
#     return n * n
# print(square(5))
# print(square(-3))
# task_31
# def greet(name="Зочин"):
#     return f"Сайн уу, {name}!"
# print(greet("Бат"))
# print(greet())
# task_32
# def is_adult(age):
#     if age >= 18:
#         return True
#     else:
#         return False
# print(is_adult(20))
# print(is_adult(16))
# task_33
# def calculate_bmi(weight, height):
#     return round(weight / (height * height), 2)
# def get_category(bmi):
#     if bmi < 18.5:
#         return "Туранхай"
#     elif bmi < 25:
#         return "Хэвийн"
#     elif bmi < 30:
#         return "Илүүдэл жинтэй"
#     else:
#         return "Таргалалттай"
# weight = float(input())
# height = float(input())
# bmi = calculate_bmi(weight, height)
# category = get_category(bmi)
# print(f"BMI: {bmi}, {category}")
# task_34
# def calc_insurance(gross):
#     return gross * 0.115
# def calc_tax(gross):
#     insurance = calc_insurance(gross)
#     return (gross - insurance) * 0.10
# def calc_net(gross):
#     insurance = calc_insurance(gross)
#     tax = calc_tax(gross)
#     return gross - insurance - tax
# gross = int(input())
# print("НДШ:", int(calc_insurance(gross)))
# print("Татвар:", int(calc_tax(gross)))
# print("Гарт:", int(calc_net(gross)))
# task_35
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
# task_36
# user = {
#     "name": "Бат",
#     "age": 20,
#     "city": "Улаанбаатар"
# }
# print(user)
# user["age"] += 1
# user["email"] = "bat@mail.com"
# del user["city"]
# print(user)
# task_37
# prices = {"талх": 2500, "сүү": 3800, "мах": 18000}
# for name, price in prices.items():
#     print(f"{name} — {price}₮")
# task_38
# prices = {"талх": 2500, "сүү": 3800, "мах": 18000, "өндөг": 6500}
# highest_name = ""
# highest_price = 0
# total = 0
# for name, price in prices.items():
#     total += price
#     if price > highest_price:
#         highest_price = price
#         highest_name = name
# print(f"Хамгийн үнэтэй: {highest_name} — {highest_price}₮")
# print(f"Нийт: {total}₮")
# task_39
# votes = ["Бат", "Сараа", "Бат", "Дорж", "Бат", "Сараа"]
# counts = {}
# for name in votes:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)
# winner = ""
# highest = 0
# for name, count in counts.items():
#     if count > highest:
#         highest = count
#         winner = name
# print(f"Ялагч: {winner} ({highest} санал)")
# task_40
# students = [
#     {"name": "Бат", "class": "10А", "score": 85},
#     {"name": "Сараа", "class": "10Б", "score": 92},
#     {"name": "Дорж", "class": "10А", "score": 70},
#     {"name": "Нараа", "class": "10Б", "score": 78},
#     {"name": "Тэмүүлэн", "class": "10А", "score": 95}
# ]
# groups = {}
# for student in students:
#     class_name = student["class"]
#     name = student["name"]
#     if class_name not in groups:
#         groups[class_name] = []
#     groups[class_name].append(name)
# print(groups)
# task_41
# students = [
#     {"name": "Бат", "class": "10А", "score": 85},
#     {"name": "Сараа", "class": "10Б", "score": 92},
#     {"name": "Дорж", "class": "10А", "score": 70},
#     {"name": "Нараа", "class": "10Б", "score": 78},
#     {"name": "Тэмүүлэн", "class": "10А", "score": 95}
# ]
# groups = {}
# for student in students:
#     class_name = student["class"]
#     if class_name not in groups:
#         groups[class_name] = []
#     groups[class_name].append(student)
# for class_name, members in groups.items():
#     total = 0
#     highest = 0
#     best_name = ""
#     for student in members:
#         total += student["score"]
#         if student["score"] > highest:
#             highest = student["score"]
#             best_name = student["name"]
#     average = round(total / len(members), 2)
#     print(f"{class_name} — дундаж: {average}, шилдэг: {best_name} ({highest})")
# task_42
# books = {"Харри Поттер": 1, "Шерлок Холмс": 2}
# loans = {}

# def borrow(person, title):
#     if title not in books:
#         return "Ийм ном байхгүй"
#     if books[title] == 0:
#         return "Бүх хувь зээлэгдсэн байна"
#     if len(loans.get(person, [])) >= 3:
#         return "Хамгийн ихдээ 3 ном зээлнэ"
#     books[title] -= 1
#     if person not in loans:
#         loans[person] = []
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