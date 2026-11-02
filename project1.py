#pdf merger project 1
# from PyPDF2 import PdfMerger

# AllPDF = ["1.pdf", "2.pdf"]

# OurMerger = PdfMerger()

# for newPDF in AllPDF:
#   OurMerger.append(newPDF)

# OurMerger.write("hablu.pdf")
# OurMerger.close()

#another project 2 Mad lip 
# username = input("what is your name:")
# motherName = input("what is your mother name:")
# fatherName = input("what is your father name:")
# study = input("which class do you read in:")
# relationship = input("tell about your relationship:")

# print(f"My friend name is {username}, My friend mother name is {motherName}, My friend father name is {fatherName}, My friend study in class {study}, My friend relationship is {relationship}")

#another project 3 number guess game
# import random
# RandomNumber = random.randrange(1,200)
# print(RandomNumber)
# userInput = int(input("Guess the number:"))

# if userInput > RandomNumber :
#   print(RandomNumber)
#   print("the number is too high")

# elif RandomNumber > userInput :
#   print(RandomNumber)
#   print("the number is too low")

# else:
#     print(RandomNumber)
#     print("yes, you matched the number")

#project 4 game
#answer = input("do you want to play this game [Yes/No]:")

# if answer == "Yes":
#   print("welcome to the game!")
#   answer = input("do you want to jungle or cave? [jungle/cave]:")
#   if answer == "jungle":
#     print("you see the hungry tiger. Tiger will eat you. game close")
#   elif answer == "cave":
#     print("you seen the bear in front of cave")
#     answer = input("do you want to fight with the bear or run away! [fight/run]:")
#     if answer == "fight":
#       print("bear is too much strong! you loss the game!")
#     else:
#       print("wow! still you are alive!")  

# else:
#   print("The game closed")

#project 5 ludugame
# import random
# DiceRolling = True
# while DiceRolling:
#   print(random.randint(1,6))
#   PlayAgain = input("Do you want to play again [y/n]:")
#   if PlayAgain == "y":
#      continue
#   else:
#      print("game over")
#      break

#project 6
# word = "Hablu"
# chances = 5
# GuessAdd = []
# done = False

# while not done:
#   for letter in word:
#     if letter.lower() in GuessAdd:
#       print(letter, end =" ")
#     else:
#       print("_", end = "")  
#   MyGuess = input(f"Your changes Is{chances}, Guess the Letter:")  
#   GuessAdd.append(MyGuess.lower())  
#   if MyGuess.lower() not in word.lower():
#     chances = chances - 1
#     if chances == 0:
#       break

#   done = True
#   for letter in word:
#     if letter.lower() not in GuessAdd:
#       done = False

# if done:
#   print(f"yes, you have won the game, the word is {word}")
# else:
#   print("you loss the game")

#project 7
# Contact = {}

# def ShowFunction():
#   print(Contact.items())
#   print("Name \t Contact")
#   for key in Contact:
#     print("{} \t {}".format(key,Contact.get(key)))
# while True:
#   Choice = int (input("1. Add New Contact \n"
#                  "2. Search the Contact \n"
#                  "3. Display the Contact \n"
#                  "4. Edit the Contact \n"
#                  "5. Delete the Contact \n"
#                  "6. Exit \n"
#                  "Please write Number between 1-6: "))
  
#   if Choice == 1:
#     name = input("Add your Contact name: ")
#     phone = input("Add your phone number:  ")
#     Contact[name] = phone

#   elif Choice == 2:
#     ContactName = input("Search the Contact: ")
#     if ContactName in Contact:
#       print(ContactName, "Contact number is", Contact[ContactName])
#     else:
#       print("not Found the Contact")

#   elif Choice == 3:
#     if not Contact:
#        print("Contact book is empty")
#     else:
#         ShowFunction()


#   elif Choice == 4:
#     EditContact = input("Edit your Contact: ")
#     if EditContact in Contact:
#       phone = input("Change your Number: ")
#       Contact[EditContact] = phone
#       print("Contact Update Successfully ")
#       ShowFunction()
#     else:
#       print("Name is Not Found")

#   elif Choice == 5:
#     Del_Contact = input("Which Contact Do you want delete?: ")
#     if Del_Contact in Contact:
#       DeleteConfirm = input("Do you want to delete this Contact y/n")
#       if DeleteConfirm == "y" or DeleteConfirm == "Y":
#             Contact.pop(Del_Contact)
#       ShowFunction()
#     else:
#       print("The name is not found in the Contact")

#   else:
#     break

#project 8 notification
from plyer import notification
import time

notification.notify(
    title="Learning Time",
    message="Hello Mahamud! It's time to learn something New",
    app_name="Python Reminder",
    timeout=5)
time.sleep(5)

notification.notify(
    title="Learning Time",
    message="Hello Mahamud! It's time to learn something New",
    app_name="Python Reminder",
    timeout=5)
time.sleep(5)

notification.notify(
    title="Learning Time",
    message="Hello Mahamud! It's time to learn something New",
    app_name="Python Reminder",
    timeout=5)
time.sleep(5)