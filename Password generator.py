import random
import string

print("PASSWORD GENERATOR")
print("------------------")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password = password + random.choice(characters)

print("Your password is:", password)
