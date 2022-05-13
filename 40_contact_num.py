
class contact:
    def __init__(self,contact_name,contact_num):
        self.contact_name=contact_name
        self.contact_num=contact_num
    def put_data(self):
        f=open("phonebookfile.txt","a")
        f.write(self.contact_name)
        f.write("\t")
        f.write(self.contact_num)
        f.write("\n")
        f.close()
    def get_data():
        f=open("phonebookfile.txt","r")
        i=f.read()
        f.close()
        return i
        



#contact_name=input("Enter Contact Name: ")
#contact_num=input("Enter Contact number: ")

#contact1=contact(contact_name,contact_num)
#contact1.put_data()


list1=[]
i=contact.get_data()
list1=i
print(i)
print(list1)

y=i.split("\n")
print(y)

print(y[0])
i=y[0]
print(i)
print(type(i))
#j=i.split("\t")
#print(j)
table=[]
for i in y:
    table.append(i.split("\t"))
print(table)
k=len(y)
print("\nContact Name","  Phone Number")
for i in range(0,k-1):
    for j in range(0,2): 
        print(table[i][j],end="\t\t")
    print("\n")



