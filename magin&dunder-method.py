🐍 Python Magic Method (Dunder Method) — Complete Beginner Friendly Note

━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Magic Method / Dunder Method কী?

Python-এ Magic Method (বা Dunder Method = Double Underscore Method)
হলো বিশেষ ধরনের Method যেগুলোর দুই পাশে ডাবল আন্ডারস্কোর (__) থাকে।

উদাহরণ:

__init__()
__str__()
__add__()

এগুলোকে Python নিজে নিজে বিশেষ সময়ে কল করে।

তুমি সরাসরি কল করতে পারো, কিন্তু সাধারণত Python অটোমেটিক কল করে।

উদাহরণ:

print(obj)

ভিতরে আসলে:

obj.__str__()

চলে।

━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Magic Method কেন ব্যবহার করি?

কারণ নিজের Class কে Python-এর Built-in Object-এর মতো আচরণ করানোর জন্য।
✔ +, -, *, ==, len(), [] এগুলো customize করতে
✔ OOP কে powerful করতে

যেমন:

+
-
*
==
print()
len()
[]
()

এসব নিজের Class-এ কাজ করাতে।

━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 CORE IDEA

Operator / Function ব্যবহার করলে
↓
Python ভিতরে Magic Method call করে
↓
তোমার class result return করে

━━━━━━━━━━━━━━━━━━━━━━━━━━


1) __init__() → Constructor
📌 কখন ব্যবহার হয়?
- Default Data সেট করতে
- Initial Value দিতে
- Setup করতে
📌 কাজ:
Object তৈরি হওয়ার সাথে সাথে run হয়

📌 বাস্তব উদাহরণ:
নতুন ব্যাংক অ্যাকাউন্ট খুললে নাম + ব্যালেন্স সেট হয়

Code:
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Hasan")
print(s.name)

Output:
Hasan

Internal:
Student("Hasan") → __init__()

━━━━━━━━━━━━━━━━━━━━━━━━━━

২) __str__() → সুন্দরভাবে Print

📌 

2) __str__() → print output
কাজ:
print(obj) দিলে কী দেখাবে।
Code:
class Car:
    def __str__(self):
        return "BMW"

c = Car()
print(c)

Output:
BMW

Internal:
print(c) → c.__str__()

━━━━━━━━━━━━━━━━━━━━━━━━━━
3) __add__() → +

📌 কাজ:
দুই অবজেক্ট কিভাবে যোগ হবে।
বাস্তব:
দুইজনের টাকা যোগ।

Code:
class Money:
    def __init__(self, taka):
        self.taka = taka

    def __add__(self, other):
        return self.taka + other.taka

a = Money(100)
b = Money(200)

print(a + b)

Output:
300

Internal:
a + b → a.__add__(b)
━━━━━━━━━━━━━━━━━━━━━━━━━━
4) __sub__() → -
কাজ:
বিয়োগ।
Code:
class Money:
    def __init__(self, val):
        self.val = val

    def __sub__(self, other):
        return self.val - other.val

a = Money(500)
b = Money(200)

print(a - b)

Output:
300

━━━━━━━━━━━━━━━━━━━━━━━━━━
5) __mul__() → *

Code:
class Product:
    def __init__(self, price):
        self.price = price

    def __mul__(self, qty):
        return self.price * qty

p = Product(100)

print(p * 5)

Output:
500

━━━━━━━━━━━━━━━━━━━━━━━━━━
6) __eq__() → ==
কাজ:
দুই অবজেক্ট সমান কিনা।
Code:
class User:
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        return self.id == other.id

a = User(1)
b = User(1)

print(a == b)

Output:
True

━━━━━━━━━━━━━━━━━━━━━━━━━━
7) __gt__() → >
কাজ:
বড় কিনা।
Code:
class Score:
    def __init__(self, num):
        self.num = num

    def __gt__(self, other):
        return self.num > other.num

a = Score(80)
b = Score(50)

print(a > b)

Output:
True

━━━━━━━━━━━━━━━━━━━━━━
8) __lt__() → <

Code:
class Score:
    def __init__(self, num):
        self.num = num

    def __lt__(self, other):
        return self.num < other.num

