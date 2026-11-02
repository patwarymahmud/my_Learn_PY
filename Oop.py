# # ==========================================================
# # Python OOP (Object-Oriented Programming)
# # Beginner Friendly Notes
# # ==========================================================

# # ==========================================================
# # 1. Class & Object
# # ==========================================================

# # Real Life:
# #
# # Mobile Company প্রথমে একটি Design বানায়।
# #
# # Camera = 50MP
# # RAM = 8GB
# # Battery = 5000mAh
# #
# # এই Design = Class
# #
# # Design অনুযায়ী তৈরি হওয়া Mobile = Object

# class Mobile:

#     def __init__(self, brand_name):
#         self.brand_name = brand_name

# # Object Variable

# mobile_1 = Mobile("Samsung")
# mobile_2 = Mobile("iPhone")

# print(mobile_1.brand_name)
# print(mobile_2.brand_name)

# # Output:
# #
# # Samsung
# # iPhone

# # ==========================================================
# # 2. Encapsulation
# # ==========================================================

# # Real Life:
# #
# # ATM Card দিয়ে টাকা তুলতে পারো।
# #
# # কিন্তু Bank Database-এর ভিতরে সরাসরি
# # ঢুকে টাকা পরিবর্তন করতে পারো না।
# #
# # Data লুকানো থাকে।
# #
# # এটাকেই Encapsulation বলে।

# class BankAccount:

#     def __init__(self):

#         # Private Variable

#         self.__balance = 50000

#     def show_balance(self):

#         print(self.__balance)

# # Object Variable

# account_1 = BankAccount()

# account_1.show_balance()

# # Output:
# #
# # 50000

# # ==========================================================
# # 3. Inheritance
# # ==========================================================

# # Real Life:
# #
# # বাবা থেকে ছেলে সম্পত্তি পায়।
# #
# # House
# # Land
# # Car
# #
# # ছেলে বাবার জিনিস ব্যবহার করতে পারে।
# #
# # এটাকেই Inheritance বলে।

# class Father:

#     def house(self):

#         print("Father House")

# class Son(Father):

#     pass

# # Object Variable

# son_1 = Son()

# son_1.house()

# # Output:
# #
# # Father House

# # ==========================================================
# # 4. Polymorphism
# # ==========================================================

# # Real Life:
# #
# # TV Remote-এর Power Button একই।
# #
# # Samsung TV চালু করে।
# # LG TV চালু করে।
# #
# # Button একই,
# # কিন্তু কাজ আলাদা।
# #
# # এটাকেই Polymorphism বলে।

# class Cat:

#     def sound(self):

#         print("Meow")

# class Dog:

#     def sound(self):

#         print("Bark")

# # Object Variables

# cat_1 = Cat()

# dog_1 = Dog()

# cat_1.sound()

# dog_1.sound()

# # Output:
# #
# # Meow
# # Bark

# # ==========================================================
# # 5. Abstraction
# # ==========================================================

# # Real Life:
# #
# # তুমি Car Start করো।
# #
# # কিন্তু ভিতরের Engine,
# # Sensor,
# # Fuel System
# #
# # কিভাবে কাজ করে জানো না।
# #
# # শুধু প্রয়োজনীয় Button ব্যবহার করো।
# #
# # এটাকেই Abstraction বলে।

# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def start(self):

#         pass

# class Car(Vehicle):

#     def start(self):

#         print("Car Started")

# # Object Variable

# car_1 = Car()

# car_1.start()

# # Output:
# #
# # Car Started

# # ==========================================================
# # OOP-এর সবচেয়ে গুরুত্বপূর্ণ বিষয়
# # ==========================================================

# # Class
# # Object
# # Variable (Attribute)
# # Method
# # Constructor (__init__)
# # Encapsulation
# # Inheritance
# # Polymorphism
# # Abstraction

# # ==========================================================
# # One Line Definition
# # ==========================================================

# # Python OOP হলো Class এবং Object ব্যবহার করে
# # Real Life-এর মতো করে Program তৈরি করার পদ্ধতি।
# # ==========================================================

# #constractor 2 prokar
# #Non-parameterized Constractor
# #class parentinfo:
# #     pass
# # p1 = parentinfo()
# # print(p1)

 #parameterized constractor
class parentinfo:
     def MahamudSFamily(self, name, age):
         print(f"my name is {name}, my age is {age}")


