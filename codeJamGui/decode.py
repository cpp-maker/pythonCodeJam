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

import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import string
import random

password_length = input()#length
def key_gen():
	password_provided = input('enter password:')
	password = password_provided.encode()  # Convert to type bytes
	salt = b'H\x8a\x04\x1b\xbdV\xb9\xfd\xab\x02\xfe!\xeb\x9b$\xce'
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=35,
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
		print("something went wrong!!!!")

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

def what_user_want(input_of_user):
	if input_of_user == "encrypt":

	