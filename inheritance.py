# Inheritance in Python

# 🔹 Python Inheritance Real Life Example
# Parent Class = বাবা 👨
# Child Class = ছেলে 👦

# বাস্তব জীবনে যেমন ছেলে বাবার সম্পত্তি পায়,
# ঠিক তেমনি পাইথনে Child Class,
# Parent Class-এর method এবং attribute ব্যবহার করতে পারে।

# উদাহরণ:
# বাবার আছে:
# ✅ জমি
# ✅ বাড়ি

# ছেলে এগুলো inherit করে পেয়ে যায়।
# তাই ছেলে নিজে আবার জমি বা বাড়ির কোড না লিখলেও,
# সে সেগুলো ব্যবহার করতে পারে।
# এটাকেই Python-এ Inheritance বলে।

# Inheritance ব্যবহার করা হয়:
# ✅ একই কোড বারবার না লেখার জন্য
# ✅ Code Reusability এর জন্য
# ✅ Parent → Child relationship তৈরি করার জন্য
# ✅ বড় প্রজেক্ট সহজভাবে ম্যানেজ করার জন্য
      #Game Development 🎮
      # Web Development 🌐
      # AI Project 🤖
      # Software System 💻
# মূল Syntax:
# class Child(Parent):

# সহজভাবে:
# Inheritance = অন্য ক্লাসের ক্ষমতা ব্যবহার করা
#ইনহেরিটেন্স হচ্ছে একটি মাধ্যম যা ২ টি ক্লাসের মধ্যে সমঝোতা করে।
# # ""

#আমরা এখানে প্রথমে প্যারেন্ট  ক্লাসকে ডাকলাম এবং তার কাছে কী কী আছে তার সম্পদগুলো লেখলাম। তারপরে আমরা চাইল্ড ক্লাসকে ডাকলাম। চাইল্ড ক্লাসের ভেতরে ব্রোকেন ফোন আছে কিন্তু কোন ফোন সেটা লেখা নাই। ব্রোকেন বাড়ি আছে কিন্তু কোন বাড়ি সেটা লেখা নাই। এখানে চাইলে ব্রোকেন ফোন এখানে আমরা কোনো একটা ফোনের নাম ব্যবহার করতে পারি। ব্রোকেন হোমের ভেতরেও কোনো একটা বাড়ির নাম লিখতে পারি। তো এখানে আমরা চাইল ক্লাস son ke যখন ডাকলাম, তখন তার ভেতরে ( ) দিয়ে আমরা আমাদের প্যারেন্ট ক্লাসকেও এখানে ডাকলাম। প্যারেন্টস ক্লাসের নাম হচ্ছে father। তো ডাকার পর এখন আমরা তার যে সম্পদগুলো আছে, এখন sei সম্পদগুলো আমরা ইউজ করতে পারছি, তাকে এখানে কল করালো। তো এখানে আমরা তার পর print করেছি, এস ডট কার তার মাধ্যমে বাবার সম্পদের car আছে বিএমডব্লিউ, Tai সন এখানে বাবার সম্পদ use করছে এবং সে তার নিজের সম্পদ ব্যবহার,korte parbe jehetu তার নিজের সম্পদ। এখানে চাইল্ড ক্লাস হচ্ছে এমন একটা বিষয় যে তার নিজের সম্পদও ইউজ করতে পারে এবং প্যারেন্ট ক্লাসের সম্পদও ইউজ করতে  পারবে। তাই এখানে আমরা সন ডট কার এবং সন ডট টাকা কল করলাম, তাহলে সে আমাদের দেখাবে যে তার কাছে কার আছে বিএমডব্লিউ এবং টাকা আছে 1 কোটি টাকা। তো এই হচ্ছে ইনহেরিটেন্স এর একটা সহজ উদাহরণ। তবে প্যারেন্ট ক্লাস চাইল্ড ক্লাস এর সাম্পদ বা মান বা ভ্যালু use করতেপারে নাই।
# inheritance.py example with parent class and child class
class father:
   car = "BMW"
   taka = " 1 crore"
   home = "10 floors"


