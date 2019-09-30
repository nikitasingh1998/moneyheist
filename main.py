import stdiomask
print("WELCOME TO MONEYHEIST")

name = ""
print("Enter credentials: \n")
credentials = {
				"Nikita" : "Nikit@1232",
				"parth" : "Krishna",
				"admin": "password"
			 }

var1,var2=1,3
while var1==1:
	name = input("Enter the username :")
	if name in credentials.keys():
		var1 = 0
		while var2 > 0:
			#password = input("Enter the password : ")
			password = stdiomask.getpass(prompt = 'Enter the password : ', mask='*')
			if password == credentials[name]:
				var2 = 0
				print("LOGGED IN")
			else:
				var2-=1
				print("You have ",var2," attempts remaining")
				if var2==0:
					print("Now calling 911!!!")
	else:
		print("Enter correct Details!!!  \n")


# For the transactions and stuff

'''

total_amt = 5000
in_cash = 2000
in_bank = 3000
print("SELECT WHAT YOU WOULD LIKE TO DO.\n")
print(" 1.	Register a positive transaction.\n 2.	Register a negative transaction\n 3.	Check balance.\n 4.	Coming soon\n")
def cash():
	amt = input("Enter the cash to be added")
	in_cash = in_cash + amt

def account():
	amt = input("Enter the cash to be added")
	in_bank = in_bank + amt

def registerp():
	print("Enter the transaction type.\n")
	print(" 1.	CASH\n 2.	IN ACCOUNT(BANK)\n")
	def p_transac():
		swticher = {
			1: cash,
			2: account
		}

#def registern():
#	print("Enter the transaction type.\n")
#	print(" 1.	\n 2.	IN ACCOUNT(BANK)\n")
#	def p_transac(ptran):
#		swticher = {
#			1: cash(amt),
#			2: account(amt)
#		}
  
num = int(input("Enter your choice"))
def main_switch(num):
	switcher = {
		1: registerp,
		2: registern,
		3: check_balance,
		4: coming_up
		}
'''

total_amt = 5000
in_cash = 2000
in_bank = 3000
print("SELECT WHAT YOU WOULD LIKE TO DO.\n")
print(" 1.	Register a positive transaction.\n 2.	Register a negative transaction\n 3.	Check balance.\n")

main_switch = {
		1 : 'registerp()',
		2 : 'registern()',
		3 : 'check_balance()'
	}
ptr_switch = {
		1 : 'cash()',
		2 : 'account()'
	}

def cash():
	c = float(input("Enter the amount added in cash : "))
	in_cash = in_cash + c
	total_amt = total_amt + c

def account():
	c = float(input("Enter the amount added in account(online payment) : "))
	in_bank = in_bank + c
	total_amt = total_amt + c



def registerp():
	print("Enter the transaction type.\n")
	print(" 1.	CASH\n 2.	IN ACCOUNT(BANK)\n")
	inp_type = int(input("Enter the type of transaction done : "))
	regi_p_type(inp_type)

def regi_p_type(val):
	if val in ptr_switch.keys():
		x = ptr_switch[val]
		eval(x)
	else:
		print("wrong Option")


def func(val):
	if val in main_switch.keys():
		x = main_switch[val]
		eval(x)
	else:
		print("Wrong Option")


inp = int(input("Enter your choice : "))
func(inp)

print("\n Printing the current financial status.\n")
print("TOTAL AMOUNT : ",total_amt,"\nAMOUNT IN CASH : ",in_cash,"\nAMOUNT IN BANK : ",in_bank)
print("\n\n Now exiting")



