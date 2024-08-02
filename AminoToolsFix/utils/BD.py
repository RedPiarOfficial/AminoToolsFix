import sqlite3
class Controller:
	def __init__(self):
		self.conn = None
		self.cursor = None

	def createBDForAllUsers(self):
		self.cursor.execute('''
			CREATE TABLE IF NOT EXISTS All_users (
				userId TEXT UNIQUE,
				nickname TEXT,
				level INT,
				reputation INT,
				followers INT,
				following INT,
				community TEXT,
				communityID TEXT
			)
			''')
	def createBDForOnlineUsers(self):
		self.cursor.execute('''
			CREATE TABLE IF NOT EXISTS online_users (
				userId TEXT UNIQUE,
				nickname TEXT,
				level INT,
				reputation INT,
				followers INT,
				following INT,
				community TEXT,
				communityID TEXT
			)
			''')
	def add_userALL(self, userId, nickname, level, reputation, followers, following, community, communityID):
		try:
			self.cursor.execute('''
				INSERT INTO All_users (userId, nickname, level, reputation, followers, following, community, communityID)
				VALUES (?, ?, ?, ?, ?, ?, ?, ?)
			''', (userId, nickname, level, reputation, followers, following, community, communityID))
		except:
			pass
	def saveUser(self):
		self.conn.commit()
	def add_user(self, userId, nickname, level, reputation, followers, following, community, communityID):
		try:
			self.cursor.execute('''
				INSERT INTO online_users (userId, nickname, level, reputation, followers, following, community, communityID)
				VALUES (?, ?, ?, ?, ?, ?, ?, ?)
			''', (userId, nickname, level, reputation, followers, following, community, communityID))
			self.conn.commit()
		except:
			pass
	def close(self):
		self.conn.close()
	def __enter__(self):
		self.conn = sqlite3.connect("DataBase.db")
		self.cursor = self.conn.cursor()
		
		return self
	def __exit__(self, exc_type, exc_value, traceback):
		self.close()
		return False