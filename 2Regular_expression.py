# ==========================================================
# MOST IMPORTANT META CHARACTERS
# ==========================================================

# .
# ^
# $
# *
# +
# ?
# []
# [^]
# {}
# ()
# |

# ==========================================================
# . (Dot)
# ==========================================================

# যেকোনো ১টি Character

print(re.findall("c.t", "cat"))

# Output:
# ['cat']

print(re.findall("c.t", "c7t"))

# Output:
# ['c7t']

# ==========================================================
# ^ (Caret)
# ==========================================================

# String এর শুরু

F = bool(re.search("^Python", "Python is easy"))
print(F)
# Output:
# True
#another example:
import re
text =  "1 is the spacial characters"
pattern = "^1"
a = re.findall(pattern,text)
if a:
  print("yes, 1 is spacial characters")
else:
  print("nope, 1 is not spacial characters")
#output:yes, 1 one is spacial characters

# ==========================================================
# $ (Dollar Sign)
# ==========================================================

# String এর শেষ

A = (bool(re.search("easy$", "Python is easy")))
print
# Output:
# True
#another example
import re 
text = "is the characters spacial"
pattern = "spacial$"

a = re.findall(pattern,text)
if a:
  print("yes, we find spacial characters")
else:
  print("nope, we not finded spacial  characters")
  #output: yes, we find spacial characters
  #another example
  import re 
text = "is the spacial characters "
pattern = "spacial$"

a = re.findall(pattern,text)
if a:
  print("yes, we find spacial characters")
else:
  print("nope, we not  finded spacial characters ")
  #output: nope, not spacial  not characters finded


# ==========================================================
# * (Asterisk)
# ==========================================================

# 0 বা তার বেশি বার

print(re.findall("ab*", "abbb"))

# Output:
# ['abbb']

# ==========================================================
# + (Plus Sign)
# ==========================================================

# 1 বা তার বেশি বার

print(re.findall("ab+", "abbb"))

# Output:
# ['abbb']

# ==========================================================
# ? (Question Mark)
# ==========================================================

# 0 বা 1 বার

print(re.findall("colou?r", "color colour"))

# Output:
# ['color', 'colour']
# ? এর আসল অর্থ
# u?

# মানে:

# u থাকতে পারে 0 বার
# অথবা
# u থাকতে পারে 1 বার

# অর্থাৎ u Optional।

# ==========================================================
# [] (Character Set)
# ==========================================================

print(re.findall("[abc]", "abcdef"))

# Output:
# ['a', 'b', 'c']

# ==========================================================
# [^] (NOT Character Set)
# ==========================================================

print(re.findall("[^abc]", "abcdef"))

# Output:
# ['d', 'e', 'f']

# ==========================================================
# {} (Curly Braces)
# ==========================================================

# কতবার Match হবে

print(re.findall("a{3}", "aa aaa aaaa"))

# Output:
# ['aaa', 'aaa']
# Example:

import re

print(re.findall("a{3}", "aa aaa aaaa"))

# Output:
# ['aaa', 'aaa']

# Explanation:

# a{3}
# মানে a ঠিক 3 বার থাকতে হবে।

# String:
# aa aaa aaaa

# প্রথম অংশ:
# aa
#
# এখানে মাত্র 2টা a আছে।
# তাই Match হবে না।

# দ্বিতীয় অংশ:
# aaa
#
# এখানে ঠিক 3টা a আছে।
# তাই Match হবে।
#
# Output:
# ['aaa']

# তৃতীয় অংশ:
# aaaa
#
# এখানে 4টা a আছে।
#
# Python বাম দিক থেকে Match শুরু করে:
#
# aaaa
# ^^^
#
# প্রথম 3টা a নিয়ে Match করে।
#
# Output:
# ['aaa', 'aaa']

# খেয়াল করো:
#
# aaaa
# ^^^
#    ^
#
# শেষের 1টা a আলাদা করে আর Match হয় না,
# কারণ a{3} ঠিক 3টা a চায়।

# Beginner Shortcut:
#
# a{3}
# = a ঠিক 3 বার
#
# aa
# ❌ Match না
#
# aaa
# ✔ Match
#
# aaaa
# ✔ প্রথম 3টা a Match
#
# তাই Output:
# ['aaa', 'aaa']

# ==========================================================
# () (Group)
# ==========================================================

re.search("(cat)", "cat")

# Group তৈরি করে।
# ==========================================================
# | (OR Operator)
# ==========================================================

print(re.findall("cat|dog", "cat dog"))

