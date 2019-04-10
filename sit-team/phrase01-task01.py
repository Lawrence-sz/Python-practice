
#------solution-01------------------

"""Define one string and one sub-string, and delete all matched sub-strings from the string in Python.（consider the recursive scenario and use function to do this job）
e.g. string = ‘'abcababcbaaabbbb'’,  sub-string = ‘ab’.  Result = ‘ccbb’
"""

import string


def delete_matched_sub_string():
    """ Delete substring from original string, and return results."""
    _originalString = input("The original string:")
    _subString = input("The sub-string:")

    while _subString in _originalString:
        # Delete the _substring from _oringinalString, and restore _originalString
        _originalString = _originalString.replace(_subString, '')

    return _originalString


if __name__ == "__main__":
    resultString = delete_matched_sub_string()
    print(resultString)

#------------------------------------
	
	
#------solution-02------------------



#------------------------------------