p1 = parentinfo()
p1.MahamudSFamily("patwary", 22)
p1.MahamudSFamily("jaber", 28)
# এইভাবে একবার ফাংশন লিখে যতবার ওই ফাংশানের প্যারেন্ট কে কল করে তারপর প্যারেন্টের ভিতরে যেই মাহমুদ ফ্যামিলি আছে বেরিয়ে ফেলার মত ওইটাকে কল করে যতবার নাম এবং বয়স  দেওয়া হবে ততবারই আউটপুট আসবে
#output: my name is patwary, my age is 22
#output:my name is jaber, my age is 28    

#another way example
class parentinfo:
     def __init__(self, name, number):
          print(f"my name is {name}, my number is {number}")
p1 = parentinfo("Mahmaud", "01869207460")
#output: my name is Mahmaud, my number is 01869207460

# ==========================================================
# Python OOP Constructor (__init__) - Beginner Friendly Notes
# ==========================================================

# ==========================================================
# Constructor কী?
# ==========================================================

# Constructor হলো Class-এর একটি Special Method,
# যা Object তৈরি হওয়ার সাথে সাথেই Automatically Run হয়।

# Python-এ Constructor-এর নাম:

# __init__()

# ==========================================================
# Constructor কেন ব্যবহার করা হয়?
# ==========================================================

# ✔ Object তৈরি হওয়ার সময় Initial Value দেওয়ার জন্য
# ✔ Object Setup করার জন্য
# ✔ Variable তৈরি করার জন্য
# ✔ Code Reuse করার জন্য
# ✔ বারবার একই Code লেখা কমানোর জন্য

# ==========================================================
# Constructor-এর গুরুত্বপূর্ণ Keywords
# ==========================================================

# 1. __init__()
# Constructor Method-এর নাম

# 2. self
# বর্তমান Object-কে নির্দেশ করে

# 3. Parameter
# Object তৈরি করার সময় Data নেওয়ার জন্য

# ==========================================================
# Real Life Example
# ==========================================================

# ধরো একটি Student Admission System আছে।

# নতুন Student Add করার সময়:

# Name
# Age
# Department

# দিতে হবে।

# তাই Object তৈরি হওয়ার সাথে সাথেই
# তথ্যগুলো Save করার জন্য Constructor ব্যবহার করা হয়।

# ==========================================================
# Constructor Syntax
# ==========================================================

class Student:

    def __init__(self):

        print("Constructor Called")

student_1 = Student()

# Output:

# Constructor Called

# ==========================================================
# Constructor Flow
# ==========================================================

# student_1 = Student()

# ↓

# Object Create

# ↓

# __init__() Automatically Call

# ↓

# Constructor-এর Code Execute

# ↓

# Object Ready

# ==========================================================
# 1. Default Constructor
# ==========================================================

# কোনো Parameter থাকে না।

class Student:

    def __init__(self):

        print("Student Created")

student_1 = Student()

# Output:

# Student Created

# Real Life:

# নতুন Account খুললেই Welcome Message দেখানো।

# ==========================================================
# 2. Parameterized Constructor
# ==========================================================

# Parameter গ্রহণ করে।

class Student:

    def __init__(self, name):

        self.name = name

student_1 = Student("Hasan")

print(student_1.name)
# Output:
# Hasan
#another example:
class parentinfo:
    def Eshansfamily(self,name, age):
        print(f"my name is {name}, my age is {age}")

p1 = parentinfo()

p1.Eshansfamily("eshan", 19)
p1.Eshansfamily("hablu", 91)
p1.Eshansfamily("hablu", 91)
#output:
# my name is eshan, my age is 19
# my name is hablu, my age is 91

# Real Life:
# Admission Form থেকে Name নেওয়া।

#------------------------------------------
# Python OOP - Non-Parameterized Constructor
#------------------------------------------
# কনস্ট্রাক্টর (Constructor) হলো ক্লাসের একটি বিশেষ মেথড (__init__())
# যা অবজেক্ট তৈরি হওয়ার সাথে সাথে অটোমেটিক রান হয়।

# Non-Parameterized Constructor:
# যে কনস্ট্রাক্টরে self ছাড়া অন্য কোনো ভ্যালু পাঠাতে হয় না।

# কেন ব্যবহার করি?
# - অবজেক্ট তৈরি হওয়ার সাথে সাথে ডিফল্ট কাজ চালাতে
# - শুরুতে কিছু ডেটা সেট করতে
# - একই ইনিশিয়ালাইজেশন বারবার না লিখতে

