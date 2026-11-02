# =========================================
# Python Scope (Real Life Example)
# =========================================

# Scope মানে হলো:
# একটি Variable কোথায় তৈরি হয়েছে এবং
# কোথায় কোথায় ব্যবহার করা যাবে।

# Python Scope মূলত ২ ধরনের:
#
# 1. Global Scope
# 2. Local Scope
#
# (আরও Enclosing এবং Built-in Scope আছে,
# কিন্তু Beginner হিসেবে আগে Global এবং Local
# ভালোভাবে বুঝলেই যথেষ্ট।)

# =========================================
# Global Scope (সরকারি ব্রিজ)
# =========================================

# Real Life Example:
#
# ধরো একটি সরকারি ব্রিজ আছে।
#
# এই ব্রিজ:
# - তুমি ব্যবহার করতে পারো
# - আমি ব্যবহার করতে পারি
# - গ্রামের মানুষ ব্যবহার করতে পারে
# - শহরের মানুষ ব্যবহার করতে পারে
#
# অর্থাৎ সবাই ব্যবহার করতে পারে।
#
# Python এ Global Variable ঠিক এমনই।

country = "Bangladesh"

def student():
    print(country)

def teacher():
    print(country)

student()
teacher()
print(country)

# এখানে country Variable
# সবার জন্য উন্মুক্ত।
#
# কারণ এটি Function এর বাইরে তৈরি হয়েছে।

# =========================================
# Local Scope (তোমার ব্যক্তিগত রাস্তা)
# =========================================

# Real Life Example:
#
# ধরো তোমার বাড়ির ভেতরে একটি ব্যক্তিগত রাস্তা আছে।
#
# এই রাস্তা:
# - শুধু তুমি ব্যবহার করতে পারো
# - বাইরের মানুষ ব্যবহার করতে পারে না
#
# Python এ Local Variable ঠিক এমনই।

def home():
    room_key = "1234"

    print(room_key)

home()

# এটা কাজ করবে।

# কিন্তু নিচের লাইন কাজ করবে না।

# print(room_key)

# কারণ room_key শুধু home()
# Function এর ভিতরের জন্য তৈরি হয়েছে।

# =========================================
# কী Error আসবে?
# =========================================

# print(room_key)

# Output:

# NameError:
# name 'room_key' is not defined

# =========================================
# কেন Error আসে?
# =========================================

# Python বাইরে room_key খুঁজবে।
#
# কিন্তু room_key Function এর ভিতরে ছিল।
#
# তাই Python বলবে:
#
# "আমি এই Variable চিনি না।"

# =========================================
# Global Variable Function এর ভিতরে ব্যবহার
# =========================================

name = "Hasan"

def show():
    print(name)

show()

# কাজ করবে।
#
# কারণ Global Variable
# Function এর ভিতরে ব্যবহার করা যায়।

# =========================================
# Local Variable Function এর বাইরে ব্যবহার
# =========================================

def student():
    age = 20

print(age)

# Error দিবে।

# কারণ age শুধুমাত্র
# student() Function এর ভিতরে আছে।

# =========================================
# Beginner Rule
# =========================================

# Function এর বাইরে Variable তৈরি করলে
# সেটি Global Variable।

# Function এর ভিতরে Variable তৈরি করলে
# সেটি Local Variable।

# =========================================
# খুব সহজে মনে রাখার উপায়
# =========================================

# Global Scope
#
# সরকারি ব্রিজের মতো।
#
# সবাই ব্যবহার করতে পারে।

# Local Scope
#
# তোমার ব্যক্তিগত রাস্তার মতো।
#
# শুধু নির্দিষ্ট Function ব্যবহার করতে পারে।

# =========================================
# One Line Definition
# =========================================

# Global Scope:
# Function এর বাইরে তৈরি Variable,
# যা প্রোগ্রামের অনেক জায়গা থেকে
# ব্যবহার করা যায়।

# Local Scope:
# Function এর ভিতরে তৈরি Variable,
# যা শুধুমাত্র ওই Function এর ভিতরেই
# ব্যবহার করা যায়।


# =========================================
# Python Enclosing Scope & Built-in Scope
# =========================================

# Python Scope মোট ৪ প্রকার:
#
# 1. Local Scope
# 2. Enclosing Scope
# 3. Global Scope
# 4. Built-in Scope
#
# এখানে আমরা Enclosing Scope এবং Built-in Scope
# সম্পর্কে জানবো।

# =========================================
# 1. Enclosing Scope
# =========================================

