from functools import reduce


list1 = [2,25,14,28,47,12,36,45,55,659]

print(list1)

sum = reduce(lambda x,y : x+y, list1)
print(sum)
