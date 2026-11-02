# #break python
#আমরা যদি কোন প্রোগ্রামকে নির্দিষ্ট জায়গায় immediately থামাতে চাইতাহলে আমরা break মেথড ইউজ করব এরকমভাবে প্রিন্ট করলে শুধু লিস্টের ভেতরে ওই এলিমেন্টটা কত নাম্বারে আছে সেই নাম্বারগুলা  দেখাবে এবং range ও len()use kore 
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# for x in range(len(fruits)):
#   if x == 4:
#     break
#   #print(x)
#output:
#0
#1
#2
#3
#   #another print way
#   # এভাবে print  করলে লিস্টের এলিমেন্ট এবং ওই  এলিমেন্ট নাম্বার সহ একসাথে প্রিন্ট হবে
#   print(fruits[x])

#   #continue python
#আমরা যদি এই কন্টিনিউ মেথড ইউজ করি তাহলে আমাদের ভেরিএবেল নাম্বার যত থাকবে সেখানে ব্রেক না করে সে তার পরের নাম্বারগুলো কেউ সেই প্রিন্ট করবে range ও len()use kore 
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for a in range(len(fruits)):
   if a == 3:
     continue
   #print(a)
#output:
#0
#1
#2
#3
#4

# #another print way
#   print(fruits[a])

# #তবে আমরা যদি রেঞ্জ এবং লেন এগুলা কেটে দিয়ে জাস্ট আমাদের  লিস্টের ভেরিয়েবল টাকে কল করি যেমন শুধুমাত্র ফ্রুটস কে তাহলে আমাদের ওই লিস্টের সমস্ত এলিমেন্ট গুলো প্রিন্ট করে দেখাবে এবং যেখানে ব্রেক দিবো ব্রেক হবে কন্টিনিউ দিলে কন্টিনিউ হবে
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# for x in fruits:
#   if x == "date":
#     break
#   print(x)
# #continue
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# for x in fruits:
#   if x == "date":
#     continue
#   print(x)

#using while loop with break and continue
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
i = 0
while i < len(fruits):
  if fruits[i] == "date":
    break
  print(fruits[i])
  i = i + 1
#continue
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
i = 0
while i < len(fruits):
  if fruits[i] == "date":
    i = i + 1
    continue
  print(fruits[i])
  i = i + 1