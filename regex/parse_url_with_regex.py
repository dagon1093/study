import re

#re.VERBOSE | re.I this is compilation flags. VERBOSE ignore tabs or \n, IGNORCASE ignore case of string
url_regex = re.compile(r'(https?)://(?P<first>www\.[A-Za-z1-9-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9#$%^&*@:=/+~?]*)',re.VERBOSE | re.I)

match = url_regex.search('dfdgfgfgfgf https://www.udemy.com/course/the-modern-python3-bootcamp/learn/lecture/9328506#overview gfgfgfgfg')

print(match.group('first'))
print(match.groups()) # for all match groups in parenthesses