# Output:
# ['cat', 'dog']

# ==========================================================
# SPECIAL SEQUENCES
# ==========================================================

# \d
# \D
# \w
# \W
# \s
# \S
# \b
# \B

# ==========================================================
# \d (Digit)
# ==========================================================

print(re.findall(r"\d", "A1B2"))

# Output:
# ['1', '2']

# Number খুঁজে।

# ==========================================================
# \D (Non Digit)
# ==========================================================

print(re.findall(r"\D", "A1B2"))

# Output:
# ['A', 'B']

# Number ছাড়া সব।

# ==========================================================
# \w (Word Character)
# ==========================================================

print(re.findall(r"\w", "abc_123"))

# Output:
# ['a', 'b', 'c', '_', '1', '2', '3']

# a-z
# A-Z
# 0-9
# _
# Example:

import re

print(re.findall(r"\w", "abc_123"))

# Output:
# ['a', 'b', 'c', '_', '1', '2', '3']

# Explanation:

# \w
#
# = Word Character
#
# Regex-এ Word Character বলতে বোঝায়:
#
# a-z   (ছোট হাতের অক্ষর)
# A-Z   (বড় হাতের অক্ষর)
# 0-9   (সংখ্যা)
# _     (Underscore)

# তাই:

# abc_123

# Python এভাবে দেখে:

# a  ✔ Word Character
# b  ✔ Word Character
# c  ✔ Word Character
# _  ✔ Word Character
# 1  ✔ Word Character
# 2  ✔ Word Character
# 3  ✔ Word Character

# তাই সবগুলো Match হয়েছে।

# Output:
# ['a', 'b', 'c', '_', '1', '2', '3']

# --------------------------------------------------

# অনেক Beginner মনে করে:

# \w
# = শুধু Word (abc)

# কিন্তু আসলে:

# \w
# = Letter + Number + Underscore

# --------------------------------------------------

# Example:

print(re.findall(r"\w", "A_B-12"))

# Python দেখে:

# A ✔
# _ ✔
# B ✔
# - ✖
# 1 ✔
# 2 ✔

# Output:
# ['A', '_', 'B', '1', '2']

# --------------------------------------------------

# তাহলে Dash (-) কেন আসেনি?

# কারণ:

# \w এর ভিতরে
# Dash (-) নেই।

# \w শুধুমাত্র:
#
# a-z
# A-Z
# 0-9
# _

# এগুলোকে Match করে।

# Beginner Shortcut:

# \w
# = Word Character

# Word Character মানে:
#
# Letter ✔
# Number ✔
# Underscore (_) ✔

# Space ✖
# Dash (-) ✖
# @ ✖
# # ✖

# তাই:

# re.findall(r"\w", "abc_123")

# Output:
# ['a', 'b', 'c', '_', '1', '2', '3']
#
# কারণ String-এর সব Character-ই
# Word Character ছিল। 

# ==========================================================
# \W (Non Word Character)
# ==========================================================

print(re.findall(r"\W", "@#$"))

# Output:
# ['@', '#', '$']
# ==========================================================
# Python Regex - \W (Non-Word Character)
# ==========================================================

# \W
#
# = Non-Word Character
#
# অর্থাৎ:
#
# \w এর উল্টো।

# ==========================================================
# \w কী Match করে?
# ==========================================================

# a-z
# A-Z
# 0-9
# _

# ==========================================================
# তাহলে \W কী Match করে?
# ==========================================================

# Space
# @
# #
# $
# %
# &
# *
# -
# +
# !
# ?
# ,
# .
#
# অর্থাৎ Letter, Number এবং Underscore ছাড়া
# বাকি সব Character।

# ==========================================================
# Example 1
# ==========================================================

import re

print(re.findall(r"\W", "abc_123@#"))

# Output:
# ['@', '#']

# Explanation:

# a ✔ Word Character
# b ✔ Word Character
# c ✔ Word Character
# _ ✔ Word Character
# 1 ✔ Word Character
# 2 ✔ Word Character
# 3 ✔ Word Character
#
# @ ✖ Word Character না
# # ✖ Word Character না

# তাই Output:
# ['@', '#']

# ==========================================================
# Example 2
# ==========================================================

print(re.findall(r"\W", "Hello World!"))

# Output:
# [' ', '!']

# Explanation:

# H,e,l,l,o ✔
# Space ✖
# W,o,r,l,d ✔
# ! ✖

# তাই Output:
# [' ', '!']

# ==========================================================
# Example 3
# ==========================================================

