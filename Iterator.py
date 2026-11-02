# =========================================
# Python Iterator
# =========================================

# Iterator হলো এমন একটি Python object
# যেটা এক এক করে data (item) প্রদান করে।

# সহজ ভাষায়:
#
# ধরো একটি ঝুড়িতে ১০টা আম আছে।
# তুমি একবারে সব আম না নিয়ে
# একটি করে আম বের করছো।
#
# Iterator ঠিক এভাবেই
# একবারে একটি item প্রদান করে।

# =========================================
# Real Life Example
# =========================================

# ধরো তোমার কাছে ছাত্রদের একটি লিস্ট আছে।

students = ["Rahim", "Karim", "Sabbir"]

# এখন তুমি একবারে সব ছাত্রকে না দেখে
# একজন একজন করে দেখতে চাও।

it = iter(students)

print(next(it))
print(next(it))
print(next(it))

# =========================================
# Output:
# =========================================

# Rahim
# Karim
# Sabbir

# =========================================
# এখানে কী ঘটলো?
# =========================================

# iter(students)
#
# iter() function লিস্টকে
# Iterator এ রূপান্তর করেছে।

# next(it)
#
# next() function ব্যবহার করে
# Iterator থেকে পরবর্তী item বের করা হয়।

# প্রথম next()
# Rahim

# দ্বিতীয় next()
# Karim

# তৃতীয় next()
# Sabbir

# =========================================
# Data শেষ হয়ে গেলে
# =========================================

# যদি আবার next(it) চালাও

# print(next(it))

# তাহলে Python এরর দিবে:

# StopIteration

# কারণ Iterator এর ভিতরের
# সব data শেষ হয়ে গেছে।

# =========================================
# Iterator প্রিন্ট করার আরেকটি উপায়
# =========================================

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

# Output:
#
# Apple
# Banana
# Mango

# =========================================
# এখানে কী ঘটছে?
# =========================================

# for loop ভেতরে ভেতরে Iterator ব্যবহার করে।

# অর্থাৎ নিচের কোড:

it = iter(fruits)

print(next(it))
print(next(it))
print(next(it))

# এবং

for fruit in fruits:
    print(fruit)

# এই দুইটার কাজ মূলত একই।

# =========================================
# Iterator কখন বেশি ব্যবহার হয়?
# =========================================

# 1. Large Data Processing
# 2. File Reading
# 3. Database Records
# 4. API Data
# 5. Generator Functions
# 6. Memory Efficient Programming

# =========================================
# Iterator এর ২টি গুরুত্বপূর্ণ Function
# =========================================

# 1. iter()
# 2. next()

# iter() function:
#
# কোনো iterable object
# (list, tuple, string ইত্যাদি)
# কে Iterator এ রূপান্তর করে।

# next() function:
#
# next() function ব্যবহার করে
# Iterator থেকে পরবর্তী item বের করা হয়।

# =========================================
# One Line Definition
# =========================================

# Iterator হলো এমন একটি Python object
# যা next() function ব্যবহার করে
# এক এক করে data প্রদান করে এবং
# data শেষ হয়ে গেলে StopIteration
# exception দেয়।