#Python recursion 
#পাইথনে রিকার্শন তৈরি করার জন্য সাধারণত প্রথমে def keyword ব্যবহার করে একটি function তৈরি করতে হয়। কারণ রিকার্শন মূলত একটি function নিজেই নিজেকে call করে।
#পাইথন recurtion  হল একটা ফাংশন যেটা নিজেই নিজেকে কল করে যেমনটা নিচের উদাহরণে দেখা যাচ্ছে। এই ফাংশনটি নিজেই নিজেকে কল করে চলতে থাকবে যতক্ষণ না আমরা কোনরকম ব্রেক পয়েন্ট ব্যবহার করি বা কোন শর্ত পূরণ হয়। এই উদাহরণে আমরা একটি ফাংশন তৈরি করেছি যার নাম "Refun" এবং এই ফাংশনটি নিজেই নিজেকে কল করে চলতে থাকবে। যখন আমরা "Refun()" কল করি, তখন এটি প্রথমে "This is a recursive function" প্রিন্ট করবে এবং তারপর আবার নিজেই নিজেকে কল করবে। এই প্রক্রিয়া অবিরত চলতে থাকবে যতক্ষণ না আমরা কোন ব্রেক পয়েন্ট ব্যবহার করি বা কোন শর্ত পূরণ হয়। এই উদাহরণটি একটি অসীম রিকার্শন তৈরি করে যা শেষ না হওয়া পর্যন্ত চলতে থাকবে। তাই এই ধরনের রিকার্শন ব্যবহার করার সময় সতর্ক থাকা উচিত এবং ব্রেক পয়েন্ট বা শর্ত ব্যবহার করা উচিত যাতে এটি অবিরত না হয়। recursion হল একটি শক্তিশালী প্রোগ্রামিং কৌশল যা জটিল সমস্যাগুলিকে সহজে সমাধান করতে সাহায্য করে, তবে এটি সঠিকভাবে ব্যবহৃত না হলে এটি অসীম লুপ তৈরি করতে পারে এবং প্রোগ্রাম ক্র্যাশ করতে পারে। তাই রিকার্শন ব্যবহার করার সময় সতর্ক থাকা উচিত এবং ব্রেক পয়েন্ট বা শর্ত ব্যবহার করা উচিত যাতে এটি অবিরত না হয়। recursion limit হল 1000, অর্থাৎ একটি ফাংশন নিজেই নিজেকে 1000 বার কল করতে পারে, তার পরে এটি "RecursionError: maximum recursion depth exceeded" ত্রুটি দেখাবে। তাই রিকার্শন ব্যবহার করার সময় সতর্ক থাকা উচিত এবং ব্রেক পয়েন্ট বা শর্ত ব্যবহার করা উচিত যাতে এটি অবিরত না হয়।
def Refun():
    print("This is a recursive function")
    Refun()
Refun()
# =========================================
# পাইথন রেকারশন (Python Recursion)
# =========================================
# রেকারশন কী?
# -----------------------------------------
# যখন একটি function নিজেকেই আবার call করে,
# তখন তাকে Recursion বলে।

# Example:
def hello():
    print("Hello")
    hello()
# এখানে hello() function আবার নিজেকেই call করছে।

# =========================================
# Base Case কী?
# =========================================
# Base Case হলো এমন condition
# যেখানে recursion থেমে যায়।
# Base Case না থাকলে infinite recursion হবে।

# Example:
def countdown(n):
    # Base Case
    if n == 0:
        return
    print(n)
    # Recursive Call
    countdown(n - 1)
countdown(5)
# Output:
# 5
# 4
# 3
# 2
# 1

# =========================================
# Recursive Call কী?
# =========================================
# যখন function নিজের ভিতরে আবার নিজেকেই call করে,
# সেটাকে Recursive Call বলে।
# Example:
def test(n):
    if n == 0:
        return
    print(n)
    # নিচের লাইনটাই Recursive Call
    test(n - 1)
test(3)
# Output:
# 3
# 2
# 1


# =========================================
# Recursion Limit কত?
# =========================================
# পাইথনে default recursion limit প্রায় 1000
# recursion limit check করার কোড:
import sys
print(sys.getrecursionlimit())

