#What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(s)   # values are same so datatype is ignored
print(len(s))