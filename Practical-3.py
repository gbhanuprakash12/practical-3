fh = open("prac 3.txt", 'w')
import random
length=12
i=1
character_set="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstwxyz0123456789!@#$%^&*"
password=""
while i<=length:
    password =  password + random.choice(character_set)
    i=i+1
fh.write(password)
fh.close()
