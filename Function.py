#plus
sum1 = 20
sum2 = 30
sum3 = sum1 + sum2
print(sum3)
#minas
sum4 = 20
sum5 = 30
sum6 = sum4 - sum5
print(sum6)
#আমাদের প্রত্যেকটা ফাংশনের যোগ করার জন্য আলাদা আলাদা variable  করা লাগতেছে তারপর প্রিন্ট করা লাগতেছে বিয়োগ  করার জন্য আলাদা বেরিয়েবল লাগতেছে তারপর আবার প্রিন্ট করা লাগতেছে তো এরকম ভাবে যোগ বিয়োগ গুণ ,ভাগ  সবকিছুর জন্য আলাদা আলাদা variable  লাগতেছে এবং প্রিন্ট করতে হচ্ছে .আমাদের পাইথন ফাংশনের কাজ হচ্ছে এই সবগুলা code ke  ছোট করে  লিখে দেয়া এবং একবার variable  করে দিলে আমরা যতবার ইচ্ছা ততবার ব্যবহার করতে পারি এবং প্রিন্ট করতে পারি .আমাদের ফাংশন এর কাজ হচ্ছে এই সবগুলা code কে ছোট করে লিখে দেয়া এবং একবার variable  করে দিলে আমরা যতবার ইচ্ছা ততবার ব্যবহার করতে পারি এবং প্রিন্ট করতে পারি .এবং কোন নির্দিষ্ট ভ্যালু না দিয়েই যে ভ্যালু দিয়ে  মন চায়, যতবার মন চায় ততবারই যোগ বিয়োগ গুণ ভাগ সব ফাংশন করা যাবে

#পাইথন ফাংশন ইউজ করার সময় সব সময় ডিপ keyword দিয়ে শুরু করতে হয়
#Function example
def funcationname(a, b):
    sum = a + b
    print(sum)
funcationname(20, 30)
funcationname(50, 60)
funcationname(100, 200)

#another example
def funcationname1(a, b):
    sum = a - b
    print(sum)
funcationname1(20, 30)
funcationname1(50, 60)
funcationname1(100, 200)
#আমরা যদি ফাংশন এর ভিতরে return keyword ব্যবহার করি তাহলে আমরা ফাংশন এর ভিতরে যে কোন ভ্যালু কে return করতে পারি এবং সেই ভ্যালু কে আমরা অন্য কোন variable এ রাখতে পারি এবং সেই variable কে আমরা প্রিন্ট করতে পারি
def funcationname(a, b):
    sum = a + b
    return sum
result = funcationname(20, 30)
print(result)
result1 = funcationname(50, 60)
print(result1)
result2 = funcationname(100, 200)
print(result2)
