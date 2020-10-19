import math
import random
def is_prime(number):
	if number > 1:
		if number == 2:
			return True
		if number % 2 == 0:
			return False
		for current in range(3, int(math.sqrt(number) + 1), 2):
			if number % current == 0: 
				return False
		return True
	return False

def gcd(a, b):
	if b > a:
		if b % a == 0:
			return a
		else:
			return gcd(b % a, a)
	else:
		if a % b == 0:
			return b
		else:
			return gcd(b, a % b)

def find_coprime(n):
	for i in range(1,n):
		if(gcd(i,n)==1):
			return(i)

def multiplicative_inverse(e, phi):
	return extended_euclid(e, phi)[1] % phi

def extended_euclid(a, b):
	if b == 0:
		return a, 1, 0
	else: 
		d2, x2, y2 = extended_euclid(b, a % b)
		d, x, y = d2, y2, x2 - (a // b) * y2
		return d, x, y

def get_keys():
	p = int(input('Input p:\n'))
	q = int(input('Input q:\n'))

	if (is_prime(p) and is_prime(q)):
		phi = (p-1)*(q-1)
		
		for i in range(2, phi):
			if gcd(phi,i) == 1:
				e = i
				break
			 
		print(e)
		d = multiplicative_inverse(e, phi)
		print(d)
		return(e, d, p*q)
	else:
		print('Numbers are not prime')

def encodeMessage(msg):
	encodedMsg = 0

	for char in msg:
		encodedMsg = encodedMsg << 8
		encodedMsg = encodedMsg ^ ord(char)
	return encodedMsg

def main():
	msg = "West"
	encodedMsg = encodeMessage(msg)
	e,d,n = get_keys()
	encryptedMsg = pow(encodedMsg, e, n)
	decryptedMsg = pow(encryptedMsg, d, n)
	print("\nOriginal message string:\n\t", msg)
	print("\nInteger encoded message:\n\t", encodedMsg)
	print("\nEncrypted message( C(M) = M^e % n ):\n\t", encryptedMsg)
	print("\nDecrypted message( M(C) = C^d % n ):\n\t", decryptedMsg)
	if encodedMsg == decryptedMsg:
	    print("\nThe decrypted message and the original encoded message match.")

                