print(re.findall(r"\W", "A_B-C"))

# Output:
# ['-']

# Explanation:

# A ✔
# _ ✔
# B ✔
# - ✖
# C ✔

# তাই শুধু '-' Match হয়েছে।

# ==========================================================
# \w vs \W
# ==========================================================

# \w
#
# Letter ✔
# Number ✔
# Underscore ✔

# ----------------------------------------------------------

# \W
#
# Space ✔
# @ ✔
# # ✔
# $ ✔
# - ✔
# ! ✔

# ==========================================================
# Beginner Shortcut
# ==========================================================

# \w
# = Word Character
#
# a-z
# A-Z
# 0-9
# _

# \W
# = Non-Word Character
#
# Space
# @
# #
# $
# %
# -
# !
# ?

# ==========================================================
# One Line Definition
# ==========================================================

# \W এমন সব Character Match করে,
# যেগুলো Letter, Number বা Underscore (_)
# নয়।
# ========================================================== 

# ==========================================================
# \s (White Space)
# ==========================================================

print(re.findall(r"\s", "Hello World"))

# Output:
# [' ']

# Space, Tab, New Line
# ==========================================================
# Python Regex - \s (Whitespace Character)
# ==========================================================

# \s
#
# = Whitespace Character
#
# অর্থাৎ:
#
# ফাঁকা জায়গা (Space)
# Tab (\t)
# New Line (\n)
#
# এগুলোকে Match করে।

# Example:

import re

print(re.findall(r"\s", "Hello World"))

# Output:
# [' ']

# Explanation:
#
# Hello World
#      ^
#
# Hello এবং World এর মাঝে 1টি Space আছে।
#
# \s শুধুমাত্র সেই Space-টিকে Match করেছে।

# ----------------------------------------------------------

print(re.findall(r"\s", "Hello   World"))

# Output:
# [' ', ' ', ' ']

# Explanation:
#
# এখানে 3টি Space আছে।
#
# তাই \s 3টি Space-ই Match করেছে।

# ----------------------------------------------------------

# গুরুত্বপূর্ণ:

# \s কখনো Letter Match করে না।
# \s কখনো Number Match করে না।
# \s কখনো Underscore Match করে না।

# \s শুধুমাত্র Whitespace Match করে।

# ==========================================================
# Beginner Shortcut
# ==========================================================

# \s
# = Whitespace (ফাঁকা জায়গা)

# Space      ✔
# Tab        ✔
# New Line   ✔

# a-z        ✖
# A-Z        ✖
# 0-9        ✖
# _          ✖

# ==========================================================
# One Line Definition
# ==========================================================

# \s এমন সব Character Match করে,
# যেগুলো ফাঁকা জায়গা (Whitespace),
# যেমন Space, Tab এবং New Line।
# ==========================================================

# ==========================================================
# Python Regex - \s এবং \S
# ==========================================================

# \s
#
# = Whitespace Character
#
# অর্থাৎ:
# Space, Tab, New Line খুঁজে।

import re

print(re.findall(r"\s", "Hello"))

# Output:
# []

# Explanation:
#
# "Hello" এর মধ্যে কোনো Space নেই।
#
# তাই \s কোনো Match পায়নি।
#
# [] মানে:
# কিছুই Match পাওয়া যায়নি।

# ----------------------------------------------------------

# \S
#
# = Non-Whitespace Character
#
# অর্থাৎ:
# Whitespace ছাড়া বাকি সব Character খুঁজে।

print(re.findall(r"\S", "Hello"))

# Output:
# ['H', 'e', 'l', 'l', 'o']

# Explanation:
#
# H ✔
# e ✔
# l ✔
# l ✔
# o ✔
#
# কারণ এগুলো কোনোটাই Whitespace না।

# ==========================================================
# Beginner Shortcut
# ==========================================================

# \s
# = Space, Tab, New Line খুঁজে

# \S
# = Space, Tab, New Line ছাড়া
#   বাকি সব Character খুঁজে

# ==========================================================
# One Line Definition
# ==========================================================

# \s = Whitespace Match করে।
# \S = Whitespace ছাড়া সব Match করে।
# ==========================================================
# ==========================================================
# \S (Non White Space)
# ==========================================================

print(re.findall(r"\S", "Hi A"))

# Output:
# ['H', 'i', 'A']

# ==========================================================
# \b (Word Boundary)
# ==========================================================
# Example:

import re

print(re.findall(r"\S", "Hi A"))

# Output:
# ['H', 'i', 'A']

