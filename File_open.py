# # ==========================================================
# # Python File Handling (Open File) - Beginner Friendly Notes
# # ==========================================================

# # ==========================================================
# # File Handling কী?
# # ==========================================================

# # File Handling হলো Python দিয়ে কোনো File
# # খুলা (Open), পড়া (Read), লেখা (Write),
# # নতুন তথ্য যোগ করা (Append) এবং বন্ধ করা (Close)।

# # ==========================================================
# # Real Life Example
# # ==========================================================

# # ধরো তোমার একটা খাতা আছে।

# # খাতা খুলা     = open()
# # খাতা পড়া     = read()
# # খাতায় লেখা   = write()
# # নতুন লেখা যোগ = append()
# # খাতা বন্ধ     = close()

# #open file read example read এর শর্ট ফর্ম হল 'r '
# readtext = open("text.text", "r")
# print(readtext.read())

#another way
#আর ভালো প্র্যাকটিস:
# with open("text.text", "r") as readtext:
#     print(readtext.read())

#open file write example write  এর শর্ট ফর্ম হল 'w '
#wr = open("hablu.html", "w")
# wr.write("tumi amak subscribe koro")
#wr.write("<h1>subscribe hablu programmer </h1>")
wr = open("hablu.html", "a")#আমরা রাইট করার সময়ও এখানে a or r+ ইউজ করব তাহলে  রিড রাইট প্লাস দোনোটাই করতে পারো
wr.write("hi \n")
#write read example
wr = open("hablu.html", "r")
#wr.write("hi \n")
print(wr.read())
#পাইথন রাইট এর ভিতরে append মেথড এর 'a' ইউজ করে অন্য লেখা এড করা যায় এবং প্রথমে যেই লেখাটা এড করা হয় সেই লেখাটা পরের লেখাটাr সাথে প্রিন্ট হয়ে তারপরের তারপর তারপর ডাটা টা দেখায় একটু ঝামেলা লাগতে পারে বাট upore এক্সাম্পল এবং এখানে \n  মানে হচ্ছে নিউ line এবং রাইট এর ভিতরে প্রত্যেকবার যদি ভিন্ন ভিন্ন লেখা লেখি তাহলে আগেরটাও থাকবে পরেরটাও থাকবে আউটপুটে, এখানে append  মেথড ইউজ করার কারণে আউটপুটটা সেভ হয়ে থাকতেছে তবে ডব্লিউ মানে রাইট মেথড ইউজ করলে একটা আউটপুটে থাকবে সেভ হয়ে থাকবে না

#delete a file
    # import os 
    # os .remove("এখানে remove function এর ভেতরে যে ফাইলটি রাখবো সেটি ডিলিট হয়ে যাবে")
#delete a folder
import os 
os .rmdir("gablu")
# # Python File Handling ঠিক এইভাবেই কাজ করে।
# # ==========================================================
# # open() Function
# # ==========================================================

# # File Open করার জন্য ব্যবহার হয়।

# # Syntax:

# file = open("file.txt", "mode")

# # প্রথম অংশ:
# #
# # "file.txt"
# #
# # File এর নাম।

# # দ্বিতীয় অংশ:
# #
# # "mode"
# #
# # কী কাজ করবে সেটা বলে।

# # ==========================================================
# # File Modes
# # ==========================================================

# # r  = Read
# # w  = Write
# # a  = Append
# # x  = Create
# # t  = Text Mode
# # b  = Binary Mode

# # ==========================================================
# # r Mode (Read)
# # ==========================================================

# file = open("data.txt", "r")

# print(file.read())

# file.close()

# # ধরো data.txt এর ভিতরে আছে:
# #
# # Hello Python
# # Welcome to File Handling
# #
# # Output:
# #
# # Hello Python
# # Welcome to File Handling

# # ==========================================================
# # w Mode (Write)
# # ==========================================================

# file = open("data.txt", "w")

