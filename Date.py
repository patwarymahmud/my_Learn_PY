# Python Date & Time (Beginner Friendly)
import datetime
a = datetime.datetime.now()
print(a)


# =========================================
# Python Date & Time (Beginner Friendly)
# =========================================

# Python Date & Time ব্যবহার করা হয়:
#
# 1. বর্তমান তারিখ বের করতে
# 2. বর্তমান সময় বের করতে
# 3. জন্মতারিখ হিসাব করতে
# 4. বয়স বের করতে
# 5. কতদিন বাকি আছে হিসাব করতে
# 6. Attendance System বানাতে
# 7. E-commerce Order Date রাখতে
# 8. Calendar App বানাতে
# 9. Logging System তৈরি করতে

# =========================================
# Date & Time Module Import
# =========================================

import datetime

# অথবা

from datetime import datetime

# =========================================
# বর্তমান Date & Time বের করা
# =========================================

from datetime import datetime

now = datetime.now()

print(now)

# Example Output:
#
# 2026-06-06 15:30:45.123456

# =========================================
# শুধু বর্তমান Date বের করা
# =========================================

from datetime import date

today = date.today()

print(today)

# Example Output:
#
# 2026-06-06

# =========================================
# Year, Month, Day বের করা
# =========================================

from datetime import datetime

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)

# Example Output:
#
# 2026
# 6
# 6

# =========================================
# strftime() Function
# =========================================

# strftime() এর পূর্ণরূপ:
#
# String Format Time
#
# এটি Date & Time কে
# নিজের ইচ্ছামতো Format করতে ব্যবহার করা হয়।

# =========================================
# Year বের করা
# =========================================

print(now.strftime("%Y"))

# Output:
#
# 2026

# =========================================
# Month Number
# =========================================

print(now.strftime("%m"))

# Output:
#
# 06

# =========================================
# Day Number
# =========================================

print(now.strftime("%d"))

# Output:
#
# 06

# =========================================
# Full Week Name
# =========================================

print(now.strftime("%A"))

# Output:
#
# Saturday

# =========================================
# Short Week Name
# =========================================

print(now.strftime("%a"))

# Output:
#
# Sat

# =========================================
# Full Month Name
# =========================================

print(now.strftime("%B"))

# Output:
#
# June

# =========================================
# Short Month Name
# =========================================

print(now.strftime("%b"))

# Output:
#
# Jun

# =========================================
# Important Format Codes
# =========================================

# %Y = Full Year
# Example: 2026

# %y = Short Year
# Example: 26

# %m = Month Number
# Example: 06

# %B = Full Month Name
# Example: June

# %b = Short Month Name
# Example: Jun

# %d = Day Number
# Example: 06

# %A = Full Week Name
# Example: Saturday

# %a = Short Week Name
# Example: Sat

# %H = Hour (24 Hour Format)
# Example: 15

# %I = Hour (12 Hour Format)
# Example: 03

# %M = Minute
# Example: 30

# %S = Second
# Example: 45

# %p = AM / PM
# Example: PM

# %j = Day Of Year
# Example: 157

# %U = Week Number
# Example: 22

# %w = Weekday Number
# Example: 6

# %c = Full Date & Time

# %x = Local Date

# %X = Local Time

# =========================================
# Custom Date Format
# =========================================

print(now.strftime("%d-%m-%Y"))

# Output:
#
# 06-06-2026

print(now.strftime("%d/%m/%Y"))

# Output:
#
# 06/06/2026

print(now.strftime("%A, %d %B %Y"))

# Output:
#
# Saturday, 06 June 2026

# =========================================
# Time Format
# =========================================

print(now.strftime("%H:%M:%S"))

# Output:
#
# 15:30:45

# =========================================
# AM / PM Format
# =========================================

print(now.strftime("%I:%M %p"))

# Output:
#
# 03:30 PM

# =========================================
# strptime() Function
# =========================================

# strptime() এর পূর্ণরূপ:
#
# String Parse Time
#
# String কে Date Object এ রূপান্তর করে।

from datetime import datetime

date_string = "06-06-2026"

date_obj = datetime.strptime(
    date_string,
    "%d-%m-%Y"
)

print(date_obj)

# =========================================
# Date Difference বের করা
# =========================================

from datetime import date

d1 = date(2026, 6, 1)
d2 = date(2026, 6, 6)

print(d2 - d1)

# Output:
#
# 5 days

# =========================================
# Beginner Friendly Important Functions
# =========================================

# datetime.now()
#
# বর্তমান Date & Time দেয়।

# date.today()
#
# বর্তমান Date দেয়।

# strftime()
#
# Date Format করে।

# strptime()
#
# String কে Date এ Convert করে।

# =========================================
# Important Attributes
# =========================================

# .year
# .month
# .day
# .hour
# .minute
# .second

# =========================================
# Real Life Example
# =========================================

# Attendance Software

from datetime import datetime

entry_time = datetime.now()

print(entry_time)

# ছাত্র কখন এসেছে
# সেটা Save করার জন্য ব্যবহার করা যায়।

# =========================================
# Beginner Shortcut
# =========================================

# প্রথমে এই ৫টি শিখো:

# datetime.now()
# date.today()
# strftime()
# %Y %m %d
# %A %B

# এগুলো ভালোভাবে শিখে ফেললে
# Python Date & Time এর প্রায় 70%
# কাজ করতে পারবে।

# =========================================
# One Line Definition
# =========================================

# Python Date & Time ব্যবহার করা হয়
# তারিখ, সময়, দিন, মাস, বছর, সপ্তাহ,
# সময়ের পার্থক্য এবং Date Formatting
# সম্পর্কিত কাজ করার জন্য।
#
# datetime Module হলো
# Python Date & Time এর প্রধান Module।
# =========================================