import re
print(re.findall(r'(ab|cd)e', 'abeabacadbcbdcde'))  # ['ab', 'cd']
print(re.findall(r'(?:ab|cd)e', 'abeabacadbcbdcde'))  # ['abe', 'cde']
print(re.findall(r'(ab){2}', 'abab'))  # ['ab']
print(re.findall(r'(?:ab){2}', 'abab'))  # ['abab']