# কখন ব্যবহার করি?
# - যখন সব অবজেক্টের জন্য একই শুরুর ভ্যালু দরকার হয়
# - যখন ইউজারের ইনপুট ছাড়াই কাজ শুরু করা যায়

# কিভাবে ব্যবহার করি?
# - ক্লাসের ভিতরে __init__() লিখি
# - শুধু self ব্যবহার করি
# - অবজেক্ট তৈরি করলেই অটোমেটিক কল হয়

# Real Life Example:
# নতুন মোবাইল চালু করলে ডিফল্ট ভাষা, সময়, সেটিং অটোমেটিক লোড হয়।
class Mobile:
    def __init__(self):
        print("Mobile is turned on")
        print("Default settings loaded")

m1 = Mobile()

# Output:
# Mobile is turned on
# Default settings loaded

# আরেকটি Example
class Student:
    def __init__(self):
        self.name = "Hablu"
        self.age = 20

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student()
s1.show()

# Output:
# Name: Hablu
# Age: 20

# ব্যাখ্যা:
# __init__() → Constructor Method
# Constructor → অবজেক্ট তৈরি হওয়ার সাথে সাথে অটোমেটিক রান হয়
# self → বর্তমান অবজেক্টকে নির্দেশ করে
# show() → অবজেক্টের ডেটা দেখানোর জন্য Method
# Student() → অবজেক্ট তৈরি করেছে
# s1 → Student ক্লাসের Object
# এখানে self ছাড়া অন্য কোনো Parameter নেই
# তাই এটি Non-Parameterized Constructor
# s1 = Student() লিখার সাথে সাথে __init__() অটোমেটিক কল হয়েছে
# এরপর s1.show() দিয়ে ডেটা দেখানো হয়েছে

# ==========================================================
# 3. Multiple Parameter Constructor
# ==========================================================

# একাধিক Data গ্রহণ করে।

class Student:

    def __init__(self, name, age):

        self.name = name

        self.age = age

student_1 = Student("Hasan", 20)

print(student_1.name)

print(student_1.age)

# Output:

# Hasan
# 20

# Real Life:

# University Admission

# Name
# Age
# Department

# সব তথ্য একসাথে নেওয়া।

# ==========================================================
# Constructor ছাড়া Example
# ==========================================================

class Student:

    pass

student_1 = Student()

student_1.name = "Hasan"

print(student_1.name)

# Output:

# Hasan

# কাজ করবে,
# কিন্তু অনেক Object হলে বারবার Value দিতে হবে।

# ==========================================================
# Constructor ব্যবহার করলে
# ==========================================================

class Student:

    def __init__(self, name):

        self.name = name

student_1 = Student("Hasan")

student_2 = Student("Rahim")

student_3 = Student("Karim")

print(student_1.name)

print(student_2.name)

print(student_3.name)

# Output:

# Hasan
# Rahim
# Karim

# ==========================================================
# Constructor-এর ভিতরে Variable তৈরি
# ==========================================================

class Mobile:

    def __init__(self, brand, ram):

        self.brand = brand

        self.ram = ram

mobile_1 = Mobile("Samsung", "8GB")

print(mobile_1.brand)

print(mobile_1.ram)

# Output:

# Samsung
# 8GB

# ==========================================================
# সবচেয়ে গুরুত্বপূর্ণ বিষয়
# ==========================================================

# def __init__(self, name):

# __init__()
# = Constructor

# self
# = বর্তমান Object

# name
# = Parameter

# self.name
# = Object Variable (Attribute)

# ==========================================================
# Constructor কখন ব্যবহার হয়?
# ==========================================================

# ✔ Student Management System
# ✔ Bank Management System
# ✔ School Software
# ✔ Mobile App Development
# ✔ Game Development
# ✔ Web Development
# ✔ Real Life Data Store করার সময়

# ==========================================================
# One Line Definition
# ==========================================================

# Constructor (__init__) হলো Class-এর একটি Special Method,
# যা Object তৈরি হওয়ার সাথে সাথেই Automatically Run হয়
# এবং Object-এর প্রয়োজনীয় Data ও Setup প্রস্তুত করে।
# ==========================================================

# মনে রাখার শর্টকাট:

# Object Create
# ↓
# Constructor (__init__) Run
# ↓
# Variable Create
# ↓
# Object Ready

