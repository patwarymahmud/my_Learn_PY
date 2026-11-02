#python set
# পাইথন সেট এর ভিতরে কোন একটা আইটেম যদি দুইবার থাকে তাহলে সেখান থেকে একটা আইটেম এর আউটপুট দেখাবে আরেকটা দেখাবে না.তবে এখানে দুইটা ওয়ান ভিন্ন method a আছে একটা intager একটা string তাই দুইটা এক না হওয়ার কারণে সে দুনোটা ওয়ানকে প্রিন্ট করেছে. আর আরেকটা বিষয় হচ্ছে পাইথন সেট এর ভিতরে সেকেন্ড ব্র্যাকেট দিয়ে লিস্ট টা লেখা হয়. এবং সেট আইটেম আনচেঞ্জেবল কিন্তু এখানে চাইলে আইটেম রিমুভ করা যাবে এবং অ্যাডও করা যাবে. এবং এটা কারো কথা শোনে না আউটপুট করার সময় ওলট-পালট ভাবে আউটপুট করে মানে আগেরটা পরে পরেরটা আগে এভাবে
Myset = {1, "1", False, "string", "string"}
print(Myset) # Output: {False, 1, 'string', '1'}
# Note: The order of elements in a set is not guaranteed, and it may vary each

#set, len() function দিয়ে সব আইটেমের মোট ইনডেক্স নাম্বার বের করা
setitem = {1,2,"3",1,3,6}
print(len(seitem))
#output:5

#Access set items
# পাইথন সেট এর ভিতরে আইটেম গুলোকে অ্যাক্সেস করা যায় না কারণ সেট এর ভিতরে আইটেম গুলো অর্ডারলেস এবং ইনডেক্সলেস হয়। তাই সেট এর ভিতরে আইটেম গুলোকে অ্যাক্সেস করা যায় না।
# Myset = {1, False, "string", "string"}
# print(Myset[0]) # Output: TypeError: 'set' object is not subscriptable
# Note: You can use a loop to access each item in a set, but you cannot access items by index.🧠 Python Set নোট:
# Set-এর এলিমেন্ট ইনডেক্স দিয়ে অ্যাকসেস করা যায় না এবং সরাসরি কোনো নির্দিষ্ট এলিমেন্ট পরিবর্তনও করা যায় না, কারণ Set unordered এবং unique value সংরক্ষণ করে।
# তবে Set-এর ভিতরের ডাটা নিয়ে কাজ করা যায় — যেমন `in` ব্যবহার করে কোনো ভ্যালু আছে কি না চেক করা যায়, `for loop` ব্যবহার করে সব এলিমেন্ট একে একে অ্যাকসেস করা যায়,এবং সেটের ভ্যালু গুলো দেখা যায় তবে Set-এর নিজস্ব মেথড ব্যবহার করে নতুন এলিমেন্ট যোগ বা মুছে Set আপডেট করা যায়।
#example:
setitem = {1,2,"3",1,3,6}
for i in setitem:
  print(i)
  #output
  #1
  #2
  #3
  #6
  #3
  # Access 2nd method using 'in' keyword. আমাদের যে set  আছে setর ভিতরে আমরা যদি কোন নির্দিষ্ট আইটেমকে বা নাম্বারকে জানতে চাই তখন এটার রেজাল্ট true অথবা false  এইভাবে দিবে। true  দিলে বুঝতে হবে সেটের ভিতর এই আইটেমটা আছে আর যদি false  হয় তার মানে এই আইটেম টা নাই.
  #example:
  setitem = {1,2,"3",1,3,6}
  print(1 in setitem)
  #output: true

# Add  set items with add() method
# পাইথন সেট এর ভিতরে আইটেম গুলোকে অ্যাড করা যায়।
Myset1 = {"apple", "banana", "cherry", "orange"}
Myset1.add("grape")
print(Myset1) # Output: {'banana', 'grape', 'cherry', 'orange', 'apple'}

