#import regex module
import re
#Define regex expression for phone number
pattern = re.compile(r'(((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10})')
#Search a first string with regex
res = pattern.search('My number +79998887788')
print(res.group())
#Search all mathes with regex
res2 = pattern.findall('My number +79998887788 and +79995553535')
print(res2)
