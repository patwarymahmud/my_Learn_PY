# python array with list difference
#আমাদের পাইথনের ডেভেলপাররা সবসময় রেকমেন্ড করে পাইথনের যে লিস্টটা আছে, এই লিস্টটাকে ইউজ করতে এবং অ্যারেটাকে অ্যাভয়েড করতে বেসিক্যালি পাইথনের যে রও ল্যাঙ্গুয়েজ আছে, এই অ্যারেটাকে তারা রেকমেন্ড করে না কারণ তাদের নামপাই নামে একটা লাইব্রেরি আছে যেটার ভেতরে নামপাই অ্যারে নামে একটা আইটেম আছে যেই আইটেমটা ইউজ করার মাধ্যমে আমরাডাটা সায়েন্স এবং এ সকল বিষয়ে যে ক্যালকুলেটিংয়ের কাজগুলো আছে সে ক্যালক কাজগুলো করতে পারি। তাই এটার জন্য আমরা যখন ro পাইথন ল্যাঙ্গুয়েজ নিয়ে কাজ করব তখন আমরা অ্যারে এর পরিবর্তে লিস্ট ইউজ করব। আর যখন আমরা ডাটা সায়েন্স, মেশিন লার্নিংম্যাথমেটিক্যাল বিষয়গুলো নিয়ে কাজ করব, তখন আমরা নামপাই লাইব্রেরির নামপাই নামে যে অ্যারেটা আছে ঐটা ইউজ করব।
#একটা এক্সাম্পল দেওয়ার পর নীচে পাইথন অ্যারে এবং লিস্টের মধ্যে পার্থক্য নিয়ে বিস্তারিত দেওয়া আছে।

#array example
Myarray = ["apple", "banana", "cherry"]
Myarray[0] = "orange"
print(Myarray)
# Output:
# ['orange', 'banana', 'cherry']

# Array কি?

# Array হচ্ছে এমন একটি system যেখানে
# একই ধরনের একাধিক data
# Array একটি single variable jar ভিতরে multipul data store kore রাখা যায়।
# Array সাধারণত number এবং same type data
# store করার জন্য বেশি ব্যবহার হয়।

# Python List vs Python Array

# List = Mixed Data
# Array = Same Type Data

# =========================
# Python List
# =========================
# Built-in
# সব ধরনের data রাখা যায়
# বেশি flexible
data = ["apple", 10, True]
print(data)
# Output: ['apple', 10, True]

# =========================
# Python Array
# =========================
# Import করতে হয়
# একই type এর data রাখতে হয়
# Fast এবং কম memory ব্যবহার করে
import array
numbers = array.array('i', [1, 2, 3, 4])
print(numbers)

# =========================
# ৫টি মৌলিক পার্থক্য
# =========================
# 1. List এ mixed data রাখা যায়
#    Array এ same type data রাখতে হয়
# 2. List built-in
#    Array import করতে হয়
# 3. List বেশি flexible
#    Array বেশি strict
# 4. List একটু বেশি memory ব্যবহার করে
#    Array কম memory ব্যবহার করে
# 5. List সাধারণ কাজে বেশি ব্যবহার হয়
#    Array numerical/number এর কাজে বেশি ব্যবহার হয়

# Python Array এর কিছু গুরুত্বপূর্ণ using Method
# append()
# extend()
# insert()
# remove()
# pop()
# index()
# count()
# reverse()
# buffer_info()
# tostring()
# fromlist()
# tolist()
