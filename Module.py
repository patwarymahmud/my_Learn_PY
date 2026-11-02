

def hablu():
    print("hablu function is called")

def mahamud():
    print("mahamud function is called")

def rahim():
    print("rahim function is called")

def azad():
    print("azad function is called")

#another example
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# #another example
# def add(a, b):
#     return a + b


# # ==========================================
# # পাইথন সম্পূর্ণ রিভিশন (Module + Function + Return + Print)
# # এক পেজ নোট (Copy-Paste Ready)
# # ==========================================

# # 🧠 1. Module কী?
# # Module = একটা Python ফাইল (.py)
# # যেখানে functions, variables, class থাকে
# # এবং সেটা অন্য ফাইলে ব্যবহার করা যায়

# # 📦 Own Module তৈরি: mymodule.py

# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def greet(name):
#     print("Hello", name)


# # 🚀 অন্য ফাইলে ব্যবহার (main.py)

# import mymodule

# print(mymodule.add(5, 3))      # 8
# print(mymodule.sub(10, 4))     # 6
# mymodule.greet("Mahmud")       # Hello Mahmud


# # 📌 mymodule.greet("Mahmud") মানে:
# # → mymodule ফাইলের ভিতরের greet function চালানো
# # → "Mahmud" হলো input (argument)
# # → তাই output: Hello Mahmud


# # -----------------------------
# # 🧠 2. Parameter vs Argument
# # -----------------------------

# # Parameter = function এর ভিতরের খালি জায়গা

# def add(a, b):   # a, b = parameter
#     return a + b

# # Argument = function call করার সময় দেওয়া value

# add(5, 3)   # 5, 3 = argument

# # 👉 চাইলে যেকোনো value দেওয়া যায়:
# # add(9, 10)
# # add(11, 20)


# # -----------------------------
# # 🧠 3. Return কী?
# # -----------------------------

# # return = function এর result বাইরে পাঠায়

# def square(x):
#     return x * x

# result = square(4)   # 16
# print(result + 10)   # 26


# # 📌 Flow:
# # 4 * 4 = 16
# # তারপর 16 + 10 = 26


# # -----------------------------
# # 🖨️ 4. print vs return
# # -----------------------------

# # print() = শুধু দেখায় (value দেয় না)
# # return = value ফিরিয়ে দেয় (reuse করা যায়)

# def demo1(x):
#     print(x + 10)

# def demo2(x):
#     return x + 10

# result = demo2(5)
# print(result)   # 15


# # ❌ print হলে সমস্যা:
# # result = None হয়ে যায়

# def bad(x):
#     print(x * x)

# # result = bad(4)
# # print(result + 10)  # error


# # ✅ return হলে power:
# def good(x):
#     return x * x

# result = good(4)
# print(result + 10)   # 26


# # -----------------------------
# # 🍔 Real Life Example
# # -----------------------------
# # Module = Recipe book
# # Function = Machine
# # Parameter = Empty box
# # Argument = Input value
# # Return = Output দিয়ে দেয়
# # Print = শুধু দেখায়


# # -----------------------------
# # 🎯 Final Memory Trick
# # -----------------------------
# # Module = reusable file
# # Function = কাজ করার মেশিন
# # Parameter = খালি জায়গা
# # Argument = দেওয়া ইনপুট
# # Return = ফলাফল ফিরিয়ে দেয়
# # Print = শুধু দেখায়


# # 🐍 Python Module → Package → PIP → pip install → Virtual Environment (Beginner Roadmap)

# # ১. Module (মডিউল)

# # Module = একটা Python ফাইল (.py) যেখানে কোড লেখা থাকে এবং অন্য ফাইলে ব্যবহার করা যায়।

# # উদাহরণ:

# # math_tools.py

# # def add(a, b):
# #     return a + b

# # main.py

# # import math_tools

# # print(math_tools.add(5, 3))

# # আউটপুট:
# # 8

# # কেন ব্যবহার করি?
# # → কোড গুছিয়ে রাখতে
# # → একই কোড বারবার ব্যবহার করতে
# # → বড় প্রজেক্ট ছোট ভাগে ভাগ করতে


# # ────────────────────

# # ২. Package (প্যাকেজ)

# # Package = অনেকগুলো Module একসাথে রাখা ফোল্ডার।

# # উদাহরণ:

# # project/
# # │
# # ├── tools/
# # │   ├── __init__.py
# # │   └── math.py
# # │
# # └── main.py

# # main.py থেকে:

# # from tools.math import add

# # কেন ব্যবহার করি?
# # → বড় প্রজেক্ট ম্যানেজ করতে
# # → ফাইল আলাদা রাখতে
# # → কোড পরিষ্কার রাখতে


# # ────────────────────

# # ৩. PIP

# # PIP = Python Package Installer

# # মানে ইন্টারনেট থেকে Python লাইব্রেরি ইনস্টল করার টুল।

# # চেক করো:

# # pip --version

# # উদাহরণ:
# # pip install requests

# # তারপর:

# # import requests

# # কেন ব্যবহার করি?
# # → অন্য মানুষের বানানো লাইব্রেরি ব্যবহার করতে


# # ────────────────────

# # ৪. pip install

# # নতুন লাইব্রেরি ইনস্টল:

# # pip install library_name

# # উদাহরণ:

# # pip install numpy

# # আপডেট:

# # pip install --upgrade numpy

# # সব দেখা:

# # pip list

# # ডিলিট:

# # pip uninstall numpy


# # ────────────────────

# # ৫. Virtual Environment (venv)

# # Virtual Environment = প্রতিটা প্রজেক্টের আলাদা Python পরিবেশ।

# # তৈরি:

# # python -m venv myenv

# # চালু (Windows):

# # myenv\Scripts\activate

# # বন্ধ:

# # deactivate

# # কেন ব্যবহার করি?
# # → এক প্রজেক্টের লাইব্রেরি আরেক প্রজেক্টে সমস্যা না করতে


# # ────────────────────

# # 📌 শেখার অর্ডার

# # Step 1 → Module
# # Step 2 → Package
# # Step 3 → PIP
# # Step 4 → pip install
# # Step 5 → Virtual Environment

# # এই ৫টা শিখে গেলে তুমি ৭০–৮০% রিয়েল Python প্রজেক্ট শুরু করার জন্য প্রস্তুত।

# # এরপর শিখবে:

# # NumPy
# # Pandas
# # API
# # Flask / Django
# # AI Automation
# # LangChain