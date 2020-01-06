import re

titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)",
    "Mary Ann in Autumn (2010)",
    "Further Tales of the City (1982)",
    "Babycakes (1984)",
    "More Tales of the City (1980)",
    "Sure of You (1989)",
    "Michael Tolliver Lives (2007)"
]
fixed_books = []

# pattern = re.compile(r'([\w ]+) \((\d{4})\)') # it work too
pattern = re.compile(r'(?P<title>[\w ]+) \((?P<year>\d{4})\)')

for book in titles:
    # result = pattern.sub("\g<2> - \g<1>", book) # it work too
    result = pattern.sub("\g<year> - \g<title>", book)
    fixed_books.append(result)

fixed_books.sort()

print(fixed_books)
"""['1978 - Tales of the City', '1980 - More Tales of the City', '1982 - Further Tales of the City', '1984 - Babycakes', '1
987 - Significant Others', '1989 - Sure of You', '2007 - Michael Tolliver Lives', '2010 - Mary Ann in Autumn', '2014 - T
he Days of Anna Madrigal']"""