# file.write("Hello Python")

# file.close()

# # Output:
# #
# # (স্ক্রিনে কিছু দেখাবে না)
# #
# # data.txt এর ভিতরে হবে:
# #
# # Hello Python

# # ==========================================================
# # a Mode (Append)
# # ==========================================================

# file = open("data.txt", "a")

# file.write("\nNew Line")

# file.close()

# # ধরো আগে data.txt এ ছিল:
# #
# # Hello Python
# #
# # Output:
# #
# # Hello Python
# # New Line

# # ==========================================================
# # x Mode (Create)
# # ==========================================================

# file = open("newfile.txt", "x")

# file.close()

# # Output:
# #
# # (স্ক্রিনে কিছু দেখাবে না)
# #
# # নতুন file তৈরি হবে:
# #
# # newfile.txt

# # ==========================================================
# # read() Function
# # ==========================================================

# file = open("data.txt", "r")

# print(file.read())

# file.close()

# # ধরো data.txt এর ভিতরে আছে:
# #
# # Hello Python
# #
# # Output:
# #
# # Hello Python

# # ==========================================================
# # read(5)
# # ==========================================================

# file = open("data.txt", "r")

# print(file.read(5))

# file.close()

# # Example:
# #
# # data.txt:
# # Hello Python
# #
# # Output:
# #
# # Hello

# # ==========================================================
# # readline()
# # ==========================================================

# file = open("data.txt", "r")

# print(file.readline())

# file.close()

# # ধরো data.txt এর ভিতরে আছে:
# #
# # Hello Python
# # Welcome
# #
# # Output:
# #
# # Hello Python

# # ==========================================================
# # readlines()
# # ==========================================================

# file = open("data.txt", "r")

# print(file.readlines())

# file.close()

# # ধরো data.txt এর ভিতরে আছে:
# #
# # Line1
# # Line2
# #
# # Output:
# #
# # ['Line1\n', 'Line2\n']

# # ==========================================================
# # write()
# # ==========================================================

# file = open("data.txt", "w")

# file.write("Python")

# file.close()

# # Output:
# #
# # (স্ক্রিনে কিছু দেখাবে না)
# #
# # data.txt এর ভিতরে হবে:
# #
# # Python

# # ==========================================================
# # with Open (Best Practice)
# # ==========================================================

# with open("data.txt", "r") as file:

#     print(file.read())

# # ধরো data.txt এর ভিতরে আছে:
# #
# # Hello Python
# #
# # Output:
# #
# # Hello Python

# # ==========================================================
# # File Exists Error Example
# # ==========================================================

# try:

#     file = open("unknown.txt", "r")

# except FileNotFoundError:

#     print("File পাওয়া যায়নি")

# # Output:
# #
# # File পাওয়া যায়নি

# # ==========================================================
# # Real Life Student Example
# # ==========================================================

# # students.txt
# #
# # Hasan
# # Rahim
# # Karim

# with open("students.txt", "r") as file:

#     print(file.read())

# # Output:
# #
# # Hasan
# # Rahim
# # Karim

# # ==========================================================
# # Add New Student
# # ==========================================================

# with open("students.txt", "a") as file:

#     file.write("\nSabbir")

# # ধরো আগে students.txt এ ছিল:
# #
# # Hasan
# # Rahim
# # Karim
# #
# # Output:
# #
# # Hasan
# # Rahim
# # Karim
# # Sabbir

# # ==========================================================
# # Most Important Functions
# # ==========================================================

# # open()
# # read()
# # read(size)
# # readline()
# # readlines()
# # write()
# # close()

# # ==========================================================
# # Most Important Modes
# # ==========================================================

# # r = Read
# # w = Write
# # a = Append
# # x = Create

# # ==========================================================
# # Beginner Shortcut
# # ==========================================================

# # open()
# # = File খুলে

# # read()
# # = File পড়ে

# # write()
# # = File লিখে

