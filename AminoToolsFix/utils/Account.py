
class Account:
	def __init__(self, mainClient):
		self.client = mainClient
		self.account = self.client.get_account_info()

	def ProfileInfo(self):
		print(f"""
nickname: {self.account.nickname}
aminoId: {self.account.aminoId}
userId: {self.account.userId}
coins: {self.client.get_wallet_info().totalCoins}
createdTime: {self.account.createdTime}

""")
	def wallet(self):
		print(f"Coins {self.client.get_wallet_info().totalCoins}")

	def get_chat_threads(self):
		chats = self.client.get_chat_threads()
		for title, chatid, nickname in zip(chats.title, chats.chatId, chats.author.nickname):
			print(f'''
titleChat: {title if title != None else "Unknown"}
nickname: {nickname}
chatId: {chatid}
{"-"*30}
''')