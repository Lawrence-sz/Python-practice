""" R-1.1
#Write a short Python function, is multiple(n, m), that takes two integer
#values and returns True if n is a multiple of m, that is, n = mi for some
#integer i, and False otherwise.
"""

import string


def is_integer(var1):
    """ Check if the given input is integer."""
    tmp = list(var1)

    # Is it a negative one?
    if tmp[0] == '-':
        tmp = tmp[1:]

    # Does it start with 0, or contain non-digits?
    if (tmp[0] == '0' and len(list(var1)) != 1) or not set(tmp) <= set(string.digits):
        print(f"\t##--'{var1}'-- is not an integer number!")
        return False

    return True


def is_not_zero_divisor(var1):
	""" Check if the given input is zero."""
	tmp = list(var1) # Is it neended?
	if tmp == ['0']:
		print("\t##Zero cannot be a divisor!")
		return False
	return True




def is_multiple():
    """ Check if the given first input is a multiple of the second given input."""
    print("\t*This function is used to count if N is a multiple of M! \n \t* Please enter both N and M.")
    n = input("\t##Enter the first integer number N:")
    # Give the user another two tries

    for i in range(2):
        if not is_integer(n):
            n = input("\t##Enter again! N:")
            if i == 1 and not is_integer(n):
                print("\t##You have tried for 3 times, we must quit this process!")
                return False
        continue

    m = input("\t##Enter the second integer number M:")
    # Give the user another two tries
    for i in range(2):
        if (not is_integer(m) or not is_not_zero_divisor(m)):
            m = input("\t##Enter again! M:")
            if i == 1 and (not is_integer(m) or  not is_not_zero_divisor(m)):
                print("\t##You have tried for 3 times, we must quit this process!")
                return False
        continue

    n = int(n)
    m = int(m)

    if n % m == 0:
        print(f"\t##--N: {n}-- is a multiple of --M: {m}--, and return: True")
        return True
    print(f"\t##--N: {n}-- is NOT a multiple of --M: {m}--, and return: False")
    return False


if __name__ == "__main__":
	
	is_multiple()
