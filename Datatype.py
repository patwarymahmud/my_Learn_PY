#Binary type data it is bytes.
from tkinter import END


Mdlist = [1, 3, 5, 55, 5, 64, 88, 255]
b = bytes(Mdlist)
print(type(b))
#Byte, and ByteArray, both have a range from (0) to (255).
# bytes → immutable
# ➜ মান change করা যায় না
# bytearray → mutable
# ➜ মান change করা যায়
#Binary type data it is bytearray.
Mdlist = [1, 3, 5, 55, 5, 64, 88, 255]
b1 = bytearray(Mdlist)
b[1] = 100
print(b1[1])

#none type data.
x = None
print(x)
print(type(x))

#list type data.
li = ["mahmud", "sojib", "arif", "muhammad"]
print(li)
print(type(li))

#There are two differences between list type data, and tuple type data. One is in brackets, and the other is, list type data is mutable, its variable value can be changed if desired. And tuple type data is immutable, its variable value cannot be changed even if desired.

#tuple type data.
tup = (5, 10, 15, 20)
print(tup)
print(type(tup))

#range type data.
ran = range(7)
print(ran)
for i in ran:
  print(i)

#🐍 Python Data Types (Complete Single Copy Block)
#কোন ডাটা টাইপের ক্লাস বা কোন ধরনের ডাটা টাইপ সেটা বের করার জন্য প্রিন্ট লিখে তার ভিতরে( )  টাইপ কিওয়ার্ড লিখেদিয়ে এবং তার ভেতরে আবার ( ) দিয়ে ওই ডাটা টাইপের ভেরিয়েবল কে প্রিন্ট করলেdata type  বা ক্লাস আসবে আউটপুট বেরিয়ে  আসবে
#example with string data type
hablu = "mahamud"
print(type(hablu))
#output:class, str

#1️⃣ Numeric Types
-----------------
int:
a = 20
Real life: মানুষের বয়স (20 বছর)

float:
price = 99.99
Real life: পণ্যের দাম (99.99 টাকা)

complex:
z = 3 + 4j
Real life: engineering/electrical signal calculation

--------------------------------------------------

#2️⃣ String Type (str)
---------------------
name = "Mahmud"
Real life: মানুষের নাম, বইয়ের নাম, ঠিকানা

--------------------------------------------------

#3️⃣ Boolean Type (bool)
-----------------------
is_student = True
is_login = False
Real life: Yes/No decision (ছাত্র কি না)

--------------------------------------------------

#4️⃣ Sequence Types
-------------------

list type data:
fruits = ["apple", "banana", "mango"]
Real life: shopping list (change করা যায়)
#list type data is mutable যার মান বা ভ্যালু caile add, or remove, or চেঞ্জ করা যায় 
tuple type data:
colors = ("red", "green", "blue")
Real life: fixed data (জন্ম তারিখ, fixed info)
#tuple type data is immutable যার মান বা ভ্যালু কখনোই চেঞ্জ করা যায় না
range type data:
numbers = range(5)
Real life: counting (0 to 4 sequence)
for i in numbers:
  print(i)
#output:
# 1
# 2
# 3
# 4
# 5
          
--------------------------------------------------

#5️⃣ Dictionary Type (dict)
--------------------------
student = {
    "name": "Mahmud",
    "age": 20,
    "city": "Chandpur"
}
Real life: ID card / profile data (key-value system)

--------------------------------------------------

#6️⃣ Set Types
-------------

set:
numbers = {1, 2, 3, 3}
Real life: unique roll numbers (duplicate allowed না)

frozenset:
fs = frozenset({1, 2, 3})
Real life: locked data (change করা যায় না)

--------------------------------------------------

#7️⃣ Binary Types
----------------

bytes:
b = b"Hello"
Real life: read-only file data

bytearray:
b = bytearray(5)
b[0] = 65
Real life: editable file data

