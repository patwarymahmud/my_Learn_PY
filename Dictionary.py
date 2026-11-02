#Python Dictionary
#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
# নির্দিষ্ট কোন ডিকশনারির ইনফো বের করতে গেলে প্রিন্টের ভেতরে শুধু ভেরিয়েবল টা এবং তার ভিতরে থার্ড ব্রেকেট ইউজ করে ওই ডিকশনারির 'কি'টা লিখতে হবে key holo, যেমন:Mahamud, sabbir, year, agulu যেমন: print(studentinfo['Mahamud']['location']) তাহলে আউটপুট হবে 'Chandpur' ,আবার যদি আমরা শুধু মাহমুদকে কল করি তাহলে তার ভেতরে সকল ইনফরমেশন গুলা দেখাবে আউটপুট হিসেবে ,এবং শুধুমাত্র ভেরিয়েবল কে কল করলে সকল স্টুডেন্টের ইনফরমেশন দেখাবে 
# studentinfo = {
#   "Mahamud": {
#     "name": "Mahamud",
#     "location": "Chandpur",
#     "Study": "Pythom",
#     "Subject": "Commerce",
#     "roll": 12,
#     "number": 12345
#   },
#   "Sabbir": {
#     "name": "Sabbir",
#     "location": "Dhaka",
#     "Study": "Python",
#     "Subject": "Science",
#     "roll": 13,
#     "number": 67890
#   },
#   "year": 1971
# }
#print(studentinfo)
# print(studentinfo["Mahamud"])

# #Dictionary Access item
# print(studentinfo['year'])

#get মেথড ইউজ করেও কোন একটা ডিকশনারির সমস্ত ইনফরমেশন বের করা যায় যেমন আমরা এখানে sabbir information get method মাধ্যমে পেয়ে গেলাম
# #dictionary Using get mathod
# x = studentinfo.get("Sabbir")
# print(x)

# #dictionary keys mathod
# # dictionary "keys  " মেথড এর ভেতরে কোনরকম আরগুমেন্ট রাখা যায় না, তা না হলে error চলে আসে তাই ব্রেকেটের ঘর খালি থাকে এবং প্রিন্ট করার পর সবগুলা "কি" দেখা যায়।
# x = studentinfo.keys()
# print(x) #output: dict_keys(['Mahamud', 'Sabbir', 'year'])

# dictionary "value" মেথড এর ভেতরে কোনরকম আরগুমেন্ট রাখা যায় না, তা না হলে error চলে আসে তাই ব্রেকেটের ঘর খালি থাকে এবং প্রিন্ট করার পর সবগুলা "value" দেখা যায়।
# #dictionary value mathod
# y = studentinfo.values()
# print(y)

#Change dictionary litem
studentinfo = {
  "Mahamud": {
    "name": "Mahamud",
    "location": "Chandpur",
    "Study": "Pythom",
    "Subject": "Commerce",
    "roll": 12,
    "number": 12345
  },
  "Sabbir": {
    "name": "Sabbir",
    "location": "Dhaka",
    "Study": "Python",
    "Subject": "Science",
    "roll": 13,
    "number": 67890
  },
  "year": 1971
}
studentinfo["year"] = 2004
#print(studentinfo)


#dictionary car
# car = {
#     "brand": "BMW",
#     "model": "X5",
#     "year": 2024
# }
# print(car) #output{'brand': 'BMW', 'model': 'X5', 'year': 2024}
# নির্দিষ্ট key এর value print
# #print(car["brand"]) Output: 'BMW'
# print(car.get("model")) 
#change car dictionary values with using get mathod
#car["year"] = 2020 #output: "brand": "BMW", "model": "x5", "year": 2020

# # dictionary update mathod
# studentinfo.update({"Sabbir":"sabbir is an CSE student"})
# print(studentinfo["Sabbir"]) #output: sabbir is an CSE student

#add dictionary items
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car["color"] = "red"
#another example
#x = {'type' : 'fruit', 'name' : 'apple'}
#x.update({'color' : 'green'})


