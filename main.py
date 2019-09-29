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
			password = stdiomask.getpass(prompt = 'Enter the password : ')
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

print("\n\n Now exiting")
