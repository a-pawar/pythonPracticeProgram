#Permutation
import fact_userdef_module as fu
print("Program to calculate permutation (npr).")
n=int(input("Enter total items(n): "))
r=int(input("Enter the number of item to be arrange(r): "))

if(n>=r):
    c=n-r
    fact_n=fu.fact(n)
    fact_c=fu.fact(c)
    per=fact_n/fact_c
    print("Permutation is",per)
else:
    print("Number of item to be select cannot greater than total item.")
#print(fr.fact(n))