# # #python dictionary pop mathode
# # studentinfo.pop("Mahamud")
# # print(studentinfo)
# # # another one
# # studentinfo.pop("year")
# # print(studentinfo)

# #popitem dictonary
# # ডিকশনারি pop আইটেম এর ভেতরে নির্দিষ্ট করে কোন ডিকশনারি নাম বলে দেয়া লাগে না সে অটোমেটিকলি একদম লাস্টের আইটেমটাকে একবার দিলে ডিলেট করে ফেলে দ্বিতীয়বার দিলে তার পরের যে লাস্ট আইটেম সেইটা ডিলিট করে ফেলে এইভাবে সে অটোমেটিকলি ডিলিট করে ফেলে কোন ডিকশনারি দেয়া লাগে না
# studentinfo.popitem()
# studentinfo.popitem()
# studentinfo.popitem()
# print(studentinfo)

#Dictionary loop
for x in studentinfo:
  print(x)
for a in studentinfo.values():
  print(a)
#Dictionary keys with using loop
for b in studentinfo.keys():
  print(b)
#Dictionary items with using loop
# পাইথন ডিকশনারি আইটেম উইথ ইউসিং লুপস দিয়ে ডিকশনারি আইটেম এবং ডিকশনারি এর ভ্যালুজ আইটেম গুলা একসাথে বের করা যায়
for item in studentinfo.items():
  print(item)

#  # dictionary del() method example
student = {
    "name": "Hasan",
    "age": 20,
    "city": "Dhaka"
}
del student["age"]
print(student)
# Output:
# {'name': 'Hasan', 'city': 'Dhaka'}

#dictionary clear() method example
student = {
    "name": "Hasan",
    "age": 20,
    "city": "Dhaka"
}
student.clear()
print(student)
# Output:
# {}

#copy dictionary
studentinfo1 = {
  "sum1": 20,
  "sum2":40,
  "sum3":60
  }
print(studentinfo1)
md = studentinfo1.copy()
print(md)

#dict dictionary mathod
# dict  ডিকশনারি দিয়েও কপি ডিকশনারি মেথড এর মত কাজ করা যায় সেম হুবহু
x = dict(studentinfo1)
print(x)

#correct function to print the number of key/value pairs in the dictionary:
x = {'type' : 'fruit', 'name' : 'banana'}
print(len(x))

#correct syntax for looping through the values of this dictionary:
x = {'type' : 'fruit', 'name' : 'apple'}
for y in x.values():
  print(y)

# correct syntax for looping through the keys AND values of this dictionary:
x = {'type' : 'fruit', 'name' : 'apple'}
for y, z in x.items():
  print(y, z)

  # correct syntax for looping through the keys of this dictionary:
x = {'type' : 'fruit', 'name' : 'apple'}
for y in x.keys():
  print(y)

#Nested dictionary
# a correct syntax for printing the name 'May'?
a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}
print(customers['c2']['name'])

#another example

a = {'name' : 'John', 'age' : 20}
b = {'name' : 'May', 'age' : 23}
customers = {'c1' : a, 'c2' : b}
for x, obj in customers.items():
  print(x)  
  for y in obj:
    print(y + ':', obj[y])

    # Nested Dictionary Example

a = {'name': 'John', 'age': 20}
b = {'name': 'May', 'age': 23}

customers = {
    'c1': a,
    'c2': b
}

for x, obj in customers.items():
    print(x)

    for y in obj:
        print(y + ':', str(obj[y]))

# Output:
# c1
# name: John
# age: 20
#
# c2
# name: May
# age: 23


# Explanation:
# customers = বাইরের Dictionary
# c1 এবং c2 = Key
# a এবং b = ভিতরের Dictionary (Nested Dictionary)
#
# .items() → key এবং value একসাথে দেয়
#
# x   → c1 / c2
# obj → {'name':'John','age':20}
#
# ভিতরের loop:
# y → name, age
# obj[y] → John, 20
#
# Nested Dictionary = Dictionary এর ভিতরে Dictionary