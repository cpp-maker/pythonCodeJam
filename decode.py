import string
import random

<<<<<<< HEAD

pass_length  = input()#length of password
def pass_gen(lenght):
	if lenght == '':# to check if password have any digit
		print("no password is of 0 words")
		exit()
	elif lenght.replace(' ','').isalpha() == True:# to check if it is not a 
		print("type a number")
		exit()
	else:
		passwordd = ("".join(random.choice(string.printable.strip())for _ in range(int(lenght))))
		return passwordd
print(pass_gen(pass_length))
=======
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
>>>>>>> 49d438af01ea3003f02516fd99cffff35ab4aa4a
