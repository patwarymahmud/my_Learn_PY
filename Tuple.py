# # পাইথন list এবং পাইথন Tuple এ দুইটা দেখতে same। তবে এই দুইটার মধ্যে দুটো মেজর পার্থক্য রয়েছে। প্রথমত হলো ব্রেকেট। পাইথনের সব জায়গাতেই কিংবা বেশিরভাগ জায়গাতেই পাইথন list  থার্ড ব্রেকেট ইউজ করা হয়। তবে পাইথন Tuple a  ফার্স্ট ব্রেকেট ইউজ করা হয়। এবং আরেকটা পার্থক্য হচ্ছে পাইথন list মিউটেবল। চাইলেই এটার  লিস্টের ভ্যালুটা সেটা নাম্বার হতে পারে, নাম হতে পারে, ফলের নাম হতে পারে, এটা চেঞ্জ করা যায়। কিন্তু পাইথন Tuple এটা ইমিউটেবল। এটা চাইলেই এটার মান বা ভ্যালু চেঞ্জ করা যায় না।

# # Python Tuples := are ordered, immutable, and allow duplicate values. They are defined using parentheses ().
#  NewTuples = (1, 2, 3, "Mahamud", "Me")
#  print(type(NewTuples))

# Access tuples with 3 ruls
#--------------------------
    #Index call
#   NewTuples[1] = 20  # This will raise an error because tuples are immutable
#   print(NewTuples)

#  #Negative Indexing
   #Negative Indexing করার সময় আউটপুট উল্টা দিক থেকে শুরু হয় এবং সামনে মাইনাস দিতে হবে
   # এবং নেগেটিভ ইনডেক্সে জিরো থেকে না1 থেকেই শুরু হয়.
#  print(NewTuples[-1]) # Output: Me
#  print(NewTuples[-2]) # Output: Mahamud 

#  #Range of Indexing
#  print(NewTuples[0:3]) # Output: (1, 2, 3)
#  print(NewTuples[3:5])  # Output: ('Mahamud', 'Me')
#  print(NewTuples[:4])  # Output: (1, 2, 3, 'Mahamud')
#  print(NewTuples[2:5])  # Output: (3, 'Mahamud', 'Me')
#  print(NewTuples[1:4])  # Output: (2, 3, 'Mahamud')

# #Update Tuples
#---------------
# # Since tuples are immutable, we cannot change their values directly. However, we can convert the tuple to a list, make the necessary changes, and then convert it back to a tuple.
# # Convert the tuple to a list
# ThisTuple = ("a", 2, "apple", "banana", "cherry")
# print(type(list(ThisTuple)))  # Output: <class 'list'>
# a = list(ThisTuple)  # Convert to list
# a.append("orange")  # Add a new element to the list
# print(a)  # Output: ['a', 2, 'apple', 'banana', 'cherry', 'orange']
#  
# print(d)  # Output: orange
# print(e)  # ThisTuple = tuple(a)  # Convert back to tuple
# print(ThisTuple)  # Output: ('a', 2, 'apple', 'banana', 'cherry', 'orange')

# #Unpacking Tuples
# # Unpacking a tuple means assigning its values to individual variables. The number of variables must match the number of elements in the tuple.
# fruits = ("apple", "banana", "cherry", "orange", "grape", "mango")
# a, b, c, d, e, f = fruits  # Unpacking the tuple
# print(a)  # Output: apple
# print(b)  # Output: banana
# print(c)  # Output: cherry
# print(d)  # Output: orange
# print(e)  # Output: grape
# print(f)  # Output: mango
# #another example
colors = ("red", "green", "blue", "yellow", "orange")
(*a, b) = colors
print(b) # Output: orange
print(a) # Output: ['red', 'green', 'blue', 'yellow']
#another example
fruits = ("apple", "banana", "cherry", "orange", "grape")
(a, *b, c) = fruits
print(a) # Output: apple
print(b) # Output: ['banana', 'cherry', 'orange']
print(c) # Output: grape

#loop Tuples
# We can loop through the elements of a tuple using a for loop.
fruits = ("apple", "banana", "cherry", "orange", "grape")
for x in fruits:
  print(x)
#output:
# apple
# banana
# cherry
# orange
# grape
#loop এইভাবে ব্যবহার করলে list ar প্রতিটা আইটেমের ইনডেক্স number কে output করবে
for i in range(len(fruits)):
  print(i)
  #output:
  #0
  #1
  #2
  #3
  #4
#loop এইভাবে ব্যবহার করলে list ar প্রতিটা আইটেমেকে output করবে
for i in range(len(fruits)):
  print(fruits[i])
  #output:
# apple
# banana
# cherry
# orange
# grape

# We can also use a while loop to iterate through the tuple.
foll = ("guava", "mango", "cherry", "orange", "date")
i = 0
while i < len(foll):
  print(foll[i])
  i = i + 1
  #output:
# guava
# mango 
# cherry
# orange
# date

#join 2 Tuples
# We can join two or more tuples using the + operator.
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: ('a', 'b', 'c', 1, 2, 3)
#another example
num1 = (1, 2, 3, 4, 5)
print(num1 * 2)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
#এখানে চাইলে যোগ বিয়োগ গুন ভাগ সবাই করা যাবে, তবে স্ট্রিং টাইপ হলে যোগ বিয়োগ গুন করা যাবে

#Tuple Methods
# Python has two built-in methods for tuples: count() and index().
# The count() method returns the number of times a specified value appears in the tuple.
# Tuple Method মূলত দুই ধরনের — index() এবং count()।

# index() Method ব্যবহার করা হয় Tuple-এর ভেতরে কোনো নির্দিষ্ট value কোন index position-এ আছে তা বের করার জন্য। অর্থাৎ কোনো string, integer বা অন্য কোনো value Tuple-এর কত নম্বর অবস্থানে রয়েছে, সেটা index() এর মাধ্যমে জানা যায়।

# অন্যদিকে count() Method ব্যবহার করা হয় Tuple-এর ভেতরে কোনো নির্দিষ্ট value কতবার রয়েছে তা গণনা করার জন্য। অর্থাৎ কোনো নাম, সংখ্যা বা value Tuple-এর মধ্যে কয়বার এসেছে, সেটা count() Method দ্বারা বের করা হয়।
fruits = ( "apple", "banana", "cherry", "orange", "grape", "banana")
a = fruits.index("cherry") 
print(a)# Output: 2

b = fruits.count("banana")
print(b) # Output: 2