# Constructor-এর প্রধান কাজ:
# Object তৈরি হওয়ার সময় প্রয়োজনীয় Data ও Setup প্রস্তুত করা।

#class methode
#ক্লাস মেথড ইউজ করার আগে @classmethode  কল করতে হয় তার মানে আমি পাইথন কে বললাম যে আমি এখন ক্লাস মেথড নিয়ে কাজ করব
class fatherinfo:
    @classmethod
    def Myname(LMS):
        print("hello python")

p1 = fatherinfo()
p1.Myname()

#Instancemethode
# ১) Instance Method (ইনস্ট্যান্স মেথড)
# --------------------------------
# এটা হলো সবচেয়ে সাধারণ মেথড।

# • এটা অবজেক্ট (instance) তৈরি করে ব্যবহার করতে হয়।
# • প্রথম প্যারামিটার হিসেবে self থাকে।
# • self এর মাধ্যমে অবজেক্টের ভেতরের ডেটা ব্যবহার করা যায়।
# • সরাসরি ক্লাস (Parent/Class Name) দিয়ে কল করলে সাধারণত এরর আসে, কারণ self অটোমেটিক পাঠানোর জন্য অবজেক্ট দরকার হয়।

# সহজ কথা:
# অবজেক্ট তৈরি → তারপর মেথড কল → আউটপুট।
class classname:
  def instancemethod(self):
    print("hello instancemethode")
v1 = classname()
v1.instancemethod()

#classmethod
#ক্লাস মেথড ইউজ করার সময় @classmethod সাইন দিয়ে মেনশন করে নিতে হয় এটা করার পর যখনই আমরা কোন function or method  লিখব তখন সেটা অটোমেটিকলি classmethod এ রূপান্তর হবে এবং ক্লাস মেথডে কোন ফাংশন রূপান্তরিত হলে সেলফ এর পরিবর্তে সি এল এস নামে ডিফল্ট একটাপ্যারামিটার চলে আসবে
# ২) Class Method (ক্লাস মেথড)
# -----------------------------
# এটা পুরো ক্লাসের সাথে কাজ করে।

# • @classmethod লিখে আগে ডেকোরেট করতে হয়।
# • প্রথম প্যারামিটার হিসেবে cls থাকে।
# • cls মানে পুরো ক্লাসকে রেফার করে।
# • অবজেক্ট ছাড়াও সরাসরি Class Name দিয়ে কল করা যায়।
# • ক্লাসের তথ্য নিয়ে কাজ করার জন্য বেশি ব্যবহার হয়।

# সহজ কথা:
# ক্লাস দিয়েও কল করা যায়।
# অবজেক্ট দিয়েও কল করা যায়।
class yourinfo:
  @classmethod
  def classmethod(cls):
    print("This is class methode")


#classmethod to way print
#first way
yourinfo.classmethod()
#second way
z1 = yourinfo()
z1.classmethod()

#staticmethod
# মেথড ইউজ করার সময় @staticmethod সাইন দিয়ে মেনশন করে নিতে হয় এটা করার পর যখনই আমরা কোন function or method  লিখব তখন সেটা অটোমেটিকলি staticmethod এ রূপান্তর হবে 
# ক্লাস মেথড এবং স্ট্যাটিক মেথড অনেকটাই সিমিলার শুধুমাত্র ক্লাসের ভিতরে প্যারামিটার ইউজ করতে হয় এবং স্টার্টিং ম্যাথরের ভিতরে কোন প্যারামিটার ইউজ না করলেও চলে
# Static Method (স্ট্যাটিক মেথড)
# ---------------------------------
# এটা ক্লাসের ভেতরে থাকে কিন্তু ক্লাস বা অবজেক্টের ডেটার উপর নির্ভর করে না।

# • @staticmethod লিখে আগে ডেকোরেট করতে হয়।
# • self বা cls বাধ্যতামূলক না।
# • চাইলে প্যারামিটার নিতে পারে, চাইলে না-ও নিতে পারে।
# • সরাসরি Class Name দিয়ে কল করা যায়।
# • অবজেক্ট দিয়েও কল করা যায়।

# সহজ কথা:
# এটা ক্লাসের ভিতরে রাখা সাধারণ ফাংশনের মতো।

class myinfo:
    @staticmethod
    def staticmethod():
        print("This is staticmethod")

