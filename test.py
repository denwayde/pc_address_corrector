import re
import string
ch = "908"
print(ch.isdigit())

adr = "Никольско-Архангельский, Болотная-1А-18"
home = '1А'
ind = adr.find(home)

substr_part = adr[ind+len(home):]
for x in adr:
# print(substr_part)
# #print(re.fullmatch(r'\W', substr_part[0]))
# if re.fullmatch(r'\W', substr_part[0]):
#     kv = substr_part[1:]
#     print(kv)
# else:
#     print("vse norm")
#     print(substr_part)
# print(adr[ind+2:])

# if adr[ind+2:][0].isdigit():
#     print("кв "adr[ind+2:])
# else:
# print(re.findall(r'\W', adr))