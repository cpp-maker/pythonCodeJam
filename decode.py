import string
import random


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