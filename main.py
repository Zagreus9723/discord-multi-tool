import discum
import json
import time
import requests
print("What do you want to do?\nMass ping [1]\nServer flooder [2]\nChannel spammer [3]")
num = input("[?]: ")
if f"{num}" == "1":
    exec(requests.get("https://raw.githubusercontent.com/Apophis52/Discord-Mass-Ping-Bot/main/main.py").text)
elif f"{num}" == "2":
    exec(requests.get("https://raw.githubusercontent.com/Apophis52/Discord-Server-Spammer/main/main.py").text)
elif f"{num}" == "3":
    exec(requests.get("https://raw.githubusercontent.com/Apophis52/Channel-Spammer/main/main.py").text)
else:
    print("You retarded")
