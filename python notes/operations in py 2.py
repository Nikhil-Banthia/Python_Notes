tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# RES = tuple1.count(3)
# RES = tuple1.index(3)
#We are searching for the first occurrence of the value 3 between the indices 4 and 8.
RES = tuple1.index(3,4,8)
print(RES)
