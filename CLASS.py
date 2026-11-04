# task_1
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# student1 = Student("Нараа", 17)
# student2 = Student("Тэмүүлэн", 19)
# print(student1.name, student1.age)
# print(student2.name, student2.age)
# task_2
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
# student1 = Student("Бат", 18, "12А")
# print("Нэр:", student1.name, "Нас:", student1.age, "Анги:", student1.grade)
# task_3
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
# student1 = Student("Бат", 85)
# student2 = Student("Сараа", 95)
# print(student1.name, student1.score)
# print(student2.name, student2.score)
# task_4
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def add_score(self):
#         self.score += 5
# student1 = Student("Бат", 80)
# student1.add_score()
# print(student1.score)
# task_5
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def show_info(self):
#         print("Нэр:", self.name, "Нас:", self.age, "Анги:", self.grade)
# student1 = Student("Сараа", 19, "12Б")
# student1.show_info()
# task_6
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def check_result(self):
#         if self.score >= 60:
#             print(self.name + ": Тэнцсэн")
#         else:
#             print(self.name + ": Тэнцээгүй")
# student1 = Student("Бат", 75)
# student2 = Student("Нараа", 45)
# student1.check_result()
# student2.check_result()
# task_7
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def add_score(self):
#         self.score += 5
# student1 = Student("Бат", 80)
# student1.add_score()
# print(student1.score)
# task_8
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def birthday(self):
#         self.age += 1
# student1 = Student("Сараа", 18)
# student1.birthday()
# student1.birthday()
# print(student1.age)
# task_9
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def get_grade(self):
#         if self.score >= 90:
#             print("A")
#         elif self.score >= 80:
#             print("B")
#         elif self.score >= 70:
#             print("C")
#         elif self.score >= 60:
#             print("D")
#         else:
#             print("F")
# student1 = Student("Бат", 85)
# student1.get_grade()
# task_10
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.attendance = 0
#     def attend(self):
#         self.attendance += 1
#     def show_attendance(self):
#         print(self.attendance)
# student1 = Student("Бат")
# student1.attend()
# student1.attend()
# student1.attend()
# student1.show_attendance()
# task-11
# class Student:
#     def __init__(self, name, score, attendance):
#         self.name = name
#         self.score = score
#         self.attendance = attendance
#     def check_result(self):
#         if self.score >= 60 and self.attendance >= 80:
#             print("Хичээлд тэнцсэн")
#         else:
#             print("Хичээлд тэнцээгүй")
# student1 = Student("Бат", 75, 90)
# student1.check_result()
# task_12
# class Student:
#     def __init__(self, name, scores):
#         self.name = name
#         self.scores = scores
#     def show_scores(self):
#         print(self.scores)
#     def add_score(self, score):
#         self.scores.append(score)
#     def average(self):
#         total = 0
#         for score in self.scores:
#             total += score
#         print(total / len(self.scores))
# student1 = Student("Бат", [80, 90, 70])
# student1.show_scores()
# student1.add_score(100)
# student1.show_scores()
# student1.average()
# task_13
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def show_info(self):
#         print(self.name, self.age, self.grade)
#     def change_name(self, new_name):
#         self.name = new_name
#     def change_grade(self, new_grade):
#         self.grade = new_grade
# student1 = Student("Бат", 18, "12А")
# student1.change_name("Болд")
# student1.change_grade("12Б")
# student1.show_info()
# task_14
# class Student:
#     def __init__(self, name, grade, score):
#         self.name = name
#         self.grade = grade
#         self.scores = [score]
#     def show_info(self):
#         print("Нэр:", self.name)
#         print("Анги:", self.grade)
#         print("Оноо:", self.scores)
#     def add_score(self, score):
#         self.scores.append(score)
#     def check_result(self):
#         total = 0
#         for score in self.scores:
#             total += score
#         avg = total / len(self.scores)
#         if avg >= 60:
#             print("Тэнцсэн")
#         else:
#             print("Тэнцээгүй")
#     def average(self):
#         total = 0
#         for score in self.scores:
#             total += score
#         print(total / len(self.scores))
# student1 = Student("Бат", "12А", 80)
# student2 = Student("Сараа", "12Б", 50)
# student1.add_score(90)
# student2.add_score(40)
# student1.show_info()
# student1.average()
# student1.check_result()
# student2.show_info()
# student2.average()
# student2.check_result()
# task_15
# class Phone:
#     def __init__(self, brand, battery):
#         self.brand = brand
#         self.battery = battery
#     def use_phone(self):
#         self.battery -= 10
#     def charge(self):
#         self.battery += 20
#     def show_battery(self):
#         print("Цэнэг:", str(self.battery) + "%")
# phone1 = Phone("iPhone", 80)
# phone1.use_phone()
# phone1.show_battery()
# phone1.charge()
# phone1.show_battery()
# task_16
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def sell(self, amount):
#         if amount > self.quantity:
#             print("Бараа хүрэлцэхгүй")
#         else:
#             self.quantity -= amount
#     def show_total(self):
#         print("Үлдэгдэл:", self.quantity, "Нийт үнэ:", self.price * self.quantity)
# product1 = Product("Mouse", 30000, 10)
# product1.sell(3)
# product1.show_total()
# task_17
# class Athlete:
#     def __init__(self, name, points):
#         self.name = name
#         self.points = points
#     def add_points(self, points):
#         self.points += points
#     def lose_points(self, points):
#         self.points -= points
#     def show_points(self):
#         print("Оноо:", self.points)
# athlete1 = Athlete("Бат", 20)
# athlete1.add_points(15)
# athlete1.lose_points(5)
# athlete1.show_points()
# task_18
# class Movie:
#     def __init__(self, title, rating, views):
#         self.title = title
#         self.rating = rating
#         self.views = views
#     def add_view(self):
#         self.views += 1
#     def update_rating(self, new_rating):
#         self.rating = new_rating
#     def show_info(self):
#         print("Кино:", self.title)
#         print("Үнэлгээ:", self.rating)
#         print("Үзсэн хүн:", self.views)
# movie1 = Movie("Avatar", 8.5, 1000)
# movie2 = Movie("Titanic", 9.0, 2000)
# movie1.add_view()
# movie1.update_rating(9.0)
# movie1.show_info()
# movie2.show_info()
# task_19
# class GameCharacter:
#     def __init__(self, name, health, damage):
#         self.name = name
#         self.health = health
#         self.damage = damage
#     def attack(self, enemy):
#         enemy.health -= self.damage
#     def show_health(self):
#         print(self.name + "-ийн амь:", self.health)
# player1 = GameCharacter("Knight", 100, 20)
# player2 = GameCharacter("Goblin", 60, 10)
# player1.attack(player2)
# player2.show_health()
# task_20
# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def add_money(self, amount):
#         self.balance += amount
#     def pay(self, amount):
#         if amount > self.balance:
#             print("Мөнгө хүрэлцэхгүй")
#         else:
#             self.balance -= amount
#     def show_balance(self):
#         print("Үлдэгдэл:", self.balance)
# wallet1 = Wallet("Бат", 50000)
# wallet1.add_money(20000)
# wallet1.pay(15000)
# wallet1.show_balance()
# task_21
# class LibraryBook:
#     def __init__(self, title, available):
#         self.title = title
#         self.available = available
#     def borrow(self):
#         if self.available:
#             self.available = False
#             print("Номыг зээллээ")
#         else:
#             print("Ном аль хэдийн зээлэгдсэн байна")
#     def return_book(self):
#         self.available = True
#         print("Номыг буцаалаа")
# book1 = LibraryBook("Python", True)
# book1.borrow()
# book1.borrow()
# book1.return_book()
# task_22
# class Employee:
#     def __init__(self, name, salary, bonus):
#         self.name = name
#         self.salary = salary
#         self.bonus = bonus
#     def add_bonus(self, amount):
#         self.bonus += amount
#     def get_total_salary(self):
#         print("Нийт цалин:", self.salary + self.bonus)
# employee1 = Employee("Бат", 2000000, 100000)
# employee1.add_bonus(50000)
# employee1.get_total_salary()
# task_23
# class CartItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def increase_quantity(self, amount):
#         self.quantity += amount
#     def decrease_quantity(self, amount):
#         if amount <= self.quantity:
#             self.quantity -= amount
#         else:
#             print("Барааны тоо хүрэлцэхгүй")
#     def get_total_price(self):
#         print(self.name, "Нийт үнэ:", self.price * self.quantity)
# item1 = CartItem("Mouse", 30000, 2)
# item2 = CartItem("Keyboard", 50000, 1)
# item3 = CartItem("Headset", 40000, 3)
# item1.get_total_price()
# item2.get_total_price()
# item3.get_total_price()
# task_24
# class Computer:
#     def __init__(self, brand, ram, storage):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage
#     def upgrade_ram(self, amount):
#         self.ram += amount
#     def upgrade_storage(self, amount):
#         self.storage += amount
#     def show_info(self):
#         print("Үйлдвэрлэгч:", self.brand)
#         print("RAM:", self.ram, "GB")
#         print("Багтаамж:", self.storage, "GB")
# pc1 = Computer("Lenovo", 8, 256)
# pc1.upgrade_ram(8)
# pc1.upgrade_storage(256)
# pc1.show_info()
# task_25
# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
# class SavingsAccount(Account):
#     def __init__(self, owner, balance, interest_rate):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate
#     def add_interest(self):
#         self.balance += self.balance * self.interest_rate / 100
#         print("Хүү нэмсний дараах үлдэгдэл:", self.balance)
# account1 = SavingsAccount("Бат", 100000, 10)
# account1.add_interest()
# task_26
# class Device:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
# class Laptop(Device):
#     def __init__(self, brand, price, ram):
#         super().__init__(brand, price)
#         self.ram = ram
#     def show_info(self):
#         print("Үйлдвэрлэгч:", self.brand)
#         print("Үнэ:", self.price)
#         print("RAM:", self.ram, "GB")
# laptop1 = Laptop("Apple", 4500000, 16)
# laptop1.show_info()
# task_27
# class User:
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
# class Admin(User):
#     def __init__(self, username, email, permission):
#         super().__init__(username, email)
#         self.permission = permission
#     def show_info(self):
#         print("Хэрэглэгч:", self.username)
#         print("Имэйл:", self.email)
#         print("Эрх:", self.permission)
# admin1 = Admin("saraa", "saraa@example.com", "Full Access")
# admin1.show_info()
# task_28
# class Character:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
# class Mage(Character):
#     def __init__(self, name, health, mana):
#         super().__init__(name, health)
#         self.mana = mana
#     def cast_spell(self):
#         if self.mana >= 10:
#             self.mana -= 10
#         else:
#             print("Mana хүрэлцэхгүй")
#     def show_info(self):
#         print("Нэр:", self.name)
#         print("Амь:", self.health)
#         print("Mana:", self.mana)
# mage1 = Mage("Wizard", 100, 30)
# mage1.cast_spell()
# mage1.show_info()