# # append()
# # = File এর শেষে যোগ করে
# #
# # (আসলে a Mode ব্যবহার করা হয়)

# # close()
# # = File বন্ধ করে

# # with open()
# # = Auto Close করে

# # ==========================================================
# # One Line Definition
# # ==========================================================

# # Python File Handling হলো File তৈরি করা,
# # পড়া, লেখা, আপডেট করা এবং পরিচালনা করার পদ্ধতি।
# # ==========================================================

# # ==========================================================
# # Python File Handling (Clear + Real Example with File Content)
# # ==========================================================

# # ==========================================================
# # ধরো আমরা আগে থেকেই জানি:
# # ==========================================================
# # data.txt ফাইলের ভিতরে এই লেখা আছে:

# # Hello Python
# # Welcome to File Handling
# # ==========================================================

# # ==========================================================
# # 1. read() Example
# # ==========================================================

# file = open("data.txt", "r")

# print(file.read())

# file.close()

# # Output:
# # Hello Python
# # Welcome to File Handling

# # Explanation:
# # পুরো ফাইল একসাথে পড়ে ফেলে।

# # ==========================================================
# # 2. read(5) Example
# # ==========================================================
# # ধরো আমরা আগে থেকেই জানি:
# # ==========================================================
# # data.txt ফাইলের ভিতরে এই লেখা আছে:

# # Hello Python
# file = open("data.txt", "r")

# print(file.read(5))

# file.close()

# # Output:
# # Hello

# # Explanation:
# # প্রথম 5টা character পড়ে।

# # ==========================================================
# # 3. readline() Example
# # ==========================================================
# # ধরো আমরা আগে থেকেই জানি:
# # ==========================================================
# # data.txt ফাইলের ভিতরে এই লেখা আছে:

# # Hello Python
# # Welcome to File Handling
# file = open("data.txt", "r")

# print(file.readline())

# file.close()

# # Output:
# # Hello Python

# # Explanation:
# # শুধু প্রথম লাইন পড়ে।

# # ==========================================================
# # 4. readlines() Example
# # ==========================================================

# file = open("data.txt", "r")

# print(file.readlines())

# file.close()

# # Output:
# # ['Hello Python\n', 'Welcome to File Handling\n']

# # Explanation:
# # পুরো ফাইলকে list আকারে দেয়।
# # প্রতিটি line আলাদা item হয়।

# # ==========================================================
# # 5. append mode (a)
# # ==========================================================

# file = open("data.txt", "a")

# file.write("\nPython is fun")

# file.close()

# # ধরো আগে ফাইল ছিল:
# #
# # Hello Python
# # Welcome to File Handling
# #
# # এখন হবে:

# # Output (file update হবে):
# # Hello Python
# # Welcome to File Handling
# # Python is fun

# # ==========================================================
# # 6. write mode (w)
# # ==========================================================
# # ধরো আমরা আগে থেকেই জানি:
# # ==========================================================
# # data.txt ফাইলের ভিতরে এই লেখা আছে:

# # Welcome to File Handling
# file = open("data.txt", "w")

# file.write("Only Python")

# file.close()

# # Output:
# # ফাইল পুরো clear হয়ে যাবে এবং নতুন লেখা হবে

# # File এখন হবে:
# # Only Python

# # ==========================================================
# # Beginner Shortcut
# # ==========================================================

# # read()     → পুরো ফাইল
# # readline() → এক লাইন
# # read(5)    → নির্দিষ্ট character
# # readlines()→ list আকারে সব line
# # w          → পুরাতন মুছে নতুন লেখা
# # a          → পুরাতনের সাথে যোগ করা

# # ==========================================================
# # One Line Definition
# # ==========================================================

# # Python file handling মানে হলো file খুলে তার ভিতরের লেখা পড়া,
# # লেখা, পরিবর্তন করা এবং সংরক্ষণ করা।
# # ==========================================================