import numpy as np
import hashlib

def hash(inp):
	return hashlib.sha256(str(inp) + "DCTF2018_BUCHAREST").hexdigest()

def square(x): # x ** 2
	try:
	    sum_so_far = 0
	    for _ in range(x):
	        sum_so_far += x
		return sum_so_far
	except Exception(e):
		print e
	finally:
		return sum_so_far

def get_key(x): # 1337 * (x-1)!
	nr = 1337
	try:
		for value in range(1,x):
			nr = nr * value
		return nr
	except Exception(e):
		print e
	finally:
		return nr

PRIV = 1198041294.0
target = 'fe79a0ee1fc2a52fc9af8592d8c0570a73d9542ec1d4ec2ae6e9d03991cb0459'

for i in range(9999):
	if hash(i * PRIV) == target:
		print(i)
	