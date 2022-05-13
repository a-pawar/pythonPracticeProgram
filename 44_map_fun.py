
list1 = [2,25,14,28,47,12,36,45,55,659]

list_even= list(filter(lambda x : x%2==0,list1))

list_even2 = list(map(lambda x: x*2,list_even))

print(list_even)
print(list_even2)