a = Score(30)
b = Score(50)

print(a < b)

Output:
True

━━━━━━━━━━━━━━━━━━━━━━━━━━
9) __len__() → len()
কাজ:
কতগুলো আছে।
Code:
class Bag:
    def __len__(self):
        return 5

b = Bag()
print(len(b))

Output:
5

Internal:
len(b) → b.__len__()
━━━━━━━━━━━━━━━━━━━━━━━━━━
10) __call__() → object as function
কাজ:
অবজেক্টকে Function বানানো।
Code:
class Robot:
    def __call__(self):
        print("Running")

r = Robot()
r()

Output:
Running

Internal:
r() → r.__call__()

━━━━━━━━━━━━━━━━━━━━━━━━━
11) __getitem__() → []
কাজ:
Index দিয়ে ডাটা বের করা।
Code:
class Box:
    def __getitem__(self, index):
        return index

b = Box()
print(b[7])

Output:
7
Internal:
b[7] → b.__getitem__(7)

━━━━━━━━━━━━━━━━━━━━━━━━━━
12) __setitem__() → []=
কাজ:
Index-এ Value বসানো।
Code:
class Box:
    def __setitem__(self, key, value):
        print(key, value)

b = Box()
b[0] = 100

Output:
0 100

Internal:
b[0] = 100 → b.__setitem__(0, 100)


━━━━━━━━━━━━━━━━━━━━━━━━━━

13) __del__() → delete object
কাজ:
অবজেক্ট ডিলিট হলে।
Code:
class Test:
    def __del__(self):
        print("Deleted")

t = Test()
del t

Output:
Deleted


━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 Operator Overloading কী?

Operator-এর কাজ নিজের মতো করে বানানো।

Example:

a+b

↓

a.__add__(b)

তুমি ঠিক করবে যোগ মানে কী।

━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 Full Mapping

Object Create
↓

__init__()

print()
↓

__str__()

+
↓

__add__()

-
↓

__sub__()

*
↓

__mul__()

==
↓

__eq__()

>
↓

__gt__()

<
↓

__lt__()

len()
↓

__len__()

()
↓

__call__()

[]
↓

__getitem__()

[]=
↓

__setitem__()

delete
↓

__del__()

━━━━━━━━━━━━━━━━━━━━━━━━━━
🔥 FINAL SUMMARY

__init__     → object create
__str__      → print()
__add__      → +
__sub__      → -
__mul__      → *
__eq__       → ==
__gt__       → >
__lt__       → <
__len__      → len()
__call__     → ()
__getitem__  → []
__setitem__  → []=
__del__      → delete

📌 কখন বেশি ব্যবহার হয়?

- OOP
- Django
- Flask
- Automation
- AI Framework
- Game Development
- Data Structure
- Custom Object Design

━━━━━━━━━━━━━━━━━━━━━━━━━━

সবচেয়ে গুরুত্বপূর্ণ লাইন:

Magic Method মুখস্থ করার জিনিস না।

এগুলো শেখার উদ্দেশ্য হলো:

"নিজের Class-কে Python Built-in Object-এর মতো আচরণ করানো।"

যখন এটা বুঝবে,
তখন OOP-এর বড় অংশ তোমার ক্লিয়ার হয়ে যাবে।

End.

🐍 Python Magic Method (Internal Mechanism) — Simple One Page Note

━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 প্রথমে সবচেয়ে গুরুত্বপূর্ণ কথা

Magic Method = Python-এর hidden method

তুমি কিছু লিখো
↓
Python ভিতরে Magic Method call করে
↓
Result দেয়

উদাহরণ:

len(obj)

আসলে:

obj.__len__()

━━━━━━━━━━━━━━━━━━━━━━━━━━

1) __len__() → len()

📌 কাজ:
কোন object-এর length কত হবে সেটা ঠিক করা।

Example:

class Bag:

    def __len__(self):
        return 5


b = Bag()

print(len(b))

Output:

5

━━━━━━━━━━

🧠 ভিতরে কী হলো?

তুমি লিখেছো:

len(b)

Python ভিতরে করেছে:

