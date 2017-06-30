import re

s = '33one1two2three3four4'

pattern = re.compile(r'(\d+)+')
result = re.findall(pattern, s)

match = re.match("\d", s)
# print(result)
print(match.re)
print(match.pos)
print(match.endpos)
print(match.lastgroup)





