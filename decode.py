from string import printable
import random
import time

a = time.time()
digit = printable.strip()
#print(digit)
lenght = input("Password Lenght ") #length
if lenght == '':
	print("no password is of 0 words")
	exit()
elif lenght.replace(' ','').isalpha() == True:
	print("type a number")
	exit()
else:
	passw  = []
	for i in range(int(lenght)):
		passw.append(random.choice(digit))
word = ''.join(passw)
print(word)
