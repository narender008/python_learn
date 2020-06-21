
# from my_module import find_index
# import sys
#
# courses = ["hindi", "physics", "maths", "english", "sst"]
#
# number = find_index(courses, "maths")
#
# # print(number)
#
# print(sys.path)


import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r'''
(?P<email>\b[\w\d*-_]+@[^\s\t,]+\b) #email
,[\s\t]
(?P<phone>\b\d{3}-\d{3}-\d{4})
''', string, re.I | re.M | re.X)


twitters = re.search(r'''
(?P<twitter>@[^\s\t]+)$
''', string, re.I | re.M | re.X)

print(twitters.groupdict())
