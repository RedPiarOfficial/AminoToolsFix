import os
import sys
import time
import aminofixfix
from utils.logger import Logger, confg
from utils.scripts import Parse
from utils.Account import Account
try:
	from colorama import Fore, init
	from utils.Users import Users
	from utils.request import Updater
except:
	os.system("pip install colorama")
	os.system("pip install sqlite3")
	os.system("pip install coloredlogs")
	input("Press Enter to restart script: ")
	sys.exit()

class AToolsFix:
	def __init__(self):
		Updater().getVersion()
		self.client = aminofixfix.Client()
		self.log = Logger().get_logger()
		self.settings = confg().GetSettings()
		status = self.login()

	def login(self):
		if os.path.exists("./sid.txt"):
			self.loginSID()
		else:
			if self.settings["QuickLogin"]["status"]:
				email = self.settings["QuickLogin"]["email"]
				password = self.settings["QuickLogin"]["password"]
			else:
				email = input("[!] Enter your Email(AccountEmail): ")
				password = input("[!] Enter your Password(AccountPassword): ")
			self.log.info("trying to log in to your account...")
			clientDATA = self.client.login(email, password)
			status = self.checkAccountLogin(LoginBySid=False)
			if status:
				os.system("cls")
				self.CreateSidFile(data=clientDATA)
				self.functions()

	def loginSID(self):
		try:
			if self.log:
				self.log.info("[SID] trying to log in to your account...")
			with open(f"sid.txt", "r") as file:
				self.client.login_sid(file.read())
			status = self.checkAccountLogin(LoginBySid=True)
			if status:
				os.system("cls")
				self.functions()
		except Exception as e:
			print(e)
			self.checkAccountLogin(LoginBySid=True)

	def checkAccountLogin(self, LoginBySid):
		try:
			self.client.get_wallet_info().totalCoins
			if self.log:
				self.log.debug("Login checked is True!")
			return True
		except:
			if self.log:
				self.log.error("login Failed! try log again")
			time.sleep(3)
			if LoginBySid:
				os.remove("sid.txt")
			os.system("cls")
			self.login()
			return False

	def CreateSidFile(self, data):
		with open(f"sid.txt", "w") as file:
			file.write(data["sid"])

	def functions(self):
		os.system("cls")
		print("""
1. Account Functions
2. ObjectID Functions
3. User Functions
4. Script Functions
""")
		try:
			select = int(input("> "))
			actions = {
				1: self.accounts_functions,
				2: self.object_id_functions,
				3: self.user_functions,
				4: self.script_functions
			}
			action = actions.get(select)
			if action:
				action()
			else:
				if self.log:
					self.log.warning("Invalid selection. Please try again.")
				input("Press Enter: ")
				self.functions()
		except ValueError:
			if self.log:
				self.log.warning("Invalid input. Please enter a number.")
			input("Press Enter: ")
			self.functions()

	def accounts_functions(self):
		os.system("cls")
		print("""
____ObjectID Functions____
1. ProfileInfo
2. Wallet
3. get_chat_threads
0. Back to main menu
""")
		try:
			select = int(input("> "))
			actions = {
				1: self.ProfileInfo,
				2: self.wallet,
				3: self.get_chat_threads,
				0: self.functions
			}
			action = actions.get(select)
			if action:
				action()
			else:
				if self.log:
					self.log.warning("Invalid selection. Please try again.")
				input("Press Enter: ")
				self.object_id_functions()
		except ValueError:
			if self.log:
				self.log.warning("Invalid input. Please enter a number.")
			input("Press Enter: ")
			self.object_id_functions()

	def object_id_functions(self):
		os.system("cls")
		print("""
____ObjectID Functions____
1. get my communities
2. get Community ID from link
3. get UserID from link
4. get UserID from community
5. get PostID from community
0. Back to main menu
""")
		try:
			select = int(input("> "))
			actions = {
				1: self.get_my_communities,
				2: self.get_community_id,
				3: self.get_user_id_global,
				4: self.get_user_id_community,
				5: self.get_post_id,
				0: self.functions
			}
			action = actions.get(select)
			if action:
				action()
			else:
				if self.log:
					self.log.warning("Invalid selection. Please try again.")
				input("Press Enter: ")
				self.object_id_functions()
		except ValueError:
			if self.log:
				self.log.warning("Invalid input. Please enter a number.")
			input("Press Enter: ")
			self.object_id_functions()

	def user_functions(self):
		os.system("cls")
		print("""
______User Functions______
1. get all users(saved to file)
2. get online users(saved to file)
3. get user followers
4. get user following
5. get user info
0. Back to main menu
""")
		try:
			select = int(input("> "))
			actions = {
				1: self.get_all_users,
				2: self.get_online_users,
				3: self.get_user_followers,
				4: self.get_user_following,
				5: self.get_user_info,
				0: self.functions
			}
			action = actions.get(select)
			if action:
				action()
			else:
				if self.log:
					self.log.warning("Invalid selection. Please try again.")
				input("Press Enter: ")
				self.user_functions()
		except ValueError:
			if self.log:
				self.log.warning("Invalid input. Please enter a number.")
			input("Press Enter: ")
			self.user_functions()

	def script_functions(self):
		os.system("cls")
		print("""
_____Script Functions_____
1. Parse communities users
0. Back to main menu
""")
		try:
			select = int(input("> "))
			actions = {
				1: self.parse_communities_users,
				0: self.functions
			}
			action = actions.get(select)
			if action:
				action()
			else:
				if self.log:
					self.log.warning("Invalid selection. Please try again.")
				input("Press Enter: ")
				self.script_functions()
		except ValueError:
			if self.log:
				self.log.warning("Invalid input. Please enter a number.")
			input("Press Enter: ")
			self.script_functions()
	"""

	Account Functions

	"""
	def ProfileInfo(self):
		Account(self.client).ProfileInfo()
		input("Press Enter: ")
		self.accounts_functions()
	def wallet(self):
		Account(self.client).wallet()
		input("Press Enter: ")
		self.accounts_functions()

	def get_chat_threads(self):
		Account(self.client).get_chat_threads()
		input("Press Enter: ")
		self.accounts_functions()
	"""

	ObjectID Functions

	"""
	def get_my_communities(self):
		os.system("cls")
		com = self.client.sub_clients(size=100)
		titles = com.name
		users = com.usersCount
		comId = com.comId
		link = com.link
		for name, count, Id, url in zip(titles, users, comId, link):
			print(f'''title: {name}
usersCount: {count}
comId: {Id}
link: {url}
{"-"*30}
''')
		input("Press Enter: ")
		self.object_id_functions()

	def get_community_id(self):
		URL = input("[!] Enter link to community: ")
		print(f"ID: {self.client.get_from_code(URL).comId}")
		input("Press Enter: ")
		self.object_id_functions()

	def get_user_id_global(self):
		URL = input("[!] Enter link to user(Global): ")
		print(f"ID: {self.client.get_from_code(URL).objectId}")
		input("Press Enter: ")
		self.object_id_functions()

	def get_user_id_community(self):
		URL = input("[!] Enter link to user from community: ")
		comID = self.client.get_from_code(URL).comId
		SubClient = aminofixfix.SubClient(mainClient=self.client, comId=comID)
		print(f"UserID: {SubClient.get_from_code(URL).objectId}")
		input("Press Enter: ")
		self.object_id_functions()

	def get_post_id(self):
		URL = input("[!] Enter link to post from community: ")
		comID = self.client.get_from_code(URL).comId
		SubClient = aminofixfix.SubClient(mainClient=self.client, comId=comID)
		print(f"PostID: {SubClient.get_from_code(URL).objectId}")
		input("Press Enter: ")
		self.object_id_functions()

	def get_all_users(self):
		Users(mainClient=self.client).get_all_users()
		input("Press Enter: ")
		self.user_functions()

	def get_online_users(self):
		Users(mainClient=self.client).get_online_users()
		input("Press Enter: ")
		self.user_functions()

	def get_user_followers(self):
		Users(mainClient=self.client).get_user_followers()
		input("Press Enter: ")
		self.user_functions()

	def get_user_following(self):
		Users(mainClient=self.client).get_user_following()
		input("Press Enter: ")
		self.user_functions()

	def get_user_info(self):
		Users(mainClient=self.client).get_user_info()
		input("Press Enter: ")
		self.user_functions()

	def parse_communities_users(self):
		Parse(mainClient=self.client).CommunitiesUsers()
		input("Press Enter: ")
		self.script_functions()

	def test(self):
		print(self.client.get_account_info())
		input("Press Enter: ")
		self.script_functions()

if __name__ == "__main__":
	AToolsFix()