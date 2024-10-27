import random
  
print("Hello and welcome to the password generator application: ")

print("Do you want us to create a password for you: ")

user_choice=input("YES/NO: ").upper()
print("User choice is: ",user_choice)
if user_choice=="YES":
    characters="abcdefghijklmnopqrstuvwxyz1234567890!@#%$&~_*()"
    password= ""
    for i in range(11):
        password+=random.choice(characters)
    print("Your password is: ",password)
else:
    print("No password is generated")

