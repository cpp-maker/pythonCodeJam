#Copyright (C) 2020 author name here
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.



#########  Version - 0.1 #########
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import string
import random

password_length = input()#length
password_provided = input('enter password:')
def key_gen(password_provided):
	password = password_provided.encode()  # Convert to type bytes
	salt = b'\xa5\x81\xadC\x0eF\x17gaxj\x87fF\xeb\xc9\x03~\x9f\xf9|\xc5\xf4\x80\xc6\xd6\xbe\xb7\xd2\x98\xfe\x91'
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=32,
		salt=salt,
		iterations=100000,
		backend=default_backend()
	)
	key = base64.urlsafe_b64encode(kdf.derive(password))  # this is the encrypted  password
	return key

def pass_gen(lenght):
	try:
		passwordd = ("".join(random.choice(string.printable.strip())for _ in range(int(lenght))))
		return passwordd
	except Exception:
		print("something went wrong!!!! try entering the length  like 10, 11 etc.")

def encrypt(key, password):
	f = Fernet(key)
	encrypted = f.encrypt(password.encode())  # Encrypt the bytes
	print(encrypted)
	print('done')

def decrypt(key, line):
	try:
		file = open("""hey pro change this""", 'rb')
		f = Fernet(key)
		lines = file.readlines()# it'll store lines in list
		decrypted = f.decrypt(lines[line])
		print(decrypted)
	except Exception:
		print("wrong password")

def what_user_want(input_of_user, password_length=0, password_provided=0, line=0):
	secure_key = key_gen(password_provided)
	random_password = pass_gen(password_length)
	if input_of_user == "encrypt":
		encrypt(secure_key, random_password)
	elif input_of_user == "decrypt":
		decrypt(secure_key, line)
	else:
		exit()