# Real Life Example:
#
# ধরো:
#
# বাংলাদেশ = Global
# জেলা = Enclosing
# বাড়ি = Local
#
# বাড়ির লোকেরা জেলার অফিসের কিছু সুবিধা
# ব্যবহার করতে পারে।
#
# কিন্তু বাইরের সবাই পারে না।
#
# Python এও ঠিক এমন হয়।

def district():

    district_name = "Chandpur"  # Enclosing Variable

    def village():
        print(district_name)

    village()

district()

# =========================================
# Output:
# =========================================

# Chandpur

# =========================================
# এখানে কী ঘটলো?
# =========================================

# district() Function এর ভিতরে
# district_name Variable তৈরি হয়েছে।

# district_name = "Chandpur"

# এরপর district() Function এর ভিতরে
# আরেকটি Function তৈরি করা হয়েছে।

# def village():

# village() Function এর ভিতরে
# district_name Variable ব্যবহার করা হয়েছে।

# print(district_name)

# Python প্রথমে village() এর ভিতরে Variable খুঁজবে।

# সেখানে না পেলে district() Function এর ভিতরে খুঁজবে।

# district() Function এর ভিতরে
# district_name Variable পাওয়া গেছে।

# তাই Output এসেছে:

# Chandpur

# =========================================
# Real Life Explanation
# =========================================

# ধরো:
#
# জেলা অফিসে একটি ফাইল আছে।
#
# ইউনিয়ন অফিস সেই ফাইল দেখতে পারে।
#
# কিন্তু রাস্তার যেকোনো মানুষ
# সেই ফাইল দেখতে পারে না।
#
# Enclosing Scope ঠিক এমন।

# =========================================
# 2. Built-in Scope
# =========================================

# Real Life Example:
#
# ধরো বাংলাদেশের কিছু আইন আছে।
#
# এই আইন:
# - সব জেলায় চলে
# - সব গ্রামে চলে
# - সবাই ব্যবহার করতে পারে
#
# এগুলো কারো ব্যক্তিগত নয়।
#
# Python এর Built-in Function গুলোও
# ঠিক এমন।

# Python এর কিছু Built-in Function:

print()
len()
type()
input()

# এগুলো Python আগে থেকেই তৈরি করে রেখেছে।

# =========================================
# Example:
# =========================================

name = "Hasan"

print(len(name))

# =========================================
# Output:
# =========================================

# 5

# =========================================
# এখানে কী ঘটলো?
# =========================================

# name Variable এর ভিতরে আছে:

# "Hasan"

# len() Function String এর
# Character সংখ্যা গুনে।

# H = 1
# a = 2
# s = 3
# a = 4
# n = 5

# মোট Character = 5

# তাই Output:

# 5

# =========================================
# আরও Example:
# =========================================

fruit = "Mango"

print(len(fruit))

# Output:
#
# 5

# কারণ:
#
# M = 1
# a = 2
# n = 3
# g = 4
# o = 5

# =========================================
# List এর ক্ষেত্রেও len() কাজ করে
# =========================================

fruits = ["Apple", "Banana", "Mango"]

print(len(fruits))

# Output:
#
# 3

# কারণ List এর ভিতরে
# 3টি Item আছে।

# =========================================
# Built-in Scope এর মূল বিষয়
# =========================================

# len() Function তুমি তৈরি করো নি।
#
# print() Function তুমি তৈরি করো নি।
#
# input() Function তুমি তৈরি করো নি।
#
# type() Function তুমি তৈরি করো নি।
#
# Python আগে থেকেই এগুলো তৈরি করে রেখেছে।
#
# তাই এগুলোকে Built-in Function বলা হয়।

# =========================================
# LEGB Rule
# =========================================

# Python Variable খোঁজে এই ক্রমে:

# L = Local
# E = Enclosing
# G = Global
# B = Built-in

# =========================================
# Example:
# =========================================

name = "Global"

def outer():

    name = "Enclosing"

    def inner():

        name = "Local"

        print(name)

    inner()

outer()

# Output:
#
# Local

# কারণ Python প্রথমে Local Scope এ খুঁজে।

# না পেলে Enclosing Scope এ খুঁজে।

# না পেলে Global Scope এ খুঁজে।

# না পেলে Built-in Scope এ খুঁজে।

# =========================================
# One Line Definition
# =========================================

# Enclosing Scope:
# একটি Function এর ভিতরের আরেকটি Function
# বাইরের Function এর Variable ব্যবহার করতে পারে।

# Built-in Scope:
# Python এর আগে থেকেই তৈরি করা Function,
# Variable এবং Object গুলোর Scope।