memoryview:
data = bytearray(b"abc")
m = memoryview(data)
Real life: large file fast access / memory optimization

--------------------------------------------------

#8️⃣ None Type
# -------------
# x = None
# Real life: empty value / কিছু নেই

# --------------------------------------------------

# 9️⃣ Type Check
# --------------
# x = 10
# print(type(x))
# Real life: কোনো জিনিসের টাইপ চেক করা

--------------------------------------------------
# 🐍 Python Data Types — কিভাবে বুঝবো কোনটা কোন টাইপ (One Page Guide)
# 👉 মূল কথা:
# Python এ data type চেনা হয় "কিভাবে লেখা হয়েছে" এবং "কি বৈশিষ্ট্য আছে" তার উপর।

--------------------------------------------------

#1️⃣ LIST (লিস্ট) — কেন লিস্ট?

✔ লেখা হয়: []
✔ একাধিক ডাটা থাকে
✔ পরিবর্তন করা যায় (mutable)

👉 Example:
fruits = ["apple", "banana", "mango"]

👉 কেন এটা list?
- [] ব্যবহার করা হয়েছে
- একাধিক item আছে
- item add/remove করা যায়

👉 Real life:
Shopping list → যেটা পরিবর্তন হয় (কিছু add/delete করা যায়)

--------------------------------------------------

2️⃣ TUPLE (টিউপল) — কেন টিউপল?

✔ লেখা হয়: ()
✔ একাধিক ডাটা থাকে
✔ কিন্তু পরিবর্তন করা যায় না (immutable)

👉 Example:
colors = ("red", "green", "blue")

👉 কেন এটা tuple?
- () ব্যবহার করা হয়েছে
- data fixed (change করা যাবে না)

👉 Real life:
Birth date / national ID info → fixed data

--------------------------------------------------

3️⃣ DICTIONARY (dict) — কেন dict?

✔ লেখা হয়: {}
✔ key-value pair থাকে

👉 Example:
student = {"name": "Mahmud", "age": 20}

👉 কেন এটা dict?
- {} ব্যবহার করা হয়েছে
- key + value আছে (name → Mahmud)

👉 Real life:
ID card / form / profile data

--------------------------------------------------

4️⃣ SET — কেন set?

✔ লেখা হয়: {}
✔ কিন্তু key-value নেই
✔ duplicate allowed না
✔ order নেই

👉 Example:
numbers = {1, 2, 3, 3}

👉 কেন এটা set?
- শুধু values আছে
- duplicate remove হয়ে যায়
- unordered

👉 Real life:
Unique roll number list

--------------------------------------------------

5️⃣ STRING (str) — কেন string?

✔ লেখা হয়: " " বা ' '
✔ text থাকে

👉 Example:
name = "Mahmud"

👉 কেন এটা string?
- quotes এর ভিতরে লেখা
- text data

👉 Real life:
Name, message, address

--------------------------------------------------

6️⃣ INT / FLOAT / COMPLEX — কেন numeric?

✔ int → 10 (পূর্ণ সংখ্যা)
✔ float → 10.5 (দশমিক)
✔ complex → 3+4j

👉 কেন numeric?
- শুধু সংখ্যা
- গণনা করা যায়

👉 Real life:
Age, price, calculation

--------------------------------------------------

7️⃣ BOOLEAN (bool) — কেন boolean?

✔ True / False

👉 Example:
is_student = True

👉 কেন boolean?
- শুধু দুইটা মান
- decision type data

👉 Real life:
Yes / No answer

--------------------------------------------------

8️⃣ RANGE — কেন range?

✔ range(5)

👉 কেন range?
- সংখ্যার সিরিজ তৈরি করে
- loop এ ব্যবহার হয়

👉 Real life:
Counting system (0 to 4)

--------------------------------------------------

9️⃣ BINARY TYPES — কেন binary?

