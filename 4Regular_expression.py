📚 Python Search & Replace (Beginner Friendly Complete Notes)

Python-এ Search & Replace বলতে কোনো Text-এর মধ্যে নির্দিষ্ট কিছু খুঁজে বের করা (Search) এবং প্রয়োজন হলে সেটিকে অন্য কিছু দিয়ে পরিবর্তন করা (Replace) বোঝায়। এটি Data Validation, Text Processing, Data Cleaning, Web Scraping, Log Analysis, Email Extraction, Phone Number Extraction এবং Sensitive Data Masking-এর মতো কাজে ব্যাপকভাবে ব্যবহৃত হয়।

━━━━━━━━━━━━━━━━━━━━
1️⃣ re.match()
━━━━━━━━━━━━━━━━━━━━

re.match() স্ট্রিংয়ের শুরুতে কোনো Pattern আছে কিনা চেক করে।

✅ কখন ব্যবহার হয়?
- Employee ID Check
- Product Code Check
- Username Prefix Check

✅ কেন ব্যবহার হয়?
কারণ অনেক ক্ষেত্রে কোনো Text নির্দিষ্ট Prefix দিয়ে শুরু হওয়া বাধ্যতামূলক থাকে।

উদাহরণ:
"EMP12345" যদি "EMP" দিয়ে শুরু হয়, তাহলে Match হবে।

মনে রাখবে:
re.match() শুধুমাত্র String-এর শুরু পরীক্ষা করে।

━━━━━━━━━━━━━━━━━━━━
2️⃣ re.fullmatch()
━━━━━━━━━━━━━━━━━━━━

re.fullmatch() পুরো String Pattern-এর সাথে মিলে কিনা পরীক্ষা করে।

✅ কখন ব্যবহার হয়?
- OTP Validation
- PIN Validation
- Age Validation
- User Input Validation

✅ কেন ব্যবহার হয়?
কারণ এখানে পুরো Input সঠিক কিনা নিশ্চিত করতে হয়।

উদাহরণ:
"12345" যদি শুধুমাত্র সংখ্যা হয়, তাহলে Match হবে।
"12345abc" হলে Match হবে না।

━━━━━━━━━━━━━━━━━━━━
3️⃣ re.findall()
━━━━━━━━━━━━━━━━━━━━

re.findall() একটি Pattern-এর সব Match খুঁজে List আকারে Return করে।

✅ কখন ব্যবহার হয়?
- Email সংগ্রহ
- Phone Number সংগ্রহ
- Keyword Count
- Data Extraction

✅ কেন ব্যবহার হয়?
কারণ অনেক সময় একটি Text-এর ভিতরে একাধিক Match থাকে এবং আমাদের সবগুলো দরকার হয়।

উদাহরণ:
"Python Java Python C++ Python"

এখানে findall() ব্যবহার করলে:
["Python", "Python", "Python"]

পাওয়া যাবে।

━━━━━━━━━━━━━━━━━━━━
4️⃣ re.finditer()
━━━━━━━━━━━━━━━━━━━━

re.finditer() সব Match খুঁজে দেয় এবং প্রতিটি Match কোথায় পাওয়া গেছে সেটাও জানায়।

✅ কখন ব্যবহার হয়?
- Text Editor
- Search Highlighting
- Document Analysis
- Keyword Tracking

✅ কেন ব্যবহার হয়?
কারণ শুধু Match পেলেই হয় না, অনেক সময় Match কোথায় আছে সেটাও জানতে হয়।

উদাহরণ:
"Python Java Python"

প্রথম Python → Position (0,6)
দ্বিতীয় Python → Position (12,18)

━━━━━━━━━━━━━━━━━━━━
5️⃣ Match Object
(group(), start(), end(), span())
━━━━━━━━━━━━━━━━━━━━

Search করার পর Match পাওয়া গেলে Python একটি Match Object Return করে।

✅ group()
Match হওয়া Text Return করে।

✅ start()
Match কোথা থেকে শুরু হয়েছে জানায়।

✅ end()
Match কোথায় শেষ হয়েছে জানায়।

