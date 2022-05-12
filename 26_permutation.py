#Permutation
print("Program to calculate permutation (npr).")
n=int(input("Enter total items(n): "))
r=int(input("Enter the number of item to be arrange(r): "))


#Calculate n factorial
fact_n=1
for i in range(1,n+1):
    fact_n=fact_n*i
#print(fac_n)

#Calculation c 
fact_r=1
for i in range(1,r+1):
    fact_r *=i
#print(fac_r)

per=fact_n/fact_r
print("Permutation is",per)