# =========================================
# Recursion Limit Change করা
# =========================================
# recursion limit বাড়ানোর কোড:
import sys
sys.setrecursionlimit(2000)
# Warning:
# খুব বেশি limit দিলে program crash করতে পারে।

# =========================================
# Recursion Error
# =========================================
# Base Case না থাকলে এই error আসে:
# RecursionError:
# maximum recursion depth exceeded
# Example:
def loop():
    loop()
# loop()


# =========================================
# Recursion কেন ব্যবহার করা হয়?
# =========================================

# কারণ কিছু problem recursion দিয়ে
# অনেক সহজে solve করা যায়।
# যেমন:
# 1. Factorial
# 2. Fibonacci
# 3. Tree Traversal
# 4. Folder Search
# 5. Graph Traversal
# 6. Backtracking
# 7. Nested Data

# =========================================
# Factorial Example
# =========================================

# 5! = 5×4×3×2×1
def factorial(n):
    # Base Case
    if n == 1:
        return 1
    # Recursive Formula
    return n * factorial(n - 1)
print(factorial(5))
# Output:
# 120

# =========================================
# Fibonacci Example
# =========================================
# Fibonacci:
# 0 1 1 2 3 5 8 13

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
print(fib(6))
# Output:
# 8

# =========================================
# Countdown Example
# =========================================
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
countdown(10)
# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1

# =========================================
# Count Up Example
# =========================================
def countup(n):
    if n == 0:
        return
    countup(n - 1)
    print(n)
countup(5)
# Output:
# 1
# 2
# 3
# 4
# 5

# =========================================
# List এর সব element print করা
# =========================================
fruits = ["apple", "banana", "mango"]
def show(data, index):
    if index == len(data):
        return
    print(data[index])
    show(data, index + 1)
show(fruits, 0)
# Output:
# apple
# banana
# mango


# =========================================
# সব সংখ্যার যোগফল বের করা
# =========================================
def total(n):
    if n == 1:
        return 1
    return n + total(n - 1)
print(total(5))
# 5+4+3+2+1
# Output:
# 15

# =========================================
# Power বের করা
# =========================================
# 2^3 = 2×2×2
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)
print(power(2, 3))
# Output:
# 8

# =========================================
# String Reverse করা
# =========================================
def reverse(text):
    if len(text) == 0:
        return text
    return reverse(text[1:]) + text[0]
print(reverse("Python"))
# Output:
# nohtyP

# =========================================
# Nested List Count করা
# =========================================
data = [1, [2, 3], [4, [5, 6]]]
def count_items(lst):
    total = 0
    for item in lst:
        if type(item) == list:
            total += count_items(item)
        else:
            total += 1
    return total
print(count_items(data))
# Output:
# 6

# =========================================
# Call Stack কী?
# =========================================
# প্রত্যেক recursive call memory stack এ জমা হয়।
# Example:
# factorial(5)
# factorial(4)
# factorial(3)
# factorial(2)
# factorial(1)
# তারপর reverse order এ return হয়।

# =========================================
# Recursion এর সুবিধা
# =========================================
# 1. Code ছোট হয়
# 2. Code clean হয়
# 3. Complex problem সহজ হয়
# 4. Tree structure সহজ হয়
# 5. Backtracking এ useful
# 6. Nested data সহজে handle করা যায়

# =========================================
# Recursion এর অসুবিধা
# =========================================
# 1. বেশি memory লাগে
# 2. Function call বেশি হয়
# 3. Slow হতে পারে
# 4. Debug করা কঠিন
# 5. Infinite recursion হতে পারে
# 6. Recursion limit আছে

# =========================================
# কখন Recursion ব্যবহার করা ভালো?
# =========================================
# যখন:
# 1. Problem ছোট ছোট একই problem এ ভাগ করা যায়
# 2. Tree/Graph থাকে
# 3. Nested data থাকে
# 4. Backtracking দরকার হয়
# 5. Mathematical recursion থাকে
# 6. Code clean রাখতে হয়

