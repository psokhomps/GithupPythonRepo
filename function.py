Usr=input("Enter username: ")
Pwd=input("Enter password: ")
def logon_auth(Usr, Pwd):
	if (Usr=="admin1" and Pwd=="123"):
		print("You are authenticated.")
		return Usr, Pwd
	else:
		print("Incorrect username or password")
credential = logon_auth(Usr, Pwd)
print(credential)
