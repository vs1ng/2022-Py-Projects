import portscanner

targets_ip=input('[?] Enter Target to scan for vulnerable open ports: ')
port_number = int(input('[?] Enter the number of ports you want to scan: '))
vul_file = input('[?] Enter file path to the file with vulnerable softwares: ')
print('\n')
target = portscanner.PortScan(targets_ip,port_number)
target.scan()

with open(vul_file, 'r') as file:
	count = 0
	for banner in target.banners:
		file.seek(0)
		for line in file.readlines():
			if line.strip() in banner:
				print('[!] Exploitable Banner : ' + banner + ' on port ' + str(target.open_ports[count]))
		count += 1
		
