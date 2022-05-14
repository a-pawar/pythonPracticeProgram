class employee():
	def __init__(self):
		self.firstname = input("Enter Your First Name : ")
		self.lastname = input("Enter Your Last Name : ")
		self.education = input("Enter Your Educational Qualification : ")
		self.contact_no = input("Enter Your Contact Number : ")
		self.mail_id = input("Enter Your Email Id : ")
		self.address = input("Enter Your address: ")
		self.account_id = input("Enter Your Bank Account Number : ")
		self.adhar_id = input("Enter Your Adhar Card Number : ")

	def show(self) :
		print("=========================================")
		print("Your First Name : ",self.firstname)
		print("Your Last Name : " ,self.lastname)
		print("Your Educational Qualification : ",self.education)
		print("Your Contact Number : ",self.contact_no)
		print("Your Email Id : ",self.mail_id)
		print("Your Address: ",self.address)
		print("Your Bank Account Number : ",self.account_id)
		print("Your Adhar Card Number : ",self.adhar_id)
		print("=========================================")

class office_assistant(employee):
	def __init__(self):
		super().__init__()
		self.salary = input("Enter Your Salary")
		self.grade = input("Enter Your Grade")		



	def show2(self) :
		super().show()
		print("Your Salary : ",self.salary)
		print("Your Grade : ",self.grade)

e1 = office_assistant()
e1.show2()
e1.show()



