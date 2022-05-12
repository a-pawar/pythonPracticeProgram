#combination

print("Program to find combinations (ncr).")
n=int(input("Enter total items(n): "))
r=int(input("Enter the number of item to be arrange(r): "))


def fact(a):
    fact_a=1
    for i in range(1,a+1):
        fact_a=fact_a*i
    return fact_a

if(n>=r):
    c=n-r
    fact_n=fact(n)
    fact_c=fact(c)
    fact_r=fact(r)
    com=fact_n/(fact_r*fact_c)

    print("Combination is",com)
else:
    print("number of item cannot be greater than total item")