#staticmethod to way print
#first way
myinfo.staticmethod()
#second way
d1 = myinfo()
d1.staticmethod()

# পাইথনের OOP-এ Instance Method, Class Method, এবং Static Method — এই তিনটি খুব গুরুত্বপূর্ণ।

# ━━━━━━━━━━━━━━━━━━━━
# ১. Instance Method (ইনস্ট্যান্স মেথড)
# ━━━━━━━━━━━━━━━━━━━━

# কী?

# যে মেথড অবজেক্টের (instance) ডেটা নিয়ে কাজ করে তাকে Instance Method বলে।

# প্রথম প্যারামিটার হিসেবে self থাকে।

# Real Life Example:

# ধরো, একটি Student ক্লাস আছে। প্রত্যেক ছাত্রের নাম ও বয়স আলাদা। তাই নাম ও বয়স দেখানোর জন্য অবজেক্টের ডেটা দরকার।

# Python Example:

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show_info(self):
#         print(self.name, self.age)

# s1 = Student("Hasan", 20)
# s1.show_info()

# Output:

# Hasan 20

# কেন self লাগে?

# self বর্তমান অবজেক্টকে নির্দেশ করে।

# s1.show_info()

# Python ভিতরে ভিতরে এটাকে এভাবে চালায়:

# Student.show_info(s1)

# এখানে self = s1

# কখন ব্যবহার হয়?

# • অবজেক্টের ডেটা ব্যবহার করতে
# • অবজেক্টের ডেটা পরিবর্তন করতে
# • প্রতিটি অবজেক্টের জন্য আলাদা কাজ করতে

# ━━━━━━━━━━━━━━━━━━━━
# ২. Class Method (ক্লাস মেথড)
# ━━━━━━━━━━━━━━━━━━━━

# কী?

# যে মেথড ক্লাসের ডেটা নিয়ে কাজ করে তাকে Class Method বলে।

# Class Method ব্যবহারের আগে:

# @classmethod

# লিখতে হয়।

# প্রথম প্যারামিটার হিসেবে সাধারণত cls থাকে।

# @classmethod
# def my_method(cls):
#     pass

# Real Life Example:

# ধরো, একটি স্কুলে সব ছাত্রের জন্য একই School Name আছে। এটি কোনো নির্দিষ্ট ছাত্রের তথ্য নয়, বরং পুরো ক্লাসের তথ্য।

# Python Example:

# class Student:

#     school = "ABC High School"

#     @classmethod
#     def show_school(cls):
#         print(cls.school)

# Student.show_school()

# Output:

# ABC High School

# কেন cls লাগে?

# cls পুরো ক্লাসকে নির্দেশ করে।

# Student.show_school()

# Python ভিতরে ভিতরে এটাকে এভাবে চালায়:

# Student.show_school(Student)

# এখানে:

# cls = Student

# কখন ব্যবহার হয়?

# • Class Variable ব্যবহার করতে
# • Class Variable পরিবর্তন করতে
# • Alternative Constructor বানাতে
# • পুরো ক্লাসের তথ্য নিয়ে কাজ করতে

# ━━━━━━━━━━━━━━━━━━━━
# ৩. Static Method (স্ট্যাটিক মেথড)
# ━━━━━━━━━━━━━━━━━━━━

# কী?

# যে মেথড না অবজেক্টের ডেটা ব্যবহার করে, না ক্লাসের ডেটা ব্যবহার করে, তাকে Static Method বলে।

# Static Method ব্যবহারের আগে:

# @staticmethod

# লিখতে হয়।

# এখানে self বা cls লাগে না।

# Real Life Example:

# ধরো, তুমি দুইটি সংখ্যার যোগফল বের করবে। এর জন্য কোনো Object বা Class Data দরকার নেই।

# Python Example:

# class Calculator:

#     @staticmethod
#     def add(a, b):
#         return a + b

# print(Calculator.add(5, 3))

# Output:

# 8

# কেন self বা cls লাগে না?

# কারণ এটি কোনো Object Data বা Class Data ব্যবহার করছে না। এটি শুধু নিজের কাজ করছে।

# কখন ব্যবহার হয়?

# • Utility Function বানাতে
# • Calculation করতে
# • Helper Function তৈরি করতে
# • এমন কাজের জন্য যেখানে Object বা Class Data দরকার নেই

# ━━━━━━━━━━━━━━━━━━━━
# তিনটির পার্থক্য
# ━━━━━━━━━━━━━━━━━━━━

