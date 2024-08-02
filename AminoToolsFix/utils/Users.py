from utils.BD import Controller
from aminofixfix import SubClient as Sclient

class Users:
	def __init__(self, mainClient):
		self.client = mainClient

	def get_all_users(self):
		URL = input("[!] Enter link to community: ")
		ComID = self.client.get_from_code(URL).comId
		start = 0
		end = 100
		request = 1
		SubClient = Sclient(mainClient=self.client, comId=ComID)
		Users = SubClient.get_all_users(start=start, size=end)
		total_users = Users.userProfileCount
		CommunityInfo = self.client.get_community_info(ComID)
		ComName = CommunityInfo.name
		with Controller() as DataBase:
			DataBase.createBDForAllUsers()
			while start < total_users:
				Users = SubClient.get_all_users(start=start, size=end)
				userId = Users.profile.userId
				nickname = Users.profile.nickname
				level = Users.profile.level
				reputation = Users.profile.reputation
				followers = Users.profile.followersCount
				following = Users.profile.followingCount
				for id, name, lvl, repu, followrs, followng in zip(userId, nickname, level, reputation, followers, following):
					DataBase.add_userALL(
							id,
							name,
							int(lvl),
							int(repu),
							int(followrs),
							int(followng),
							ComName,
							ComID
						)
					print(f"""
request: {request}
UserID: {id}
nickname: {name}
level: {lvl}
reputation: {repu}
followers: {followrs}
following: {followng}
{"-"*30}
""")
				DataBase.saveUser()
				start += end
				request +=1
				if start > 10000:
					break

	def get_online_users(self):
		URL = input("[!] Enter link to community: ")
		ComID = self.client.get_from_code(URL).comId
		start = 0
		end = 100
		request = 1
		SubClient = Sclient(mainClient=self.client, comId=ComID)
		Users = SubClient.get_online_users(start=start, size=end)
		total_users = Users.userProfileCount
		CommunityInfo = self.client.get_community_info(ComID)
		ComName = CommunityInfo.name
		with Controller() as DataBase:
			DataBase.createBDForOnlineUsers()
			while start < total_users:
				Users = SubClient.get_online_users(start=start, size=end)
				userId = Users.profile.userId
				nickname = Users.profile.nickname
				level = Users.profile.level
				reputation = Users.profile.reputation
				followers = Users.profile.followersCount
				following = Users.profile.followingCount
				for id, name, lvl, repu, followrs, followng in zip(userId, nickname, level, reputation, followers, following):
					DataBase.add_user(
							id,
							name,
							int(lvl),
							int(repu),
							int(followrs),
							int(followng),
							ComName,
							ComID
						)
					print(f"""
request: {request}
UserID: {id}
nickname: {name}
level: {lvl}
reputation: {repu}
followers: {followrs}
following: {followng}
{"-"*30}
""")
				start += end
				request +=1

	def get_user_followers(self):
		URL = input("[!] Enter link to community: ")
		URL_User = input("[!] Enter link to user: ")
		ComID = self.client.get_from_code(URL).comId
		UserID = self.client.get_from_code(URL_User).objectId
		start = 0
		end = 100
		request = 1
		SubClient = Sclient(mainClient=self.client, comId=ComID)
		UserInfo = SubClient.get_user_info(UserID)
		total_users = UserInfo.followersCount
		while start < total_users:
			Users = SubClient.get_user_followers(UserID, start=start, size=end)
			userId = Users.userId
			nickname = Users.nickname
			level = Users.level
			reputation = Users.reputation
			followers = Users.followersCount
			following = Users.followingCount
			for id, name, lvl, repu, followrs, followng in zip(userId, nickname, level, reputation, followers, following):
				print(f"""
request: {request}
UserID: {id}
nickname: {name}
level: {lvl}
reputation: {repu}
followers: {followrs}
following: {followng}
{"-"*30}
""")
			start += end
			request +=1

	def get_user_following(self):
		URL = input("[!] Enter link to community: ")
		URL_User = input("[!] Enter link to user: ")
		ComID = self.client.get_from_code(URL).comId
		UserID = self.client.get_from_code(URL_User).objectId
		start = 0
		end = 100
		request = 1
		SubClient = Sclient(mainClient=self.client, comId=ComID)
		UserInfo = SubClient.get_user_info(UserID)
		total_users = UserInfo.followingCount
		while start < total_users:
			Users = SubClient.get_user_following(UserID, start=start, size=end)
			userId = Users.userId
			nickname = Users.nickname
			level = Users.level
			reputation = Users.reputation
			followers = Users.followersCount
			following = Users.followingCount
			for id, name, lvl, repu, followrs, followng in zip(userId, nickname, level, reputation, followers, following):
				print(f"""
request: {request}
UserID: {id}
nickname: {name}
level: {lvl}
reputation: {repu}
followers: {followrs}
following: {followng}
{"-"*30}
""")
			start += end
			request +=1

	def get_user_info(self):
		URL = input("[!] Enter link to community: ")
		URL_User = input("[!] Enter link to user: ")
		ComID = self.client.get_from_code(URL).comId
		UserID = self.client.get_from_code(URL_User).objectId
		SubClient = Sclient(mainClient=self.client, comId=ComID)
		UserInfo = SubClient.get_user_info(UserID)
		userId = UserInfo.userId
		nickname = UserInfo.nickname
		level = UserInfo.level
		reputation = UserInfo.reputation
		followers = UserInfo.followersCount
		following = UserInfo.followingCount
		print(f"""
UserID: {userId}
nickname: {nickname}
level: {level}
reputation: {reputation}
followers: {followers}
following: {following}
{"-"*30}
""")