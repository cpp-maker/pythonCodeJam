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

def pass_gen(lenght):
    passwordd = ("".join(random.choice(string.printable.strip())for _ in range(int(lenght))))
    return passwordd

def encrypt(key, password):
    f = Fernet(key)
    encrypted = f.encrypt(password.encode())  # Encrypt the bytes
    return encrypted

def decrypt(key, line):
    f = Fernet(key)
    return f.decrypt(line)

def what_user_want(input_of_user, password_length=0, password_provided=0, line=0):
    secure_key = key_gen(password_provided)
    random_password = pass_gen(password_length)
    if input_of_user == "encrypt":
        encrypt(secure_key, random_password)
    elif input_of_user == "decrypt":
        decrypt(secure_key, line)
    else:
        exit()
