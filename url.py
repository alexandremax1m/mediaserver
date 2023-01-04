import ctypes, struct

from psutil import Popen as cmd
from psutil import AccessDenied as PSAD
from psutil import process_iter

from pathlib import Path

from os import getcwd

import requests,socket
from requests import Response
from ipaddress import IPv4Address

class File:
	__slots__ = "filename","ekey"
	def __init__(self,filename):
		self.filename = str(self.filename)
	def readc(self):
		print(open(f"{self.filename}",'r',encoding='UTF-8').read())
	def readbytes(self):
		print(open(f"{self.filename}",'rb').read())

class URL:
	__slots__ = "url","ip","ports"
	def __init__(self,url):
		if not requests.get(f"http://{url}").ok == True:
			self.url = None
			print('The URL May Not Exist :: ')
		else:
			self.url = url
			self.ip = socket.gethostbyname(f"{self.url}")
			self.ports = ()
	def transferhistory(self):
		for x in requests.get(f"http://{self.url}").history:
			print(x.headers)
	def reversepointer(self):
		return IPv4Address(socket.gethostbyname(f"{self.ip}")).reverse_pointer
	def ipinfo(self):
		return requests.get(f"https://ipinfo.io/{self.ip}/json").json() if self.url is not None else 'URL Not Valid'
	def httpgetheaders(self):
		print(requests.get(f"http://{self.url}").headers)
	def portscan(self,sequences):
		toscan = []
		for x in range(int(sequences)):
			toscan.append([])
			if not toscan[x]:
				toscan[x] = [x for x in range(int(input('Start Port :: ')),int(input('End Port :: ')))]
			for x in toscan[x]:
				if socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((f"{self.ip}",x)) == 0:
					if not type(self.ports) == list:
						self.ports = list(self.ports)
						self.ports.append(x)
						self.ports = tuple(self.ports)
				else:
					pass		
	def urlquery(self,query):
		return requests.get(f"http://{self.url}/{query}").status_code