# Instance Method:
# • Decorator লাগে না
# • প্রথম প্যারামিটার: self
# • Object Data নিয়ে কাজ করে

# Class Method:
# • @classmethod লাগে
# • প্রথম প্যারামিটার: cls
# • Class Data নিয়ে কাজ করে

# Static Method:
# • @staticmethod লাগে
# • self বা cls লাগে না
# • Object বা Class Data ছাড়া স্বাধীনভাবে কাজ করে

# ━━━━━━━━━━━━━━━━━━━━
# সহজ ট্রিক
# ━━━━━━━━━━━━━━━━━━━━

# self
# → Instance Method
# → বর্তমান Object নিয়ে কাজ করবে

# @classmethod + cls
# → Class Method
# → পুরো Class নিয়ে কাজ করবে

# @staticmethod
# → Static Method
# → Class-এর ভিতরে থাকবে, কিন্তু Class বা Object-এর কোনো Data ব্যবহার করবে না

# ━━━━━━━━━━━━━━━━━━━━
# এক লাইনে মনে রাখো
# ━━━━━━━━━━━━━━━━━━━━

# • self = Instance Method = Object-এর জন্য
# • @classmethod + cls = Class Method = Class-এর জন্য
# • @staticmethod = Static Method = স্বাধীন কাজের জন্য (self/cls ছাড়া)


#polymorphism
# পলিমরফিজম (Polymorphism)
# ------------------------
# Polymorphism শব্দের অর্থ হলো → “এক জিনিসের একাধিক রূপ” বা “একজন/একটি জিনিস পরিস্থিতি অনুযায়ী ভিন্নভাবে আচরণ করা”।

# রিয়াল লাইফ উদাহরণ:

# ধরো একজন মানুষ আছে।

# • তার সন্তানের কাছে → সে একজন বাবা
# • তার স্ত্রীর কাছে → সে একজন স্বামী
# • তার অফিসে → সে একজন কর্মচারী (Employee)
# • তার বাবা-মায়ের কাছে → সে একজন ছেলে
# • তার বন্ধুদের কাছে → সে একজন বন্ধু

# এখানে মানুষ কিন্তু একজনই।
# কিন্তু পরিস্থিতি ও সম্পর্ক অনুযায়ী তার পরিচয় বা আচরণ আলাদা দেখা যাচ্ছে।

# এটাই পলিমরফিজমের মূল ধারণা —
# একই জিনিস, কিন্তু ভিন্ন অবস্থায় ভিন্ন রূপ বা আচরণ।

# সহজ ভাষায়:
# “একই অবজেক্ট বা ব্যক্তি → একাধিকভাবে কাজ করতে পারে বা দেখা যেতে পারে।”

# মনে রাখার শর্ট লাইন:
# One Person → Many Roles
# একজন মানুষ → অনেক রূপ
# এটাই Polymorphism।

# যেমন:
# Vehicle নামে একটি Parent Class একবার তৈরি করা হয়েছে।
# এরপর Car, Plane, Bike ইত্যাদি Child Class সেই Vehicle Class-এর
# বৈশিষ্ট্য ব্যবহার করতে পারে এবং প্রয়োজনে নিজেদের মতো করে পরিবর্তনও করতে পারে।

# অর্থাৎ একবার Class তৈরি করে সেটিকে বিভিন্ন Object বা Child Class-এর মাধ্যমে
# বিভিন্নভাবে ব্যবহার করার ধারণাকেই Polymorphism বলা হয়।

# সহজ ভাষায়:
# "একটি নাম বা একটি Class, কিন্তু প্রয়োজন অনুযায়ী একাধিক রূপে কাজ করতে পারে।"
#আমরা একবার ক্লাস বা blue print তৈরি করেছি এটাকেই বারবার ইউজ করতে পারছি নিচে এক্সাম্পল:
class vehicle:
    def __init__(self, Model, Brand, component):
        self.Model = Model
        self.Brand = Brand
        self.component = component



class plane(vehicle):
        pass
p2 = plane("new update", "BMW", "all component")
print(p2.Model, p2.Brand, p2.component)
#next example
class car(vehicle):
    pass
c2 = car("Ar43", "Bugate", "Main component")
print(c2.Model, c2.Brand, c2.component)
#another example
class bike(vehicle):
    pass