b.__len__()

তারপর:

return 5

তাই output:

5

━━━━━━━━━━

❗ গুরুত্বপূর্ণ

return 5 fixed না।

তুমি চাইলে:

return 10

করতে পারো।

তাহলে output:

10

আসবে।

━━━━━━━━━━━━━━━━━━━━━━━━━━

2) __call__() → object কে function বানানো

📌 কাজ:
Object কে () দিয়ে call করা।

Example:

class Robot:

    def __call__(self):

        print("Running")


r = Robot()

r()

Output:

Running

━━━━━━━━━━

🧠 ভিতরে কী হলো?

তুমি লিখেছো:

r()

Python করেছে:

r.__call__()

তারপর:

print("Running")

তাই output:

Running

━━━━━━━━━━

সহজভাবে:

r()

=

r.__call__()

━━━━━━━━━━━━━━━━━━━━━━━━━━

3) __getitem__() → []

📌 কাজ:
Index দিয়ে data বের করা।

Example:

class Box:

    def __init__(self):

        self.data=[10,20,30]

    def __getitem__(self,index):

        return self.data[index]


b=Box()

print(b[1])

Output:

20

━━━━━━━━━━

🧠 ভিতরে কী হলো?

তুমি লিখেছো:

b[1]

Python করেছে:

b.__getitem__(1)

তারপর:

return self.data[1]

মানে:

return 20

তাই output:

20

━━━━━━━━━━

🧠 List এর ভিতরে:

Index:

0 → 10
1 → 20
2 → 30

তাই:

b[1]

=

20

━━━━━━━━━━━━━━━━━━━━━━━━━━

4) __setitem__() → []=

📌 কাজ:
Index এ value বসানো।

Example:

class Box:

    def __setitem__(self,key,value):

        print(key,value)


b=Box()

b[0]=100

Output:

0 100

━━━━━━━━━━

🧠 ভিতরে কী হলো?

তুমি লিখেছো:

b[0]=100

Python করেছে:

b.__setitem__(0,100)

তারপর:

print(0,100)

তাই output:

0 100

━━━━━━━━━━

❗ এটা fixed না।

তুমি চাইলে:

b[5]=500

Python করবে:

b.__setitem__(5,500)

━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 বাস্তবে __setitem__ কী করে?

Example:

class Box:

    def __init__(self):

        self.data=[0,0,0]

    def __setitem__(self,key,value):

        self.data[key]=value


b=Box()

b[0]=100

print(b.data)

Output:

[100,0,0]

━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 FINAL SUPER SIMPLE SUMMARY

তুমি যা লেখো
↓

Python ভিতরে যা করে

len(b)
↓

b.__len__()

━━━━━━━━━━

r()
↓

r.__call__()

━━━━━━━━━━

b[1]
↓

b.__getitem__(1)

━━━━━━━━━━

b[0]=100
↓

b.__setitem__(0,100)

━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 এক লাইনে মনে রাখো

Magic Method = Python-এর hidden bridge
যা operator আর syntax কে
তোমার function-এর সাথে connect করে।

END

🐍 Python __getitem__() — Understanding Correction Note

━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 আমার ধারণা (যেটা আমি ভেবেছিলাম)

আমি ভেবেছিলাম:

10 → index 0
20 → index 1
30 → index 2

তাই:

b[1]

=

20

━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 আমার understanding কোথায় ঠিক ছিল?

✔ আমি ঠিক ধরেছিলাম যে এখানে index ব্যবহার হচ্ছে।

কারণ:

List এর ভিতরে সত্যিই index থাকে।

উদাহরণ:

data=[10,20,30]

Index:

0 → 10
1 → 20
2 → 30

তাই:

data[1]

=

20

এতটুকু চিন্তা ঠিক ছিল।

━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 কোথায় ভুল ছিল?

❌ আমি ভেবেছিলাম:

10 → 0
20 → 1
30 → 2

এভাবে Python নিজে value কে index বানায়।

এটা ভুল।

Python value কে index বানায় না।

━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 আসলে কী হয়?

List আগে থেকেই index ধরে রাখে।

Example:

