# ==========================================================
# Python Try-Except (Beginner Friendly Complete Notes)
# ==========================================================

# Python Try-Except হলো Error Handling System।
#
# অর্থাৎ Program চলার সময় কোনো Error আসলে
# Program Crash না করে Error Handle করার জন্য
# Try-Except ব্যবহার করা হয়।

# ==========================================================
# Python Try-Except এর 4টি প্রধান অংশ (Functions/Blocks)
# ==========================================================

# 1. try
# 2. except
# 3. else
# 4. finally

# ==========================================================
# Real Life Example
# ==========================================================

# ধরো তুমি ATM বুথে টাকা তুলতে গেছো।

# try
# = টাকা তোলার চেষ্টা করা।

# except
# = কোনো সমস্যা হলে (PIN ভুল, কার্ড Error)
#   Error Message দেখানো।

# else
# = সব ঠিক থাকলে টাকা পাওয়া।

# finally
# = Error হোক বা না হোক,
#   ATM কার্ড ফেরত পাওয়া।

#try & except example:
try:
    print("give me output number 1 line")
except:
    print("tomar net slow speed varaw")
    print("give me function")
    print("give me 500 line code")
    #output:
    # give me output number 1 line
    # give me 500 line code
    # give me function 
    # give me 500 line code

# ==========================================================
# Basic Syntax
# ==========================================================

try:
    # যে কোডে Error আসতে পারে

    pass

except:
    # Error হলে চলবে

    pass

else:
    # Error না হলে চলবে

    pass

finally:
    # সব সময় চলবে

    pass

# ==========================================================
# 1. TRY BLOCK
# ==========================================================

# try Block এর ভিতরে এমন Code লেখা হয়
# যেখানে Error আসার সম্ভাবনা থাকে।

try:
    print(10 / 0)

except:
    print("Error হয়েছে")

# ==========================================================
# 2. EXCEPT BLOCK
# ==========================================================

# Error হলে except Block কাজ করে।

try:
    print(10 / 0)

except:
    print("Error হয়েছে")

# Output:
#
# Error হয়েছে

# ==========================================================
# Try-Except না থাকলে
# ==========================================================

print(10 / 0)

print("Hello")

# Output:
#
# ZeroDivisionError
#
# Program বন্ধ হয়ে যাবে।
#
# Hello Print হবে না।

# ==========================================================
# Try-Except থাকলে
# ==========================================================

try:
    print(10 / 0)

except:
    print("Error হয়েছে")

print("Hello")

# Output:
#
# Error হয়েছে
# Hello

# Program Crash করবে না।

# ==========================================================
# 3. ELSE BLOCK
# ==========================================================

# Error না হলে else Block চলবে।

try:
    print(10 / 2)

except:
    print("Error")

else:
    print("সব ঠিক আছে")

# Output:
#
# 5.0
# সব ঠিক আছে

# ==========================================================
# Error হলে Else চলবে না
# ==========================================================

try:
    print(10 / 0)

except:
    print("Error")

else:
    print("সব ঠিক আছে")

# Output:
#
# Error

# ==========================================================
# 4. FINALLY BLOCK
# ==========================================================

# Error হোক বা না হোক
# finally সব সময় চলবে।

try:
    print(10 / 0)

except:
    print("Error")

finally:
    print("Program শেষ")

# Output:
#
# Error
# Program শেষ

# ==========================================================
# Error না হলেও Finally চলবে
# ==========================================================

try:
    print(10 / 2)

except:
    print("Error")

finally:
    print("Program শেষ")

# Output:
#
# 5.0
# Program শেষ

# ==========================================================
# Real Life Restaurant Example
# ==========================================================

# try
#
# খাবার অর্ডার করা।

# except
#
# খাবার না থাকলে ক্ষমা চাওয়া।

# else
#
# খাবার পেলে খাওয়া শুরু করা।

# finally
#
# খাওয়া হোক বা না হোক,
# বিল পরিশোধ করে বের হওয়া।

# ==========================================================
# Specific Error Handling
# ==========================================================

# নির্দিষ্ট Error ধরার জন্য।

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Zero দিয়ে ভাগ করা যায় না")

# Output:
#
# Zero দিয়ে ভাগ করা যায় না

# ==========================================================
# Multiple Except
# ==========================================================

try:
    num = int("abc")

except ValueError:
    print("ভুল Number")

except ZeroDivisionError:
    print("Zero Error")

# Output:
#
# ভুল Number

# ==========================================================
# Error Message দেখা
# ==========================================================

try:
    print(10 / 0)

except Exception as e:
    print(e)

# Output:
#
# division by zero

# e এর ভিতরে আসল Error Message থাকে।

# ==========================================================
# সবচেয়ে ব্যবহৃত Structure
# ==========================================================

try:
    # Risky Code

    pass

except Exception as e:
    print(e)

else:
    print("Success")

finally:
    print("Done")

# ==========================================================
# Beginner Shortcut
# ==========================================================

# try
# = কাজ করার চেষ্টা করো

# except
# = Error হলে সামলাও

# else
# = Error না হলে চালাও

# finally
# = সব অবস্থায় শেষ কাজ করো

# ==========================================================
# One Line Definition
# ==========================================================

# Python Try-Except হলো এমন একটি Error Handling System,
# যা Program Crash হওয়া থেকে বাঁচায় এবং Error কে
# সুন্দরভাবে Handle করতে সাহায্য করে।
# ==========================================================