✅ span()
Start এবং End Position একসাথে Return করে।

✅ কখন ব্যবহার হয়?
- Data Extraction
- Search Highlighting
- Text Processing
- Pattern Analysis

━━━━━━━━━━━━━━━━━━━━
6️⃣ str.replace()
━━━━━━━━━━━━━━━━━━━━

এটি Python-এর সাধারণ Replace Function।

✅ কখন ব্যবহার হয়?
- Word Change
- Typo Fix
- Data Cleaning
- Simple Text Editing

✅ কেন ব্যবহার হয়?
যখন Regex-এর প্রয়োজন নেই এবং সরাসরি Text পরিবর্তন করতে হয়।

উদাহরণ:
Python → Java

Replace করলে Text পরিবর্তিত হয়ে যাবে।

━━━━━━━━━━━━━━━━━━━━
7️⃣ re.sub()
━━━━━━━━━━━━━━━━━━━━

Regex ব্যবহার করে Search এবং Replace করার জন্য ব্যবহৃত হয়।

✅ কখন ব্যবহার হয়?
- Email Hide
- Phone Number Hide
- Sensitive Data Masking
- Pattern Based Replace

✅ কেন ব্যবহার হয়?
কারণ অনেক সময় নির্দিষ্ট Word নয়, Pattern অনুযায়ী Replace করতে হয়।

উদাহরণ:
সব সংখ্যা "XX" দিয়ে Replace করা।

━━━━━━━━━━━━━━━━━━━━
8️⃣ re.subn()
━━━━━━━━━━━━━━━━━━━━

re.sub() এর মতো Replace করে, তবে অতিরিক্তভাবে কতবার Replace হয়েছে সেটাও জানায়।

✅ কখন ব্যবহার হয়?
- Replace Count Tracking
- Log Analysis
- Data Cleaning Report

✅ কেন ব্যবহার হয়?
কারণ Replace-এর সংখ্যা জানা গুরুত্বপূর্ণ হতে পারে।

উদাহরণ:
৩টি Word Replace হলে Result-এর সাথে 3-ও Return করবে।

━━━━━━━━━━━━━━━━━━━━
9️⃣ Capturing Groups
━━━━━━━━━━━━━━━━━━━━

Regex-এর কোনো অংশকে আলাদা করে ধরে রাখার জন্য Capturing Group ব্যবহার করা হয়।

✅ কখন ব্যবহার হয়?
- Name Extraction
- Email Username Extraction
- Date Extraction
- Custom Data Extraction

✅ কেন ব্যবহার হয়?
কারণ অনেক সময় পুরো Match নয়, Match-এর নির্দিষ্ট অংশ দরকার হয়।

উদাহরণ:
"Name: Hasan"

এখান থেকে শুধু "Hasan" আলাদা করে বের করা।

━━━━━━━━━━━━━━━━━━━━
🔟 Real-World Search & Replace Projects
━━━━━━━━━━━━━━━━━━━━

বাস্তব জীবনে Search & Replace ব্যবহার করা হয়:

✅ Email খোঁজা
✅ Phone Number খোঁজা
✅ URL খোঁজা
✅ HTML Tag Remove করা
✅ Text Cleaning
✅ Data Validation
✅ Sensitive Data Hide করা
✅ Log File Analysis
✅ Web Scraping
✅ Data Extraction

━━━━━━━━━━━━━━━━━━━━
🎯 সংক্ষেপে
━━━━━━━━━━━━━━━━━━━━

Search Functions:
✔ re.match()
✔ re.fullmatch()
✔ re.findall()
✔ re.finditer()

Replace Functions:
✔ str.replace()
✔ re.sub()
✔ re.subn()

Match Information:
✔ group()
✔ start()
✔ end()
✔ span()

Advanced Extraction:
✔ Capturing Groups

এই ১০টি বিষয় ভালোভাবে শিখে প্র্যাকটিস করলে Python Search & Replace-এর প্রায় ৮০–৯০% ব্যবহারিক কাজ করতে পারবে।

📚 Python Search & Replace (Beginner Friendly Complete Notes)

