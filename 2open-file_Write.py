#python file write example
# wr = open("Mahamud.text", "a")
# wr.write("This is a python file write example")
# wr.write("append mathode use korle file er data overwrite hoy na, notun data file er sesh e add hoy \n")
# প্রথমে:

# wr = open("Mahamud.text", "w")

# এখানে open() Function ব্যবহার করে "Mahamud.text" নামে একটি File খুলা হয়।

# যদি File আগে থেকে না থাকে, তাহলে Python নতুন করে "Mahamud.text" নামে একটি File তৈরি করে।

# এরপর "w" (Write Mode) ব্যবহার করার কারণে File-টি লেখার জন্য প্রস্তুত হয়।

# তারপর:

# wr.write("This is a python file write example")

# এখানে write() Method File-এর ভিতরে
# "This is a python file write example"
# লেখাটি লিখে দেয়।

# ফলাফল হিসেবে "Mahamud.text" File-এর ভিতরে এই লেখাটি সংরক্ষণ হয়:

# This is a python file write example

# অর্থাৎ open() দিয়ে File খুলা বা তৈরি করা হয়, আর write() দিয়ে File-এর ভিতরে Data লেখা হয়।

# আরেকটা ছোট্ট বিষয়: সাধারণত .text এর বদলে .txt বেশি ব্যবহার করা হয়। তাই "Mahamud.txt" নামেও File তৈরি করা যেতে পারে।

# Python Append Mode ("a") ব্যবহার করা হয় File-এর পুরাতন Data না মুছে শেষে নতুন Data যোগ করার জন্য।

# উদাহরণ:

# file = open("data.txt", "a")
# file.write("Hello Python")
# file.close()

# ফলাফল:
# যদি data.txt আগে থেকেই থাকে, তাহলে "Hello Python" লেখাটি ফাইলের শেষে যোগ হবে।

# গুরুত্বপূর্ণ:

# w = পুরাতন Data মুছে নতুন লিখে
# a = পুরাতন Data রেখে শেষে নতুন যোগ করে

# "\n" = New Line (Enter)

# উদাহরণ:

# file.write("Hasan\n")
# file.write("Rahim\n")

# ফাইলের ভিতরে হবে:

# Hasan
# Rahim

# একই লাইন কয়েকবার লিখতে:

# for i in range(3):
#     file.write("Hello Python\n")

# ফাইলের ভিতরে হবে:

# Hello Python
# Hello Python
# Hello Python

# কোথায় ব্যবহার হয়?

# ✔ Student List Save করতে
# ✔ Chat History রাখতে
# ✔ Log File তৈরি করতে
# ✔ Notes যোগ করতে
# ✔ User Activity Save করতে

# সহজভাবে:

# open() = File খুলে
# write() = File-এ লিখে
# w = পুরাতন Data মুছে লিখে
# a = পুরাতন Data রেখে শেষে যোগ করে
# \n = নতুন লাইনে নেয়

#python file delete example
# import os
# os.remove("Mahamud.text")
# import os

print(os.path.exists("Mahamud.text"))

os.remove("Mahamud.text")

print("Deleted Successfully")

# যখন File Delete শিখছো, তখন এভাবে লিখো:

# import os

# if os.path.exists("Mahamud.text"):
#     os.remove("Mahamud.text")
#     print("File Deleted Successfully")
# else:
#     print("File Not Found")

# এতে সব সময় বুঝতে পারবে কী হয়েছে।

# os.path.exists() = File আছে কিনা চেক করে
# os.remove() = File Delete করে

# os.remove("file.txt") সফলভাবে File Delete করলে কোনো Output দেয় না। তাই Beginner-দের জন্য print() বা os.path.exists() ব্যবহার করে চেক করা ভালো।
# os.remove() = File Delete করে
# আমরা এই ডিলিট মেথড ইউজ করে যেকোনো ফাইলকে আমরা চাইলে ডিলিট করতে পারি。 


# #os.rmdir() ব্যবহার করা হয় খালি Folder Delete করার জন্য।

# Syntax:

# import os

# os.rmdir("FolderName")

# গুরুত্বপূর্ণ:

# ✔ Folder খালি হতে হবে
# ✔ Folder-এর ভিতরে File থাকলে Error আসবে
# ✔ os.remove() = File Delete
# ✔ os.rmdir() = Empty Folder Delete

# Safe Way:

# if os.path.exists("FolderName"):
#     os.rmdir("FolderName")

# Real Life:

# খালি আলমারি ফেলে দেওয়া = os.rmdir()
# খাতার পৃষ্ঠা ফেলে দেওয়া = os.remove()

# """
# Python os.rmdir() — Full Beginner One Page Note

# os.rmdir() ব্যবহার করা হয় খালি folder (empty directory) delete করার জন্য। এটা শুধুমাত্র সেই folder delete করতে পারে যার ভিতরে কোনো file বা subfolder নেই।

# Syntax:
# import os
# os.rmdir("FolderName")

# Example:
# import os
# os.rmdir("TestFolder")
# print("Folder Deleted")

# Important Rule:
# os.rmdir() শুধু খালি folder delete করতে পারে। যদি folder-এর ভিতরে file বা subfolder থাকে তাহলে error দিবে।

# Error Case:
# যদি folder এ file থাকে:
# TestFolder/
#     data.txt

# তাহলে:
# os.rmdir("TestFolder")

# Output:
# OSError: Directory not empty

# Safe Way:
# import os

# folder = "TestFolder"

# if os.path.exists(folder):
#     os.rmdir(folder)
#     print("Folder Deleted")
# else:
#     print("Folder Not Found")

# Comparison:
# os.remove() -> File delete করে
# os.rmdir() -> Empty folder delete করে
# shutil.rmtree() -> Full folder delete করে (সব কিছু সহ)

# Memory Trick:
# File = os.remove()
# Empty Folder = os.rmdir()
# Full Folder = shutil.rmtree()
# """


#"""
# Python shutil.rmtree() — Full Folder Delete One Page Note

# shutil.rmtree() ব্যবহার করা হয় পুরো folder (directory) delete করার জন্য। এর মাধ্যমে folder-এর ভিতরের সব file, subfolder একসাথে delete হয়ে যায়।

# Syntax:
# import shutil
# shutil.rmtree("FolderName")

# Example:
# import shutil
# shutil.rmtree("TestFolder")
# print("Folder Deleted Successfully")

# Important Warning:
# এটা খুব powerful function। ভুল folder দিলে সব data delete হয়ে যেতে পারে এবং এটা undo করা যায় না।

# Safe Way:
# import os
# import shutil

# folder = "TestFolder"

# if os.path.exists(folder):
#     shutil.rmtree(folder)
#     print("Folder Deleted")
# else:
#     print("Folder Not Found")

# Comparison:
# os.remove() -> File delete করে
# os.rmdir() -> Empty folder delete করে
# shutil.rmtree() -> Full folder delete করে (file + subfolder সহ)

# Memory Trick:
# File = os.remove()
# Empty Folder = os.rmdir()
# Full Folder = shutil.rmtree()
# """