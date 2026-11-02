#while loop
a = 0
while a < 5:
  print("yes a is less than 5", a)
  a = a + 1

#for loop
fruits = ["apple", "banana", "cherry"]
for n in fruits:
  print(n)
#for loop break way
for n in fruits:
    if n == "banana":
        break
    print(n)
    #output:apple