#set update with update()method
# পাইথন সেট এর ভিতরে আইটেম গুলোকে আপডেট করা যায়
Myset2 = {"apple", "banana", "cherry"}
set3 = {1, 2, 3}
Myset2.update(set3)
print(Myset2)
# Output: {1, 2, 3, 'banana', 'cherry', 'apple'}

#আমরা চাইলে আমাদের listটাইপ ডাটা বা tuple টাইপ ডাটা সেটের ভিতরে এড করতে পারি.
#another defferent example
Myset3 = {"apple", "banana", "cherry"}
List1 = [1, 2, 3]
Myset3.update(List1)
print(Myset3)
# Output: { 'banana', 1, 2, 3, 'cherry', 'apple'}

# পাইথন রিমুভ সেট আইটেম এর ভেতরে দুইভাবে এলিমেন্ট রিমুভ করা যায় একটা হচ্ছে রিমুভ আরেকটা হচ্ছে ডিসকার্ড দিয়ে এই দুটোর মধ্যে একটি পার্থক্য আছে রিমুভ দিয়ে কোন এলিমেন্ট ডিলেট করতে চাইলে যদি ওই এলিমেন্ট টা সেটের ভেতরে থাকে তাহলে আউটপুট চলে আসবে আর যদি না থাকে তাহলে 
# এরোর দেখাবে এবং ডিসকার্ড দিয়ে কোন এলিমেন্ট ডিলেট করতে চাইলে ওই এলিমেন্ট যদি সেট এর ভেতরে থাকে তাহলে ডিলিট হয়ে যাবে তবে যদি না থাকে তাহলে এরর আসবে না এটাই পার্থক্য
#Remove set items
# পাইথন সেট এর ভিতরে আইটেম গুলোকে রিমুভ করা যায়
Myset4 = {"apple", "banana", "cherry",}
Myset4.remove("cherry")
print(Myset4)
# Output: {'banana', 'apple'}
#another remove method using discard
Myset5 = {"apple", "banana", "cherry",}
Myset5.discard("banana")
print(Myset5)
# Output: {'cherry', 'apple'}

#pop set items
# পাইথন পপ সেট মেথড দিয়েও সেট এর ভিতরে কোন এলিমেন্ট কে রিমুভ করা . তবে এটাতে কোন নির্দিষ্ট করে বলে দেয়া যায় না. তাহলে error  চলে আসে. এই মেথড নিজে নিজে তার ইচ্ছামত যেকোনো একটি এলিমেন্ট রিমুভ করে দেয় এবং সেট থেকে রিমুভ করা এলিমেন্ট কে আউটপুট হিসেবে দেখায়
Myset6 = {"apple", "banana", "cherry",}
Myset6.pop()
print(Myset6)
# Output: {'banana', 'cherry'} (Note: The popped item is removed 

#clear set items
# পাইথন ক্লিয়ার সেট মেথড দিয়ে সেট এর ভিতরে সব এলিমেন্ট কে একসাথে রিমুভ করা যায় 
Myset7 = {"apple", "banana", "cherry",}
Myset7.clear()
print(Myset7)
# Output: set()

#Loop set items
# পাইথন সেট এর ভিতরে আইটেম গুলোকে লুপ করা 
Myset8 = {"apple", "banana", "cherry",}
for i in Myset8:
    print(i)
    #output: apple
    #output: banana
    #output: cherry

#copy set items
# পাইথন কপি সেট মেথড দিয়ে সেট এর ভিতরে সব এলিমেন্ট কে একসাথে কপি করা যায়
Myset8 = {"apple", "banana", "cherry",}
Myset8.copy()
print(Myset8)
# Output: {'banana', 'cherry', 'apple'}

#difference set items
# পাইথন ডিফারেন্স সেট মেথড দিয়ে সেট এর ভিতরে সব এলিমেন্ট কে একসাথে ডিফারেন্স করা যায়
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
# Output: {'banana', 'cherry'}