class son(father):   
   brokenphone = "nokia" 
   brokenhome = "0 home"
s = son()
print(s.car)
print(s.taka)
print(s.brokenphone)
print(s.brokenhome)

# Output:
# BMW
#  1 crore
# nokia
# 0 home

#python multiple inheritance example
class father:
   car = "BMW"
   taka = "1 crore"
   home = "10 floors"

class uncle:
   shop = "Clothing Shop"

class chacha:
   bike = "R15 Bike"

# Multiple Inheritance
class son(father, uncle, chacha):
   brokenphone = ""
   brokenhome = ""

s = son()

print(s.car)
print(s.taka)
print(s.home)
print(s.shop)
print(s.bike)
print(s.brokenphone)
print(s.brokenhome)
# Output:\
# BMW
# 1 crore
# 10 floors
# Clothing Shop
# R15 Bike
# 
# 

#python multilevel inheritance with real example
# ================================
# Python Multiple Inheritance
# ================================
# Multiple Inheritance মানে হলো:
# একটি Child Class একসাথে একাধিক Parent Class থেকে
# feature/property/method inherit করতে পারে।

# =========================================
# Real Life Example:
# =========================================
# ধরো বাস্তব জীবনে একজন ছেলে শুধু তার বাবার কাছ থেকেই না,
# বরং তার কাকা, চাচা সবার কাছ থেকেও কিছু না কিছু পেতে পারে।

# যেমন:
# বাবা -> জমি দিয়েছে
# কাকা -> দোকান দিয়েছে
# চাচা -> গাড়ি দিয়েছে

# এখন ছেলে সবার feature ব্যবহার করতে পারবে।
# Python এ এটাকেই Multiple Inheritance বলে।

# =========================================
# Example Code:
# =========================================
class Father:
    land = "10 বিঘা জমি"

class Uncle:
    shop = "কাপড়ের দোকান"

class Chacha:
    car = "Toyota Car"

# Son class একসাথে Father, Uncle, Chacha
# এই ৩টা class inherit করছে
class Son(Father, Uncle, Chacha):
    pass

# Object তৈরি
s = Son()

# সব Parent Class এর property access করা
print(s.land)
print(s.shop)
print(s.car)

# =========================================
# Output:
# =========================================
# 10 বিঘা জমি
# কাপড়ের দোকান
# Toyota Car

# =========================================
# এখানে কী ঘটলো?
# =========================================
# এই লাইনে:
# class Son(Father, Uncle, Chacha):

# এর মানে হলো:
# Son class একসাথে একাধিক class inherit করছে।

# তাই Son class এখন:
# Father এর land পাচ্ছে
# Uncle এর shop পাচ্ছে
# Chacha এর car পাচ্ছে

# এটাই Multiple Inheritance।

# =========================================
# Professional Real Example:
# =========================================
# Smartphone এর ভিতরে যেমন:
# Camera feature থাকে
# আবার Music Player feature ও থাকে

# Python এও Multiple Inheritance এমন কাজেই ব্যবহার হয়।
class Camera:
    def take_photo(self):
        print("Photo Taken")

class MusicPlayer:
    def play_music(self):
        print("Music Playing")

class Smartphone(Camera, MusicPlayer):
    pass

phone = Smartphone()

phone.take_photo()
phone.play_music()

# =========================================
# Output:
# =========================================
# Photo Taken
# Music Playing

# =========================================
# Summary:
# =========================================
# Single Inheritance:
# একটি Child Class -> একটি Parent Class inherit করে

# Multiple Inheritance:
# একটি Child Class -> একাধিক Parent Class inherit করে

# =========================================
# One Line Definition:
# =========================================
# Multiple Inheritance হলো এমন একটি system
# যেখানে একটি Child Class একসাথে একাধিক
# Parent Class থেকে feature inherit করতে পারে।