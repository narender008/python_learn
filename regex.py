
import re

text_to_search = """
1. this is plain text file.
2. what you are going to acheive with this?
3. third line hai ye.
4. this one is forth line.
5. and so on fifth line.
6. sixth.
7. Seventh.
8. eighth line.
9. ninth line.
10. last but not least tenth line.

ha ha hahahaha HAHAHAHAH

12 4 3 4 6 3

123.456.6745
654-453-5674
454*656*3456

# $ 5 * ( & ! )

Mr. corey
Ms. nina
Mrs. kumari
Mrs lyla
Mr Narendra
Mr T

my-server-com
hy.server.com
xy*server*com

cat
mat
pat
bat

"""
emails = """

narendrakumar@gmail.com
narendra.kumar@university.edu
nar-end-ra@gov.net
"""
urls = """

http://www.google.com
https://narendra.com
https://www.my-name.gov.in
http://www.hello_all.com

"""

pattern = re.compile(r'[a-yA-Y]+\://(www.)?[a-y-_]+\.[a-y]+')

matches = pattern.finditer(urls)

for match in matches:
    print(match.group())


# pattern = re.compile(r'[a-x-.]+@(gmail|university|gov)\.(com|edu|net)')
#
# matches = pattern.finditer(emails)
#
# for match in matches:
#     print(match.group())
# print(match.group())