#difference_update set items
# পাইথন ডিফারেন্স আপডেট সেট মেথড দিয়ে সেট এর ভিতরে সব এলিমেন্ট কে একসাথে ডিফারেন্স আপডেট করা যায়
set4 = {"apple", "banana", "cherry"}
set5 = {"google", "microsoft", "apple"}
set4.difference_update(set5)
print(set4)
# Output: {'banana', 'cherry'}

#intersection set items
# পাইথন ইন্টারসেকশন সেট মেথড দিয়ে সেট এর ভিতরে সব এলিমেন্ট কে একসাথে ইন্টারসেকশন করা যায়
set6 = {"apple", "banana", "cherry"}
set7 = {"google", "microsoft", "apple"}
set8 = set6.intersection(set7)
print(set8)
# Output: {'apple'}

#intersection_update set items
# পাইথন ইন্টারসেকশন আপডেট সেট মেথড দিয়ে সেট এর ভিতরে সব এলিমেন্ট কে একসাথে ইন্টারসেকশন আপডেট করা যায়
set9 = {"apple", "banana", "cherry"}
set10 = {"google", "microsoft", "apple"}
set9.intersection_update(set10)
print(set9)
# Output: {'apple'}



#delete set items
# পাইথন ডিলিট সেট মেথড দিয়ে সেট এর ভিতরে সব এলিমেন্ট কে একসাথে রিমুভ করা যায় তবে এই মেথড দিয়ে সেট টা পুরোপুরি ডিলিট হয়ে যায়
Myset9 = {"apple", "banana", "cherry",}
del Myset9
print(Myset9)
# Output: NameError: name 'Myset9' is not defined

#set join
# পাইথন সেট এর ভিতরে আইটেম গুলোকে জয়েন করা যায়. পাইথন জয়েন সেট এর ভেতরে আবার দুইটা মেথড আছে যেই দোনোটার কাজ একই দুইটা দিয়েই দুইটা আলাদা আলাদা সেট কে জয়েন করা হয় একটা হচ্ছে union আরেকটা হচ্ছে update
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)
# # Output: {1, 2, 3, 'a', 'c' 'b',}

# #another example using update method
# set4 = {"a", "b", "c"}
# set5 = {1, 2, 3}
# set4.update(set5)
# print(set4)
# Output: {3, 1, 2,  'b', 'a', 'c'}

# #Do python set excercise with w3schools

# #🧠 Python Set Methods (Python Example + Real-life Example)

# 1. difference()
# → প্রথম Set থেকে দ্বিতীয় Set-এর কমন এলিমেন্ট বাদ দিয়ে শুধু আলাদা এলিমেন্ট বের করে।

# Python Example:
# a = {1, 2, 3, 4}
# b = {3, 4}

# print(a.difference(b))

# Output:
# {1, 2}

# Real-life Example:
# তোমার ব্যাগে ৪টা বই আছে, বন্ধু ২টা নিয়ে গেছে → তোমার কাছে যেগুলো বাকি আছে।


# 2. difference_update()
# → difference() এর মতো কাজ করে, তবে আসল Set-টাই পরিবর্তন করে।

# Python Example:
# a = {1, 2, 3, 4}
# b = {3, 4}

# a.difference_update(b)

# print(a)

# Output:
# {1, 2}

# Real-life Example:
# তালিকা থেকে ব্যবহৃত জিনিস স্থায়ীভাবে কেটে দেওয়া।


# 3. intersection()
# → দুই Set-এর মধ্যে যেগুলো কমন আছে শুধু সেগুলো বের করে।

# Python Example:
# a = {1, 2, 3}
# b = {2, 3, 4}

# print(a.intersection(b))

# Output:
# {2, 3}

# Real-life Example:
# দুই বন্ধুর পছন্দের খাবারের মধ্যে মিল বের করা।


# 4. intersection_update()
# → কমন এলিমেন্ট রেখে আসল Set আপডেট করে।

# Python Example:
# a = {1, 2, 3}
# b = {2, 3, 4}

# a.intersection_update(b)

# print(a)

# Output:
# {2, 3}

