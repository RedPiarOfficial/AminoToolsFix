import os
import sys
import time
import aminofixfix

try:
	from colorama import Fore, init
	from utils.Users import Users
except:
	os.system("pip install colorama")
	os.system("pip install sqlite3")
	input("Press Enter to restart script: ")
	sys.exit()

init()

class Colors:
	def __init__(self):
		self.Error = Fore.RED
		self.successfully = Fore.GREEN
		self.RESET = Fore.RESET

class AToolsFix:
	def __init__(self):
		self.client = aminofixfix.Client()
		status = self.login()

	def login(self):
		if os.path.exists("./sid.txt"):
			self.loginSID()
		else:
			email = input("[!] Enter your Email(AccountEmail): ")
			password = input("[!] Enter your Password(AccountPassword): ")
			print("trying to log in to your account...")
			clientDATA = self.client.login(email, password)
			status = self.checkAccountLogin(LoginBySid=False)
			if status:
				os.system("cls")
				self.CreateSidFile(data=clientDATA)
				self.Functions()

	def loginSID(self):
		try:
			print("[SID] trying to log in to your account...")
			with open(f"sid.txt", "r") as file:
				self.client.login_sid(file.read())
			status = self.checkAccountLogin(LoginBySid=True)
			if status:
				os.system("cls")
				self.Functions()
		except Exception as e:
			print(e)
			self.checkAccountLogin(LoginBySid=True)

	def checkAccountLogin(self, LoginBySid):
		try:
			self.client.get_wallet_info().totalCoins
			print("Login checked is True!")
			return True
		except:
			print("login Failed! try log again")
			time.sleep(3)
			if LoginBySid:
				os.remove("sid.txt")
			os.system("cls")
			self.login()
			return False

	def CreateSidFile(self, data):
		with open(f"sid.txt", "w") as file:
			file.write(data["sid"])

	def Functions(self):
		os.system("cls")
		print("""

____ObjectIDs____
1. get Community ID from link
2. get UserID from link
3. get UserID from community
4. get PostID from community
______Users______
5. get all users(saved to file)
6. get online users(saved to file)
7. get user followers
8. get user following
9. get user info
""")
		select = int(input("> "))
		if select == 1:
			URL = input("[!] Enter link to community: ")
			print(f"ID: {self.client.get_from_code(URL).comId}")
			input("Press Enter: ")
			self.Functions()
		elif select == 2:
			URL = input("[!] Enter link to user: ")
			print(f"ID: {self.client.get_from_code(URL).objectId}")
			input("Press Enter: ")
			self.Functions()
		elif select == 3:
			URL = input("[!] Enter link to user from community: ")
			comID = self.client.get_from_code(URL).comId
			SubClient = aminofixfix.SubClient(mainClient=self.client, comId=comID)
			print(f"UserID: {SubClient.get_from_code(URL).objectId}")
			input("Press Enter: ")
			self.Functions()
		elif select == 4:
			URL = input("[!] Enter link to post from community: ")
			comID = self.client.get_from_code(URL).comId
			SubClient = aminofixfix.SubClient(mainClient=self.client, comId=comID)
			print(f"PostID: {SubClient.get_from_code(URL).objectId}")
			input("Press Enter: ")
			self.Functions()
		elif select == 5:
			Users(mainClient=self.client).get_all_users()
			input("Press Enter: ")
			self.Functions()
		elif select == 6:
			Users(mainClient=self.client).get_online_users()
			input("Press Enter: ")
			self.Functions()
		elif select == 7:
			Users(mainClient=self.client).get_user_followers()
			input("Press Enter: ")
			self.Functions()
		elif select == 8:
			Users(mainClient=self.client).get_user_following()
			input("Press Enter: ")
			self.Functions()
		elif select == 9:
			Users(mainClient=self.client).get_user_info()
			input("Press Enter: ")
			self.Functions()

if __name__ == "__main__":
	AToolsFix()