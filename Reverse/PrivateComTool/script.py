from Crypto.Cipher import DES

E = ['0', '2', '4', '6', '8']

if __name__ == '__main__':
	text = open('Message.Agency', 'rb').read()
	for i in E[1:]:
		for j in E:
			for k in E:
				for l in E:
					for m in E:
						for n in E:
							for o in E:
								for p in E:
									key = i + j + k + l + m + n + o + p
									plaintext = DES.new(key, DES.MODE_ECB).decrypt(text)
									if b"DCTF{" in plaintext:
										print(plaintext)
