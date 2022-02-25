import socket
import time 
from IPy import IP
def scan(target,port_num):
    converted_ip = check_ip(target) #we check the IP
    print('\n ' + '[~] Scanning Target: ' + str(target))
    for port in range(1,port_num):
        scan_port(converted_ip, port)
def check_ip(ip):
	try:
		IP(ip)
		return(ip)
	except ValueError:
		return socket.gethostbyname(ip)
def get_banner(s):
    return s.recv(1024)
    
def scan_port(ipaddress,port):
    try:
        sock = socket.socket()
        sock.settimeout(tim_out)
        sock.connect((ipaddress,port))
        try:
            banner = get_banner(socket)
            print('[✔] Port ' + str(port) + ' is Open.' + ' && ' + '[~] Banner Information : ' +str(banner.decode().strip('\n')))
        except:
            print('[✔] Port ' + str(port) + ' is Open.')
    except:
        with open('closed_ports.txt','w') as file:
            file.seek(0)
            file.write('\n'+ '[x] Port ' + str(port) + 'is closed.')
targets = input("[+] Enter Target/Targets to Scan : ") #we ask the target website/IP
port_num = int(input('[?] Enter the number of Ports you want to scan: '))
tim_out = int(input('[?] Enter the timeout you prefer: '))
if ',' in targets:
    for ip_add in targets.split(','):
    #we check if it's 2 targets or 1 target
        scan(ip_add.strip(''),port_num)																	
else:
    scan(targets,port_num)
    #if no comma , they start tge scan
