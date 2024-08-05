import aminofixfix
from utils.BD import Controller
from utils.logger import Logger
import time
class Parse:
	def __init__(self, mainClient):
		self.client = mainClient
		self.log = Logger().get_logger()

	def CommunitiesUsers(self):
		com = self.client.sub_clients(size=100)
		comIDs = com.comId
		start = 0
		end = 100
		request = 1
		for ID in comIDs:
			with Controller() as DataBase:
				DataBase.createBDForAllUsers()
				start = 0
				subclient = aminofixfix.SubClient(mainClient=self.client, comId=ID)
				CommunityInfo = self.client.get_community_info(ID)
				ComName = CommunityInfo.name
				while start < 10_000:
					Users = subclient.get_all_users(start=start, size=end)
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
							ID
						)
						print(f"""
request: {request}
TitleCommunity: {ComName}
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
					if not userId:
						if self.log:
							self.log.warning(f"break format: {ComName}")
						time.sleep(2)
						break
					