<<<<<<< HEAD:codeJamGui/pyjamGen.py
import random
import string 


def gen_code(length):
	return ("".join(random.choice(string.ascii_letters + string.digits) for _ in range(length)))


print(gen_code(5))
=======
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

import random
import string 


def gen_code(length):
	return ("".join(random.choice(string.ascii_letters + string.digits) for _ in range(length)))


print(gen_code(5))
>>>>>>> 970b1cbdd27d0feae658f1d939d95fffdb10b512:pyjamGen.py