✔ bytes → b"Hello"
#bytes is immutable যার মান বা ভ্যালু কখনোই চেঞ্জ করা যায় না
✔ bytearray → editable binary
#bytearray is mutable যার মান বা ভ্যালু caile চেঞ্জ করা যায়
#Bytearray & bytes range হলো 0 to 255
✔ memoryview → fast memory access

👉 কেন binary?
- computer-level raw data
- file/data processing

👉 Real life:
File storage, image/video data

--------------------------------------------------

🔟 NONE — কেন None?

✔ None

👉 Example:
x = None

👉 কেন None?
- কিছুই নেই
- empty value

👉 Real life:
Empty form field

--------------------------------------------------

🎯 FINAL TRICK (সব মনে রাখার সহজ নিয়ম)

👉 [] → LIST (change করা যায়)
👉 () → TUPLE (change করা যায় না)
👉 {} + key:value → DICT
👉 {} only values → SET
👉 " " → STRING
👉 number → INT/FLOAT
👉 True/False → BOOLEAN
👉 range() → SEQUENCE
👉 b"" → BINARY
👉 None → EMPTY


🐍 Python String Formatting (Beginner Note)
# গুরুত্বপূর্ণ কথা
# f-string ব্যবহার করার সময়
# String-এর আগে f বসাতে হয়।
#string formating example
num1 = 20
num2 = 10

print(f"this is my super number", {num1 + num2})
#output:this is my super number 30
#স্ট্রিং এর ভিতর এভাবে আমরা যোগ বিয়োগ গুন ভাগ সবকিছু করতে পারে
#আমরা চাইলে স্টিং এর ভিতরে রেখেও আউটপুট করতে পারি ফর এক্সাম্পল
username = "mahamud"
roll = "20"
print(f"my name is {username} + & my class roll is {roll}")
#output:my name is mahamud & my class roll is 20

📌 String Formatting কী?

String Formatting = আগে থেকে লেখা Text-এর ভিতরে
পরে Variable-এর Value বসানো।

সহজভাবে:

Text
+
Variable
=
String Formatting

উদাহরণ:

নাম = Hasan

↓

"আমার নাম Hasan"

━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 কেন ব্যবহার করি?

✔ Dynamic Output বানাতে

✔ User-এর Data দেখাতে

✔ Message বানাতে

✔ Report দেখাতে

✔ Code ছোট ও সুন্দর রাখতে

━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 গুরুত্বপূর্ণ কথা

f-string ব্যবহার করার সময়
String-এর আগে f বসাতে হয়।

Syntax:

f"Text {variable}"

এখানে:

f = formatting চালু করে

{}

= Variable বসানোর জায়গা

━━━━━━━━━━━━━━━━━━━━━━━━━━

🐍 Example 1 (২০২৬ Style)

name="Hasan"

print(f"Hello {name}, welcome to 2026")

Output:

Hello Hasan, welcome to 2026

━━━━━━━━━━━━━━━━━━━━━━━━━━

🐍 Example 2 (AI Learning)

skill="Python"

print(f"আমি ২০২৬ সালে {skill} শিখছি")

Output:

আমি ২০২৬ সালে Python শিখছি

━━━━━━━━━━━━━━━━━━━━━━━━━━

🐍 Example 3 (Shopping)

product="Laptop"
price=70000

print(f"{product} এর দাম {price} টাকা")

Output:

Laptop এর দাম 70000 টাকা

━━━━━━━━━━━━━━━━━━━━━━━━━━

🐍 Example 4 (IELTS)

score=7

print(f"আমার IELTS score {score}")

Output:

আমার IELTS score 7

━━━━━━━━━━━━━━━━━━━━━━━━━━

🐍 Example 5 (Calculation)

a=10
b=20

print(f"যোগফল {a+b}")

Output:

যোগফল 30

━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 এক লাইনে মনে রাখো

f"Text {variable}"

=

Text-এর ভিতরে Value বসানো

END