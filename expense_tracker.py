e = []
def a_e():
	a = input("Enter the name of the product : ")
	b = input("Enter the price of the product")
	b = int(b)
	e.append({a:b})

def s_e():
	for i in e:
		for a,b in i.items():
			print("Name : ", a , "\tprice : ", b)
def c_e():
	sm = 0
	for i in e:
		for a,b in i.items():
			sm += b
	print("The Total expenses is : ", sm)
	
op = int(input("Welcome to our Expense tracker ! \n1. Add Item\n2.Show Items\n3.Calculate the total expense\n4.Quit\n"))

while op != 4 :
	if op == 1:
		a_e()
	elif op == 2 :
		s_e()
	elif op == 3 :
		c_e()
	elif op == 4:
		break
	else:
		print("Please select the right option ! ")
	op = int(input("Welcome to our Expense tracker ! \n1. Add Item\n2.Show Items\n3.Calculate the total expense\n4.Quit\n"))
	





