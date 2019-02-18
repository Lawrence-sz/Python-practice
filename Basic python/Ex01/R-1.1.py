'''
R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
'''

import string

'''
is_integer used to check if the input is a integer

'''
def is_integer(var1):
	for i in list(var1):
		if i not in list(string.digits) + ['-']:
			print(f"--'{var1}'-- is not an integer number,")
			
			# if i == '-' and list(var1).index('-') != 0:
				# print(f"--'{var1}'-- is not an integer number,")
			
			return False
		return True
		
	

def is_multiple():

	n = input("Enter the first integer number N:")
	#give the user another two tries
	for i in range(2):
		if not is_integer(n):
			n = input("Enter again! N:")
		continue
		
	if not is_integer(n):
		print("You have tried for 3 times, we must quit this process!")
		return False
	
	m = input("Enter the second integer number M:")
	#give the user another two tries
	for i in range(2):
		if not is_integer(m):
			m = input("Enter again! M:")
		elif list(m) == ['0']:
			print("M should not be zero!")
			m = input("Enter again! M:")
		
		continue
		
	if not is_integer(m):
		print("You have tried for 3 times, we must quit this process!")
		return False	
	
	
	n = int(n)
	m = int(m)
	
	if n%m == 0:
		print("N is a multiple of M, and return: True")
		return True
	print("N is NOT a multiple of M, and return: False")
	return False
	

if __name__ == "__main__":
	is_multiple()