# =========================================
# কখন Recursion ব্যবহার না করাই ভালো?
# =========================================
# যখন:
# 1. Loop দিয়েই সহজে করা যায়
# 2. অনেক deep recursion দরকার
# 3. Memory কম ব্যবহার করতে হবে
# 4. Speed বেশি দরকার

# =========================================
# Loop vs Recursion
# =========================================
# Loop:
# Fast
# কম memory লাগে
# Simple problem এ ভালো
# Recursion:
# একটু slow
# বেশি memory লাগে
# Complex problem এ ভালো

# =========================================
# Backtracking কী?
# =========================================
# Backtracking হলো:
# একটার পর একটা possibility check করা।
# Example:
# 1. Sudoku Solver
# 2. Maze Solver
# 3. N Queen Problem
# 4. Password Combination

# =========================================
# Tree Traversal কী?
# =========================================
# Tree structure এর সব node visit করা।
# এটা recursion ছাড়া অনেক কঠিন হয়ে যায়।

# =========================================
# File Folder Search
# =========================================
# Folder এর ভিতরে folder এর ভিতরে folder...
# এগুলো recursion দিয়ে search করা হয়।

# =========================================
# সবচেয়ে গুরুত্বপূর্ণ বিষয়
# =========================================
# Recursion বুঝতে হলে শিখতে হবে:
# 1. Base Case
# 2. Recursive Call
# 3. Call Stack
# 4. Return Value
# 5. Stack Overflow
# 6. Backtracking

# =========================================
# Short Definition
# =========================================
# Recursion হলো এমন একটি process
# যেখানে একটি function নিজেকেই call করে
# problem solve করে।

# =========================================
# পাইথন রেকারশন কোথায় বেশি ব্যবহার হয়?
# =========================================
# 1. Tree Structure
# ---------------------------------
# Tree এর node visit করতে recursion সবচেয়ে বেশি ব্যবহার হয়।
# Example:
# Binary Tree
# File Folder Structure
# HTML DOM Tree

# =========================================
# 2. Folder / File Search
# =========================================
# Folder এর ভিতরে আবার folder,
# তার ভিতরে আবার folder থাকলে
# recursion দিয়ে search করা সহজ হয়।
# Example:
# Computer File Explorer
# VS Code folder scan

# =========================================
# 3. Backtracking Problem
# =========================================
# একটার পর একটা possibility check করতে।
# Example:
# Sudoku Solver
# Maze Solver
# N Queen Problem
# Password Combination

# =========================================
# 4. Mathematical Problem
# =========================================
# যেসব problem নিজের ছোট version এ ভাগ হয়।
# Example:
# Factorial
# Fibonacci
# Power Calculation

# =========================================
# 5. Divide and Conquer Algorithm
# =========================================
# বড় problem কে ছোট problem এ ভাগ করে solve করতে।
# Example:
# Merge Sort
# Quick Sort

#condition ব্যবহার করে recursion limit কমানো হয় না।
# Condition ব্যবহার করে recursion থামানো হয়।
# আর আসল recursion limit change করা হয় sys.setrecursionlimit() দিয়ে।
# উদাহরণ:
import sys

# recursion limit কমানো
sys.setrecursionlimit(500)
print(sys.getrecursionlimit())
Output:
500

# আর condition দিয়ে recursion control করা হয়:
def test(n):

    # Condition
    if n == 0:
        return
    print(n)
    test(n - 1)
test(5)

# এখানে:
if n == 0:
    return
# এই condition recursion থামিয়ে দিয়েছে।
# মানে:
# sys.setrecursionlimit()
# --> recursion limit change করে
# if condition
# --> recursion কখন থামবে সেটা control করে
#দুটো আলাদা 

#advanced topic এখনো বাকি আছে, যেমন:
# Advanced Recursion Topics

# 1. Tail Recursion
# 2. Memoization
# 3. Dynamic Programming
# 4. Binary Tree DFS
# 5. Recursive Sorting
#    - Merge Sort
#    - Quick Sort
# 6. Graph DFS
# 7. Divide and Conquer
# 8. Recursive Lambda
# 9. Stack Memory Analysis
# 10. Time Complexity