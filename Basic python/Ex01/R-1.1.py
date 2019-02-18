'''
R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.

-----------------------------------------
@author: lawrence  ludingkun@outlook.com
@date: 2019-02-18
-----------------------------------------
'''

def is_multiple():
	n = input("Enter the first number N:")
	m = input("Enter the first number M:")
	n = int(n)
	m = int(m)
	if n%m == 0:
		print("N is a multiple of M, and return: True")
		return True
	print("N is NOT a multiple of M, and return: False")
	return False
	

if __name__ == "__main__":
	is_multiple()