# b2 = bike("sz400", "kawasaki ninza", "rass component")
# print(b2.Model, b2.Brand, b2.component)
# এবং চাইলেই মডেল ব্র্যান্ড কিবা কম্পনেন্ট এগুলোর ভ্যালু চেঞ্জ করা যায়
#valu change example
b2 = bike("sz400", "kawasaki ninza", "rass component")
#এখানে দেখো আমরা b2. মডেল ইকুয়াল টু আমরা মডেলকে এখন নিউ বাইক নাম দিয়েছি তাই এখন আউটপুট মডেল ইকুয়াল টু নিউ বাইক এসেছে এভাবে চাইলে প্রত্যেকটা বেলুড় মান চেঞ্জ করা যায় এবং নামও পরিবর্তন করা যায়
b2.Model = "new bike"
print(b2.Model)

#Python Encapsulation (oop)
# 🧠 Python Encapsulation (ইনক্যাপসুলেশন) কী?

# অনেকেই মনে করেন Encapsulation হ্যাকারদের থেকে কোড লুকানোর জন্য ব্যবহার করা হয়। কিন্তু আসলে Encapsulation-এর মূল উদ্দেশ্য হ্যাকারদের থেকে কোড লুকানো নয়।

# Encapsulation-এর প্রধান কাজ হলো:

# • Data সুরক্ষিত রাখা
# • Data-এর উপর নিয়ন্ত্রণ রাখা
# • বাইরের কেউ যেন ভুলভাবে Data পরিবর্তন করতে না পারে
# • Class-এর ভেতরের জটিল বিষয়গুলো লুকিয়ে রাখা
# • Clean এবং Secure Code লেখা

# সহজ ভাষায়:

# Encapsulation = Data Hiding + Controlled Access

# ━━━━━━━━━━━━━━━━━━━━
# 🏧 Real Life Example (ATM Booth)
# ━━━━━━━━━━━━━━━━━━━━

# ধরো তুমি ATM বুথ থেকে টাকা তুলতে গেলে।

# তুমি শুধু:

# • ATM Card Insert করো
# • PIN দাও
# • Amount লিখো

# কিন্তু ATM-এর ভিতরে:

# • Database কীভাবে কাজ করছে
# • Balance কীভাবে Check হচ্ছে
# • Server কীভাবে Connect হচ্ছে
# • Transaction কীভাবে Process হচ্ছে

# এসব কিছু তুমি দেখতে বা পরিবর্তন করতে পারো না।

# ATM তোমাকে শুধু প্রয়োজনীয় Interface দেয়।

# এটাই Encapsulation-এর বাস্তব উদাহরণ।

# ━━━━━━━━━━━━━━━━━━━━
# 🐍 Python Example
# ━━━━━━━━━━━━━━━━━━━━

# class BankAccount:

#     def __init__(self):
#         self.__balance = 5000

#     def show_balance(self):
#         print("Balance:", self.__balance)

# account = BankAccount()

# account.show_balance()

# Output:

# Balance: 5000
#another example:
class vehicle:
    def __init__(self, Model, Brand, component):
        self.Model = Model
        self.Brand = Brand
        self.component = component\

v1 = vehicle("new vec", "new model", "new component")
print(v1.Model)
#output:new vec
#when change the value
v1.Model = "new car"
print(v1.Model)
#output:new car

# এখন যদি কেউ সরাসরি Balance Access করতে চায়:

# print(account.__balance)

# তাহলে:

# AttributeError

# আসবে।

# কারণ __balance একটি Private Variable হিসেবে ব্যবহৃত হয়েছে।

# ━━━━━━━━━━━━━━━━━━━━
# 🔹 Single Underscore (_)
# ━━━━━━━━━━━━━━━━━━━━

# class Student:

#     def __init__(self):
#         self._name = "Hasan"

# এখানে:

# _name

# মানে:

# "এটি Internal Variable, সরাসরি ব্যবহার না করাই ভালো।"

# এটি শুধুমাত্র একটি Convention।

# Python এটিকে সত্যিকারের Private বানায় না।

# তাই Access করা যায়:

# print(student._name)

# ━━━━━━━━━━━━━━━━━━━━
# 🔹 Double Underscore (__)
# ━━━━━━━━━━━━━━━━━━━━

# class Student:

#     def __init__(self):
#         self.__name = "Hasan"

# এখানে:

# __name

# Private Variable-এর মতো আচরণ করে।

