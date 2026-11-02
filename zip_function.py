#python zip function
#The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it. This function is used to map the similar index of multiple containers so that they can be used just using a single entity.
#পাইথন জিপ ফাংশন অনেকটা জয়েন লিস্ট এর মতই তবে আউটপুটের দিক দিয়ে এবং প্রিন্ট করার দিক দিয়ে অনেকটাই ভিন্ন তারা আছে নিচে এক্সাম্পল
#Example 1
list1 = ["Mahamud,", "Rafiq", "Hasan"]
list2 = ["programmer", "engineer", "doctor"]
zipped = zip(list1, list2)
print(list(zipped))
#another print way
#print(list(zip(list1, list2)))
#Output: [('Mahamud,', 'programmer'), ('Rafiq', 'engineer'), ('Hasan', 'doctor')]