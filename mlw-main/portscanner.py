import socket
import time 
from IPy import IP

class PortScan():
	banners = []
	open_ports = []
	def __init__(self,target, port_num):
		self.target = target
		self.port_num = port_num
		
	def scan(self):
		for port in range(20,90):
			self.scan_port(port)
			
	def check_ip(self):
		try:
			IP(self.target)
			return(self.target)
		except ValueError:
			return socket.gethostbyname(self.target)
			
	def scan_port(self,port):
		try:
			converted_ip = self.check_ip()
			sock = socket.socket()
			sock.settimeout(tim_out)
			sock.connect((converted_ip,port))
			self.open_ports.append(port)
			try:
				banner = sock.recv(1024).decode().strip('\n').strip('\r')
				self.banners.append(banner)
			except:
				self.banners.append('')
			sock.close()
		except:
			pass