Python-এ Search & Replace বলতে কোনো Text-এর মধ্যে নির্দিষ্ট কিছু খুঁজে বের করা (Search) এবং প্রয়োজন হলে সেটিকে অন্য কিছু দিয়ে পরিবর্তন করা (Replace) বোঝায়। এটি Data Validation, Text Processing, Data Cleaning, Web Scraping, Log Analysis, Email Extraction, Phone Number Extraction এবং Sensitive Data Masking-এর মতো কাজে ব্যাপকভাবে ব্যবহৃত হয়।

━━━━━━━━━━━━━━━━━━━━
1️⃣ re.match()
━━━━━━━━━━━━━━━━━━━━

re.match() স্ট্রিংয়ের শুরুতে কোনো Pattern আছে কিনা চেক করে।

✅ কখন ব্যবহার হয়?
- Employee ID Check
- Product Code Check
- Username Prefix Check

✅ কেন ব্যবহার হয়?
কারণ অনেক ক্ষেত্রে কোনো Text নির্দিষ্ট Prefix দিয়ে শুরু হওয়া বাধ্যতামূলক থাকে।

উদাহরণ:
"EMP12345" যদি "EMP" দিয়ে শুরু হয়, তাহলে Match হবে।

মনে রাখবে:
re.match() শুধুমাত্র String-এর শুরু পরীক্ষা করে।

━━━━━━━━━━━━━━━━━━━━
2️⃣ re.fullmatch()
━━━━━━━━━━━━━━━━━━━━

re.fullmatch() পুরো String Pattern-এর সাথে মিলে কিনা পরীক্ষা করে।

✅ কখন ব্যবহার হয়?
- OTP Validation
- PIN Validation
- Age Validation
- User Input Validation

✅ কেন ব্যবহার হয়?
কারণ এখানে পুরো Input সঠিক কিনা নিশ্চিত করতে হয়।

উদাহরণ:
"12345" যদি শুধুমাত্র সংখ্যা হয়, তাহলে Match হবে।
"12345abc" হলে Match হবে না।

━━━━━━━━━━━━━━━━━━━━
3️⃣ re.findall()
━━━━━━━━━━━━━━━━━━━━

re.findall() একটি Pattern-এর সব Match খুঁজে List আকারে Return করে।

✅ কখন ব্যবহার হয়?
- Email সংগ্রহ
- Phone Number সংগ্রহ
- Keyword Count
- Data Extraction

✅ কেন ব্যবহার হয়?
কারণ অনেক সময় একটি Text-এর ভিতরে একাধিক Match থাকে এবং আমাদের সবগুলো দরকার হয়।

উদাহরণ:
"Python Java Python C++ Python"

এখানে findall() ব্যবহার করলে:
["Python", "Python", "Python"]

পাওয়া যাবে।

━━━━━━━━━━━━━━━━━━━━
4️⃣ re.finditer()
━━━━━━━━━━━━━━━━━━━━

re.finditer() সব Match খুঁজে দেয় এবং প্রতিটি Match কোথায় পাওয়া গেছে সেটাও জানায়।

✅ কখন ব্যবহার হয়?
- Text Editor
- Search Highlighting
- Document Analysis
- Keyword Tracking

✅ কেন ব্যবহার হয়?
কারণ শুধু Match পেলেই হয় না, অনেক সময় Match কোথায় আছে সেটাও জানতে হয়।

উদাহরণ:
"Python Java Python"

প্রথম Python → Position (0,6)
দ্বিতীয় Python → Position (12,18)

━━━━━━━━━━━━━━━━━━━━
5️⃣ Match Object
(group(), start(), end(), span())
━━━━━━━━━━━━━━━━━━━━

Search করার পর Match পাওয়া গেলে Python একটি Match Object Return করে।

✅ group()
Match হওয়া Text Return করে।

✅ start()
Match কোথা থেকে শুরু হয়েছে জানায়।

✅ end()
Match কোথায় শেষ হয়েছে জানায়।

✅ span()
Start এবং End Position একসাথে Return করে।

✅ কখন ব্যবহার হয়?
- Data Extraction
- Search Highlighting
- Text Processing
- Pattern Analysis

