import random
import string 


def gen_code(length):
	return ("".join(random.choice(string.ascii_letters + string.digits) for _ in range(length)))


print(gen_code(5))