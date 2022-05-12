#combination
import fact_userdef_module as fu
print("Program to find combinations (ncr).")
n=int(input("Enter total items(n): "))
r=int(input("Enter the number of item to be arrange(r): "))


if(n>=r):
    c=n-r
    fact_n=fu.fact(n)
    fact_c=fu.fact(c)
    fact_r=fu.fact(r)
    com=fact_n/(fact_r*fact_c)

    print("Combination is",com)
else:
    print("number of item cannot be greater than total item")
