#python multilevel inheritance example
# =========================================
# Python Multi-Level Inheritance
# =========================================

# Multi-Level Inheritance মানে হলো:
# একটি class আরেকটি class কে inherit করে,
# আবার সেই class কে আরেকটি class inherit করে।

# অর্থাৎ inheritance ধাপে ধাপে নিচে নামতে থাকে।

# =========================================
# Real Life Example:
# =========================================
# ধরো:
# Father এর কাছে আছে:
# - BMW Car
# - 10 Crore টাকা
#
# Son1 বাবার সব property inherit করলো।
# আবার Son1 এর নিজেরও আছে:
# - Gaming PC
#
# Son2 আবার Son1 কে inherit করলো।
# তাই Son2 এখন পাবে:
# - Father এর Car
# - Father এর টাকা
# - Son1 এর Gaming PC
#
# এরপর Son3 আবার Son2 কে inherit করলো।
# তাই Son3 এখন পাবে:
# - Father এর সব property
# - Son1 এর Gaming PC
# - Son2 এর Bike
# - নিজের Laptop
#
# এভাবেই inheritance ধাপে ধাপে নিচে নামতে থাকে।
#
# এটাই Multi-Level Inheritance।

# =========================================
# Example Code:
# =========================================
# Parent Class
class Father:
    car = "BMW"
    taka = "10 Crore"

# Father কে inherit করছে Son1
class Son1(Father):
    gaming_pc = "RTX Gaming PC"

# Son1 কে inherit করছে Son2
class Son2(Son1):
    bike = "R15 Bike"

# Son2 কে inherit করছে Son3
class Son3(Son2):
    laptop = "MacBook Pro"


# Object তৈরি
s = Son3()

# Father থেকে আসছে
print(s.car)
print(s.taka)

# Son1 থেকে আসছে
print(s.gaming_pc)

# Son2 থেকে আসছে
print(s.bike)

# Son3 এর নিজের
print(s.laptop)

# =========================================
# Output:
# =========================================
# BMW
# 10 Crore
# RTX Gaming PC
# R15 Bike
# MacBook Pro

# =========================================
# এখানে কী ঘটলো?
# =========================================
# Step 1:
# Father class এর ভিতরে car এবং taka আছে।

# Step 2:
# Son1(Father)
# মানে Son1 এখন Father এর সবকিছু inherit করছে।

# তাই Son1 এখন পাবে:
# - car
# - taka

# Step 3:
# Son2(Son1)
# মানে Son2 এখন Son1 কে inherit করছে।

# তাই Son2 এখন পাবে:
# - Father এর property
# - Son1 এর property

# Step 4:
# Son3(Son2)
# মানে Son3 এখন Son2 কে inherit করছে।

# আর যেহেতু Son2 আগে থেকেই Son1 কে inherit করেছে,
# এবং Son1 আবার Father কে inherit করেছে,
# তাই Son3 এখন সবার property access করতে পারছে।

# =========================================
# Inheritance Chain:
# =========================================
# Father -> Son1 -> Son2 -> Son3

# inheritance ধাপে ধাপে নিচে নামছে।

# =========================================
# Single vs Multiple vs Multi-Level
# =========================================
# Single Inheritance:
# এক Parent -> এক Child

# Multiple Inheritance:
# এক Child -> একাধিক Parent

# Multi-Level Inheritance:
# Parent -> Child -> Grand Child

# =========================================
# One Line Definition:
# =========================================
# Multi-Level Inheritance হলো এমন একটি system
# যেখানে একটি class অন্য class কে inherit করে,
# আবার সেই class কে আরেকটি class inherit করে।


#Python Hierarchical Inheritance
# =========================================
# Python Hierarchical or Hybrid Inheritance
# =========================================

# Hierarchical Inheritance মানে হলো:
# একটি Parent Class থেকে একাধিক Child Class
# inherit করে।

# =========================================
# Real Life Example:
# =========================================

# ধরো:
#
# Father এর কাছে আছে:
# - BMW Car
# - 10 Crore টাকা
# - 10 Floor Building
#
# Father এর ৩ জন ছেলে আছে:
#
# Son1
# Son2
# Son3
#
# তিনজনই Father এর সম্পত্তির উপর অধিকার রাখে।
#
# তাই Son1, Son2 এবং Son3
# সবাই Father এর property ব্যবহার করতে পারবে।
#
# তবে প্রত্যেকের নিজেরও কিছু property থাকতে পারে।

# =========================================
# Example Code:
# =========================================

# Parent Class
class Father:
    car = "BMW"
    taka = "10 Crore"
    home = "10 Floor Building"


# Child Class 1
class Son1(Father):
    laptop = "MacBook Pro"


# Child Class 2
class Son2(Father):
    bike = "R15 Bike"


# Child Class 3
class Son3(Father):
    phone = "iPhone"


# Object তৈরি
s1 = Son1()
s2 = Son2()
s3 = Son3()

# Son1
print(s1.car)
print(s1.taka)
print(s1.laptop)

# Son2
print(s2.car)
print(s2.taka)
print(s2.bike)

# Son3
print(s3.car)
print(s3.taka)
print(s3.phone)

# =========================================
# Output:
# =========================================

# BMW
# 10 Crore
# MacBook Pro
#
# BMW
# 10 Crore
# R15 Bike
#
# BMW
# 10 Crore
# iPhone

# =========================================
# Inheritance Structure:
# =========================================

#            Father
#          /    |    \
#         /     |     \
#      Son1   Son2   Son3

# =========================================
# এখানে কী ঘটলো?
# =========================================

# Father হলো Parent Class।

# Son1, Son2, Son3
# সবাই Father কে inherit করেছে।

# তাই তিনজনই Father এর:
# - car
# - taka
# - home

# ব্যবহার করতে পারছে।

# কিন্তু Son1 এর laptop,
# Son2 এর bike,
# Son3 এর phone
# অন্যরা ব্যবহার করতে পারবে না।

# =========================================
# One Line Definition:
# =========================================

# Hierarchical Inheritance হলো এমন একটি system
# যেখানে একটি Parent Class থেকে
# একাধিক Child Class inherit করে।

#Hybrid Inheritance হলো Hierarchical + Multiple Inheritance-এর মিশ্রণ। সাধারণত Python-এ Hybrid Inheritance শেখার আগে Single → Multiple → Multi-Level → Hierarchical ভালোভাবে বুঝে নেওয়া হয়। তারপর Hybrid অনেক সহজ লাগে।