# Real-life Example:
# শুধু দুজনের মিল থাকা পছন্দগুলো রেখে দেওয়া।


# 5. isdisjoint()
# → দুই Set-এর মধ্যে কোনো কমন এলিমেন্ট আছে কি না চেক করে।

# Python Example:
# a = {1, 2}
# b = {3, 4}

# print(a.isdisjoint(b))

# Output:
# True

# Real-life Example:
# দুই ক্লাসে কোনো একই ছাত্র নেই।


# 6. issubset()
# → একটি Set-এর সব এলিমেন্ট অন্য Set-এর ভিতরে আছে কি না চেক করে।

# Python Example:
# a = {1, 2}
# b = {1, 2, 3}

# print(a.issubset(b))

# Output:
# True

# Real-life Example:
# মনিটরদের তালিকা ছাত্রদের তালিকার অংশ।


# 7. issuperset()
# → একটি Set-এর ভিতরে অন্য Set-এর সব এলিমেন্ট আছে কি না চেক করে।

# Python Example:
# a = {1, 2, 3}
# b = {1, 2}

# print(a.issuperset(b))

# Output:
# True

# Real-life Example:
# সব ছাত্রের তালিকার মধ্যে মনিটরদের তালিকা আছে।


# 8. symmetric_difference()
# → দুই Set-এর কমন বাদ দিয়ে শুধু আলাদা এলিমেন্ট বের করে।

# Python Example:
# a = {1, 2, 3}
# b = {3, 4, 5}

# print(a.symmetric_difference(b))

# Output:
# {1, 2, 4, 5}

# Real-life Example:
# দুইজনের আলাদা আলাদা পছন্দ বের করা।


# 9. symmetric_difference_update()
# → symmetric_difference() এর মতো কাজ করে, তবে আসল Set-টাই পরিবর্তন করে।

# Python Example:
# a = {1, 2, 3}
# b = {3, 4, 5}

# a.symmetric_difference_update(b)

# print(a)

# Output:
# {1, 2, 4, 5}

# Real-life Example:
# কমন জিনিস বাদ দিয়ে নতুন তালিকাটা স্থায়ীভাবে রেখে দেওয়া।


# 📌 শর্ট ট্রিক:
# difference → আমার থেকে বাদ
# intersection → মিল
# disjoint → মিল নেই
# subset → আমি ওর ভিতরে
# superset → ও আমার ভিতরে
# symmetric → কমন বাদ
# update → আসল Set পরিবর্তন

#  Python Frozen Set

# Frozen Set হলো Set-এর মতোই একটি ডাটা টাইপ, কিন্তু এটি immutable (পরিবর্তন করা যায় না)।

# মানে:
# → Frozen Set তৈরি করার পর নতুন এলিমেন্ট add করা যায় না।
# → remove করা যায় না।
# → update করা যায় না।
# → শুধু read/access করা যায়।

# তৈরি করার জন্য:
# frozenset()

# Python Example:

# numbers = frozenset([1, 2, 3, 4])

# print(numbers)

# Output:
# frozenset({1, 2, 3, 4})


# এলিমেন্ট আছে কি না চেক:

# numbers = frozenset([1, 2, 3])

# print(2 in numbers)

# Output:
# True


# for loop দিয়ে অ্যাকসেস:

# numbers = frozenset([10, 20, 30])

# for i in numbers:
#     print(i)

# Output:
# 10
# 20
# 30


# ❌ পরিবর্তন করা যায় না:

# numbers = frozenset([1, 2])

# numbers.add(3)

# Output:
# AttributeError


# 🧠 Real-life Example:

# Set = হোয়াইটবোর্ডে লেখা তালিকা
# → চাইলে মুছতে বা লিখতে পারো

# Frozen Set = ল্যামিনেট করা প্রিন্ট করা তালিকা
# → দেখা যাবে, কিন্তু বদলানো যাবে না


# 📌 মনে রাখার ট্রিক:

# set
# → mutable (পরিবর্তন করা যায়)

# frozenset
# → immutable (পরিবর্তন করা যায় না)