# Python Name Mangling ব্যবহার করে Variable-এর নাম পরিবর্তন করে ফেলে, তাই সরাসরি Access করা যায় না।

# ━━━━━━━━━━━━━━━━━━━━
# 🔹 Variable Encapsulation
# ━━━━━━━━━━━━━━━━━━━━

# class Student:

#     def __init__(self):
#         self.__name = "Hasan"

#     def show_name(self):
#         print(self.__name)

# s = Student()

# s.show_name()

# Output:

# Hasan

# ━━━━━━━━━━━━━━━━━━━━
# 🔹 Method Encapsulation
# ━━━━━━━━━━━━━━━━━━━━

# Method-এর ক্ষেত্রেও Encapsulation ব্যবহার করা যায়।

# class Student:

#     def __private_method(self):
#         print("Private Method")

#     def call_method(self):
#         self.__private_method()

# s = Student()

# s.call_method()

# Output:

# Private Method

# ━━━━━━━━━━━━━━━━━━━━
# 🔹 Function-কে Encapsulation করা যায়?
# ━━━━━━━━━━━━━━━━━━━━

# Class-এর ভিতরের Method-কে Encapsulation করা যায়।

# যেমন:

# class Student:

#     def __show(self):
#         pass

# কিন্তু Class-এর বাইরে থাকা সাধারণ Function:

# def hello():
#     pass

# এগুলোর ক্ষেত্রে সাধারণত Encapsulation ব্যবহার করা হয় না।

# ━━━━━━━━━━━━━━━━━━━━
# 🔹 Class-কে Encapsulation করা যায়?
# ━━━━━━━━━━━━━━━━━━━━

# সরাসরি পুরো Class-কে Private করার ধারণা Python-এ সাধারণভাবে ব্যবহার করা হয় না।

# যেমন:

# class __Student:
#     pass

# এভাবে লিখলেও Class সত্যিকারের Private হয়ে যায় না।

# বাস্তবে Encapsulation সাধারণত:

# • Variables
# • Methods

# এর উপর ব্যবহার করা হয়।

# ━━━━━━━━━━━━━━━━━━━━
# 🎯 Encapsulation কেন ব্যবহার হয়?
# ━━━━━━━━━━━━━━━━━━━━

# ১. Data Protection

# self.__balance

# এর মতো Variable বাইরে থেকে সরাসরি পরিবর্তন করা কঠিন হয়।

# ২. Better Security

# ভুলভাবে Data পরিবর্তনের ঝুঁকি কমে।

# ৩. Controlled Access

# deposit()
# withdraw()
# show_balance()

# এর মতো Method-এর মাধ্যমে Data ব্যবহার করা যায়।

# ৪. Clean Code

# ভেতরের Logic লুকিয়ে রাখা যায় এবং Code আরও Organized হয়।

# ━━━━━━━━━━━━━━━━━━━━
# 📝 সহজ ট্রিক
# ━━━━━━━━━━━━━━━━━━━━

# Public Variable

# name = "Hasan"

# ➡ সবাই Access করতে পারবে।

# Single Underscore

# _name = "Hasan"

# ➡ Internal Use (Convention Only)

# Double Underscore

# __name = "Hasan"

# ➡ Private-এর মতো আচরণ করবে।

# ━━━━━━━━━━━━━━━━━━━━
# ⚠ গুরুত্বপূর্ণ বিষয়
# ━━━━━━━━━━━━━━━━━━━━

# Python-এর __variable সম্পূর্ণ Security দেয় না।

# এটি মূলত:

# • Accidental Access রোধ করে
# • Code-এর Structure বজায় রাখে
# • Data-এর উপর নিয়ন্ত্রণ রাখতে সাহায্য করে

# তাই Encapsulation-কে "হ্যাকার থেকে কোড লুকানোর ব্যবস্থা" না ভেবে "Data Protection এবং Controlled Access-এর ব্যবস্থা" হিসেবে মনে রাখা সবচেয়ে সঠিক।

# ━━━━━━━━━━━━━━━━━━━━
# 📌 এক লাইনে মনে রাখো
# ━━━━━━━━━━━━━━━━━━━━

Encapsulation হলো Class-এর Data এবং Method-কে সুরক্ষিত রাখা এবং বাইরের Access নিয়ন্ত্রণ করা, যাতে Data সরাসরি পরিবর্তন না হয়ে নির্দিষ্ট Method-এর মাধ্যমে ব্যবহার করা যায়।