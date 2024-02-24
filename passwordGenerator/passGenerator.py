import time
import random, string
password = []

print("Welcome to the password generator!")
time.sleep(1)
passLenght = int(input("Password Lenght(In Numbers): "))
time.sleep(1)
print("Loading...")
time.sleep(3)
passCharacters = string.ascii_letters + string.digits + string.punctuation

for x in range(passLenght):
    password.append(random.choice(passCharacters))

print("Password: " + ''.join(password))