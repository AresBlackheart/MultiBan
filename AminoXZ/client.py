from time import time as timestamp
import json
from .lib.util.generator import Generator
from .lib.util import exceptions, helpers, headers
import requests
from typing import BinaryIO, Union


"""
	Made by Xsarz (@DXsarz)
	GitHub: https://github.com/xXxCLOTIxXx
	Telegram channel: https://t.me/DxsarzUnion
	YouTube: https://www.youtube.com/channel/UCNKEgQmAvt6dD7jeMLpte9Q]

"""



class Client():
	def __init__(self, deviceId: str=None, proxies: dict = None):
		requests.Session()
		self.sid = None
		self.proxies=proxies
		self.session = requests.Session()
		self.api = "https://service.narvii.com/api/v1"
		self.uid = None
		self.device = Generator().deviceId()
		self.User_Agent = self.device["user_agent"]
		if deviceId!=None:self.device_id = deviceId
		else:self.device_id = self.device["device_id"]

	def parser(self, header_type: str = "app", data = None, content_type: str = None, referer: str = None):
		if header_type == 'app':return headers.headers(data=data, content_type=content_type, deviceId=self.device_id, sid=self.sid).headers
		else:return headers.headers(data=data, content_type=content_type, deviceId=self.device_id, sid=self.sid).headers




	def login(self, email: str, password: str):
		"""
		Account login

		** options **

		- *email*: email
		- *password*: password

		"""


		data = json.dumps({
			"email": email,
			"v": 2,
			"secret": f"0 {password}",
			"deviceID": self.device_id,
			"clientType": 100,
			"action": "normal",
			"timestamp": int(timestamp() * 1000)
		})
		with self.session.post(f"{self.api}/g/s/auth/login", headers=self.parser(data=data), data=data, proxies=self.proxies) as response:
			if response.status_code != 200: return exceptions.checkExceptions(json.loads(response.text))
			else:json_response = json.loads(response.text)
		self.sid = json_response["sid"]
		self.uid = json_response["account"]["uid"]
		return self.uid



	def get_from_link(self, link: str):
		"""
		Get the information from the Amino URL.
		** options **
		- *link* : link.

		"""
		response = self.session.get(f"{self.api}/g/s/link-resolution?q={link}", headers=self.parser(), proxies=self.proxies)
		if response.status_code != 200: return exceptions.checkExceptions(json.loads(response.text))
		else: return json.loads(response.text)["linkInfoV2"]



	def get_community_members(self, comId: str,  type: str = "recent", start: int = 0, size: int = 25):

		"""
		Get chat members
		** options **

		- *start* : Where to start the list.
		- *size* : The size of the list.
		- *comId*: community id (if chat in community)
		- *type*: type of participants

		=-types-=
		recent - recent members
		online - online users
		banned - banned users
		featured - featured members
		leaders - leaders
		curators - curators

		"""
		if type == "recent": response = self.session.get(f"{self.api}/x{comId}/s/user-profile?type=recent&start={start}&size={size}", headers=self.parser(), proxies=self.proxies)
		elif type == 'online': response = self.session.get(f"{self.api}/x{comId}/s/live-layer?topic=ndtopic:x{comId}:online-members&start={start}&size={size}", headers=self.parser(), proxies=self.proxies)
		elif type == "banned": response = self.session.get(f"{self.api}/x{comId}/s/user-profile?type=banned&start={start}&size={size}", headers=self.parser(), proxies=self.proxies)
		elif type == "featured": response = self.session.get(f"{self.api}/x{comId}/s/user-profile?type=featured&start={start}&size={size}", headers=self.parser(), proxies=self.proxies)
		elif type == "leaders": response = self.session.get(f"{self.api}/x{comId}/s/user-profile?type=leaders&start={start}&size={size}", headers=self.parser(), proxies=self.proxies)
		elif type == "curators": response = self.session.get(f"{self.api}/x{comId}/s/user-profile?type=curators&start={start}&size={size}", headers=self.parser(), proxies=self.proxies)
		if response.status_code != 200: return exceptions.checkExceptions(json.loads(response.text))
		else: return json.loads(response.text)



	def get_my_communities(self, start: int = 0, size: int = 25):

		"""

		Get communities on account


		** options **

		- *start* : Where to start the list.
		- *size* : The size of the list.

		"""
		response = self.session.get(f"{self.api}/g/s/community/joined?v=1&start={start}&size={size}", headers=self.parser(), proxies=self.proxies)
		if response.status_code != 200: return exceptions.checkExceptions(json.loads(response.text))
		else: return json.loads(response.text)["communityList"]



	def get_user_info(self, userId: str, comId: str = None):
		"""
		get user information


		** options **

		- *userId* : user id
		- *comId*: community id (if you want to get a profile from a community)

		"""
		if comId!=None:
			response = self.session.get(f"{self.api}/x{comId}/s/user-profile/{userId}", headers=self.parser(), proxies=self.proxies)
			if response.status_code != 200: return exceptions.checkExceptions(json.loads(response.text))
			else: return json.loads(response.text)["userProfile"]

		response = self.session.get(f"{self.api}/g/s/user-profile/{userId}", headers=self.parser(), proxies=self.proxies)
		if response.status_code != 200: return exceptions.checkExceptions(json.loads(response.text))
		else: return json.loads(response.text)["userProfile"]



	def ban(self, comId: str, userId: str, reason: str, banType: int = None):
		data = {
			"reasonType": banType,
			"note": {
				"content": reason
			},
			"timestamp": int(timestamp() * 1000)
		}

		response = self.session.post(f"{self.api}/x{comId}/s/user-profile/{userId}/ban", headers=self.parser(data=json.dumps(data)), data=json.dumps(data), proxies=self.proxies)
		if response.status_code != 200: return exceptions.checkExceptions(json.loads(response.text))
		else: return json.loads(response.text)