data=[10,20,30]

Python ভিতরে রাখে:

Index:

0 → 10
1 → 20
2 → 30

তাই:

data[1]

মানে:

index 1 এর value বের করো

Result:

20

━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Example

class Box:

    def __init__(self):

        self.data=[10,20,30]

    def __getitem__(self,index):

        return self.data[index]


b=Box()

print(b[1])

Output:

20

━━━━━━━━━━

🧠 ভিতরে কী হলো?

তুমি লিখেছো:

b[1]

Python করেছে:

b.__getitem__(1)

তারপর:

return self.data[1]

=

20

━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 Step by Step

b[1]

↓

b.__getitem__(1)

↓

self.data[1]

↓

20

━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 সবচেয়ে গুরুত্বপূর্ণ কথা

Index তৈরি করে Python না।

Index আগে থেকেই list-এর ভিতরে থাকে।

__getitem__ শুধু সেই index ব্যবহার করে value তুলে আনে।

━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 এক লাইনে মনে রাখো

b[1]=20 এসেছে কারণ
index 1 এ আগে থেকেই 20 ছিল।

না যে Python 20 কে index বানিয়েছে।

END

🐍 Python Custom List + Magic Method + Next Level (One Note)

━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 লক্ষ্য (Goal)

আমরা এমন একটা Custom List বানাবো যেখানে:

b[0]=10
b[1]=20

print(b[1])

Output:

20

মানে:
তুমি নিজের মতো করে List Control করবে।

━━━━━━━━━━━━━━━━━━━━━━━━━━

🐍 Custom List (OOP Version)

class MyList:

    def __init__(self):

        self.data=[]


    def __setitem__(self,index,value):

        if index>=len(self.data):

            self.data.extend(
                [None]*(index-len(self.data)+1)
            )

        self.data[index]=value


    def __getitem__(self,index):

        return self.data[index]


    def __len__(self):

        return len(self.data)


    def __str__(self):

        return str(self.data)

━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 ব্যবহার

b=MyList()

b[0]=10

b[1]=20

b[2]=30

print(b)

print(b[1])

print(len(b))

━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Output

[10,20,30]

20

3

━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 কী হচ্ছে ভিতরে?

তুমি লিখেছো:

b[1]

Python করেছে:

b.__getitem__(1)

━━━━━━━━━━

তুমি লিখেছো:

b[0]=10

Python করেছে:

b.__setitem__(0,10)

━━━━━━━━━━

তুমি লিখেছো:

print(b)

Python করেছে:

b.__str__()

━━━━━━━━━━

তুমি লিখেছো:

len(b)

Python করেছে:

b.__len__()

━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 কেন এটা Powerful?

কারণ এখন:

✔ Index Control করতে পারো

✔ Rule বসাতে পারো

✔ Data Protect করতে পারো

✔ Custom Logic বসাতে পারো

✔ নিজের List Design করতে পারো

━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 Real Life Example

Inventory System

0 → Product A

1 → Product B

2 → Product C

তুমি চাইলে:

✔ Out of stock block

✔ Custom validation

✔ History tracking

সব করতে পারো।

━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 Final Concept

Python List

=

Built-in Structure

━━━━━━━━━━

Custom List

=

নিজের Rule দিয়ে List

━━━━━━━━━━

Magic Method

=

Python Syntax
↓

তোমার Logic

━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 এক লাইনে Mastery

__getitem__ + __setitem__

=

তুমি List-এর Boss

━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 NEXT LEVEL

যখন এগুলো বুঝে যাবে তখন:

👉 Circular Queue
(Advanced Interview Favorite)

👉 Stack Using Linked List

👉 Queue Using Linked List

👉 Real Project:
Browser History System

━━━━━━━━━━━━━━━━━━━━━━━━━━

🧠 Final Thought

এখনই Next Level এ যাওয়ার দরকার নাই।

কারণ তুমি Beginner।

আগে:

✔ __getitem__()

✔ __setitem__()

✔ __len__()

✔ __str__()

এগুলো পরিষ্কার করো।

তারপর Stack / Queue।

তারপর Linked List।

তারপর Real Project।

END