import hashlib

salt = b'DH'
target = 'd92ef03b828d111152ae4a612cc35439'

string = '2/10,6/29,11/23,8/14,3/14,12/11,11/10,9/7,5/1,7/29,9/11,2/15,13/17,5/14,9/19,10/13,2/12,1/17,2/10,10/13,9/5,4/11,12/7,1/24,8/24,8/2,1/20,10/24,12/6,13/12,07/11,12/25,10/24,8/4,9/10,4/21,5/16,9/3,1/26,13/22,12/28,6/7,13/2,11/27,7/10,6/20,5/6,8/5,3/9,13/7,8/19,5/25,11/20,12/28,1/2,10/6,2/27,1/11,9/13,6/15,1/28,4/14,4/6,8/10,13/6,8/28,10/29,6/28,8/12,2/3,10/5,2/2,7/27,13/7,7/10,8/26,1/26,2/24,9/28,7/4,6/23,13/5,1/24,5/22,5/1,3/1,4/10,3/9,11/1,4/11,1/1,5/9'

def hash(x):
	return hashlib.md5(salt + bytes(x, 'utf-8')).hexdigest()

def getC(x, y="279146358279"):
	c = sum([int(i) * int(j) for i, j in zip(x, y)]) % 11
	if c == 10: return "1"
	else: return str(c)

for S in range(1, 9):
	S = str(S)
	for AA in range(100):
		AA = str(AA).zfill(2)
		for LLZZ in string.split(','):
			LLZZ = LLZZ.replace('/', '').zfill(4)
			for JJ in range(1, 53):
				JJ = str(JJ).zfill(2)
				for NNN in range(1, 1000):
					NNN = str(NNN).zfill(3)
					C = getC(S+AA+LLZZ+JJ+NNN)
					if hash(S+AA+LLZZ+JJ+NNN+C) == target:
						print(S+AA+LLZZ+JJ+NNN+C)