# ==========================================================
# Explanation
# ==========================================================

# \S
#
# = Non-Whitespace Character
#
# অর্থাৎ:
#
# Space ছাড়া বাকি সব Character Match করবে।

# String:

# "Hi A"

# Python এভাবে দেখে:

# H ✔ Non-Whitespace
# i ✔ Non-Whitespace
#   ✖ Space (Whitespace)
# A ✔ Non-Whitespace

# তাই Python শুধু:

# H
# i
# A

# Match করে।

# Output:

# ['H', 'i', 'A']

# ==========================================================
# কেন Space Output এ আসেনি?
# ==========================================================

# কারণ:

# \S
#
# = Non-Whitespace

# আর Space হলো:

# Whitespace

# তাই Space Match হয়নি।

# ==========================================================
# Beginner Shortcut
# ==========================================================

# \S
#
# = Space বাদ দিয়ে
# বাকি সব Character Match করে।

# H ✔
# i ✔
# Space ✖
# A ✔

# তাই Output:

# ['H', 'i', 'A']

# ==========================================================
# One Line Definition
# ==========================================================

# \S এমন সব Character Match করে,
# যেগুলো Space, Tab বা New Line নয়।
# ==========================================================

# \b (Word Boundary)
# পুরো Word Match করে।
print(re.findall(r"\bcat\b", "cat category"))

# Output:
# ['cat']

# ==========================================================
# Python Regex - \b (Word Boundary) এবং \B (Non-Word Boundary)
# ==========================================================

# গুরুত্বপূর্ণ:
#
# \b এবং \B কোনো Character Match করে না।
#
# এগুলো Position Match করে।

# ==========================================================
# \b = Word Boundary
# ==========================================================

# \b
#
# = শব্দের শুরু বা শেষের সীমানা (Boundary) খুঁজে।

# Example:

import re

print(re.findall(r"\bcat\b", "cat bat cat"))

# Output:
# ['cat', 'cat']

# Explanation:
#
# এখানে cat আলাদা একটি শব্দ।
#
# তাই Match হয়েছে।

# ----------------------------------------------------------

print(re.findall(r"\bcat\b", "catfish cat"))

# Output:
# ['cat']

# Explanation:
#
# catfish এর ভিতরের cat Match হয়নি।
#
# কারণ catfish একটি বড় শব্দ।
#
# \bcat\b সম্পূর্ণ cat শব্দ চায়।

# ==========================================================
# \B = Non-Word Boundary
# ==========================================================

# \B
#
# = শব্দের ভিতরের Position খুঁজে,
# যেখানে কোনো Boundary নেই।

# Example:

print(re.findall(r"\Bcat", "scat category"))

# Output:
# ['cat', 'cat']

# Explanation:
#
# scat
#  ^
#
# cat এর আগে s আছে।
#
# তাই Boundary নেই।
#
# Match হয়েছে।

# ----------------------------------------------------------

# category
#
# cat এর পরে আরও Letter আছে।
#
# তাই এটাও Boundary না।
#
# Match হয়েছে।

# ==========================================================
# Python কীভাবে দেখে?
# ==========================================================

# cat

# |cat|

# এখানে | শুধু বোঝানোর জন্য।
#
# c এর আগে Boundary আছে।
# t এর পরে Boundary আছে।

# ----------------------------------------------------------

# catfish

# |catfish|

# cat এবং fish এর মাঝখানে
# Boundary নেই।
#
# কারণ দুই পাশেই Letter আছে।

# ==========================================================
# \b বনাম \B
# ==========================================================

# \b
#
# = পুরো শব্দ Match করে।

# Match:
# cat

# Match না:
# catfish
# scat

# ----------------------------------------------------------

# \B
#
# = বড় শব্দের ভিতরের অংশ Match করে।

# Match:
# scat
# category

# ==========================================================
# Beginner Shortcut
# ==========================================================

# \b
# = Word Boundary
#
# শব্দের শুরু বা শেষের সীমানা।

# \B
# = Non-Word Boundary
#
# শব্দের ভিতরের Position।

# ==========================================================
# One Line Definition
# ==========================================================

# \b = শব্দের শুরু বা শেষের Boundary Match করে।
#
# \B = শব্দের ভিতরের এমন Position Match করে,
# যেখানে কোনো Boundary নেই।
# ==========================================================

# ==========================================================
# \B (Non Word Boundary)
# ==========================================================

print(re.findall(r"\Bcat\B", "scatcatx"))

# Output:
# ['cat']
