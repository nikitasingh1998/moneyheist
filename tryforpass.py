'''
import getpass

password = getpass.getpass()
print(password)
'''

values = {
			1: 'one()',
			2: 'two()'
		}

def one():
	print("one")
	
def two():
	print("two")
 
def func(val):
	if val in values.keys():
		x = values[val]
		eval(x)
	else:
		print("wrong option")


inp = int(input("num(1 or 2): "))
func(inp)