━━━━━━━━━━━━━━━━━━━━
6️⃣ str.replace()
━━━━━━━━━━━━━━━━━━━━

এটি Python-এর সাধারণ Replace Function।

✅ কখন ব্যবহার হয়?
- Word Change
- Typo Fix
- Data Cleaning
- Simple Text Editing

✅ কেন ব্যবহার হয়?
যখন Regex-এর প্রয়োজন নেই এবং সরাসরি Text পরিবর্তন করতে হয়।

উদাহরণ:
Python → Java

Replace করলে Text পরিবর্তিত হয়ে যাবে।

━━━━━━━━━━━━━━━━━━━━
7️⃣ re.sub()
━━━━━━━━━━━━━━━━━━━━

Regex ব্যবহার করে Search এবং Replace করার জন্য ব্যবহৃত হয়।

✅ কখন ব্যবহার হয়?
- Email Hide
- Phone Number Hide
- Sensitive Data Masking
- Pattern Based Replace

✅ কেন ব্যবহার হয়?
কারণ অনেক সময় নির্দিষ্ট Word নয়, Pattern অনুযায়ী Replace করতে হয়।

উদাহরণ:
সব সংখ্যা "XX" দিয়ে Replace করা।

━━━━━━━━━━━━━━━━━━━━
8️⃣ re.subn()
━━━━━━━━━━━━━━━━━━━━

re.sub() এর মতো Replace করে, তবে অতিরিক্তভাবে কতবার Replace হয়েছে সেটাও জানায়।

✅ কখন ব্যবহার হয়?
- Replace Count Tracking
- Log Analysis
- Data Cleaning Report

✅ কেন ব্যবহার হয়?
কারণ Replace-এর সংখ্যা জানা গুরুত্বপূর্ণ হতে পারে।

উদাহরণ:
৩টি Word Replace হলে Result-এর সাথে 3-ও Return করবে।

━━━━━━━━━━━━━━━━━━━━
9️⃣ Capturing Groups
━━━━━━━━━━━━━━━━━━━━

Regex-এর কোনো অংশকে আলাদা করে ধরে রাখার জন্য Capturing Group ব্যবহার করা হয়।

✅ কখন ব্যবহার হয়?
- Name Extraction
- Email Username Extraction
- Date Extraction
- Custom Data Extraction

✅ কেন ব্যবহার হয়?
কারণ অনেক সময় পুরো Match নয়, Match-এর নির্দিষ্ট অংশ দরকার হয়।

উদাহরণ:
"Name: Hasan"

এখান থেকে শুধু "Hasan" আলাদা করে বের করা।

━━━━━━━━━━━━━━━━━━━━
🔟 Real-World Search & Replace Projects
━━━━━━━━━━━━━━━━━━━━

বাস্তব জীবনে Search & Replace ব্যবহার করা হয়:

✅ Email খোঁজা
✅ Phone Number খোঁজা
✅ URL খোঁজা
✅ HTML Tag Remove করা
✅ Text Cleaning
✅ Data Validation
✅ Sensitive Data Hide করা
✅ Log File Analysis
✅ Web Scraping
✅ Data Extraction

━━━━━━━━━━━━━━━━━━━━
🎯 সংক্ষেপে
━━━━━━━━━━━━━━━━━━━━

Search Functions:
✔ re.match()
✔ re.fullmatch()
✔ re.findall()
✔ re.finditer()

Replace Functions:
✔ str.replace()
✔ re.sub()
✔ re.subn()

Match Information:
✔ group()
✔ start()
✔ end()
✔ span()

Advanced Extraction:
✔ Capturing Groups

এই ১০টি বিষয় ভালোভাবে শিখে প্র্যাকটিস করলে Python Search & Replace-এর প্রায় ৮০–৯০% ব্যবহারিক কাজ করতে পারবে।

  class counter:
    def __init__(self):
      self.value = 1

      def count_up(self):
        self.value = value + 1

        def count_up(self):
          self.value = value - 1

  count1 = counter()
  count2 = counter()

  count1.count_up()
  count2.count_up()

  print(count1, count2)
  print(count1 + count2)