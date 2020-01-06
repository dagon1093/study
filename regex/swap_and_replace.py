import re

text = 'Mr. Jones said, Ms. Jenifer was muredered by Mrs. Joana'
pattern = re.compile(r'(Mr\.|Ms\.|Mrs\.) ([a-z])[a-z]+',re.I)
result = pattern.sub("\g<1> \g<2>", text) # replace pattern by "first argument" in "second argument"
# \g<1> - substitute the first part of the pattern, that in parenthesses (Mr\.|Ms\.|Mrs\.)

print(result) # Mr. J said, Ms. J was muredered by Mrs. J


def censor(input):
    '''Func that substitute bad word on CENSORED'''
    pattern = re.compile(r'fra\w+',re.I)
    result = pattern.sub("CENSORED",input)
    return result

print(censor("frack you")) # CENSORED you