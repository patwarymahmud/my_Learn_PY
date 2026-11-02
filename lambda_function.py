# Lambda Function in Python
#পাইথনে Lambda Function হচ্ছে একটা ছোট, নামবিহীন (anonymous) ফাংশন।মানে, আমরা সাধারণত def দিয়ে যেভাবে ফাংশন লিখি, Lambda Function সেখানে এক লাইনে দ্রুত ছোট ফাংশন তৈরি করার জন্য ব্যবহার করা হয়।
#প্রথমে def  দিয়ে কাজ করেexample  দিয়ে তিন থেকে চার লাইনের লেগে গেল এবং পরে lambda   example দিয়ে মাত্র দুই লাইনে এসে কাজ kora  হয়ে গেল এটাই lambda ,কোন কাজকে ছোট করে আনার জন্য lambda function ব্যবহার করা হয়। যেমন, আমরা যদি একটা ফাংশন লিখতে চাই যা একটি সংখ্যাকে jog করে, তাহলে আমরা def দিয়ে লিখতে পারি:
def Hablu(a, b):
    sum = a + b
print(sum)
Hablu(5, 3)
# Output: 8

# কিন্তু একই কাজ আমরা lambda function দিয়ে করতে পারি এক লাইনে:
add = lambda a, b: a + b
print(add(5, 3))
# Output: 8

# ================================
# Python Lambda Function
# ================================
# Lambda Function হচ্ছে পাইথনের একটি ছোট Anonymous Function।
# অর্থাৎ, এটি এমন একটি function যার সাধারণত আলাদা নাম থাকে না।
# Lambda Function এক লাইনে দ্রুত ছোট function তৈরি করার জন্য ব্যবহার করা হয়।
# =========================================
# Lambda Function এর Syntax
# =========================================
# lambda arguments : expression

# Example:
x = lambda a: a * 2
print(x(5))
# Output:
# 10

# =========================================
# Normal Function vs Lambda Function
# =========================================
# Normal Function
def add(a, b):
    return a + b
print(add(5, 3))
# Output:
# 8
#another difference lambda example
#এখানে যোগ বিয়োগ গুন ভাগ সবই করা যাবে
x = lambda a,b,c,d: (a + b) / (c - d)
print(x(10, 20, 20, 5))
# Output:
# 2.0

# একই কাজ Lambda Function দিয়ে
add2 = lambda a, b: a + b
print(add2(5, 3))
# Output:
# 8

# =========================================
# Lambda Function কেন ব্যবহার করা হয়?
#=========================================
# 1. ছোট function দ্রুত লেখার জন্য
# 2. এক লাইনের function তৈরির জন্য
# 3. Temporary function বানানোর জন্য
# 4. map(), filter(), sorted() এর সাথে বেশি ব্যবহার হয়

# =========================================
# Lambda + map()
# =========================================
# map() প্রতিটি item এর উপর কাজ করে এবং একটি নতুন list তৈরি করে
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)
# Output:
# [2, 4, 6, 8]

# =========================================
# Lambda + filter()
# =========================================
# filter() condition অনুযায়ী data filter করে
numbers2 = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers2))
print(even_numbers)
# Output:
# [2, 4, 6]

# =========================================
# Lambda + sorted()
# =========================================
students = [
    ("Rahim", 80),
    ("Karim", 65),
    ("Sabbir", 90)
]
result2 = sorted(students, key=lambda x: x[1])
print(result2)
# Output:
# [('Karim', 65), ('Rahim', 80), ('Sabbir', 90)]

# =========================================
# Lambda Function কখন ব্যবহার হয়?
# =========================================
# Lambda Function ব্যবহার হয় যখন:
# 1. Function ছোট হয়
# 2. এক লাইনের logic দরকার হয়
# 3. Temporary কাজ করতে হয়
# 4. Code ছোট রাখতে চাই
# 5. map(), filter(), sorted() ব্যবহার করি

# =========================================
# Lambda Function এর সুবিধা
# =========================================
# 1. Code ছোট হয়
# 2. দ্রুত লেখা যায়
# 3. Temporary function তৈরি করা যায়

# =========================================
# Lambda Function এর অসুবিধা
# =========================================
# 1. বড় logic লেখা কঠিন
# 2. Complex code বুঝতে কষ্ট হয়
# 3. বেশি বড় Lambda readable না

# =========================================
# আরেকটি ছোট Example
# =========================================
square = lambda x: x * x
print(square(5))
# Output:
# 25

# =========================================
# সংক্ষেপে
# =========================================
# Lambda Function =
# ছোট One Line Function
# এটি ব্যবহার হয়:
# map()
# filter()
# sorted()
# ছোট logic দ্রুত লেখার জন্য Lambda খুব উপকারী।