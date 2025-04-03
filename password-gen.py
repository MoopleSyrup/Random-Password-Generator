import random
import string

length = int(input("Enter Length: "))

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

""" Version 1 """
""" password = ""
for i in range(length):
    password += random.choice(chars) """

""" Version 2 """
password = ''.join([random.choice(chars) for i in range(length)])

print("Your random passowrd is: ", password)