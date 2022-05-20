import requests
import json


def prrr():
    print("-----------------------------------")


r = requests.get('https://v2.jokeapi.dev/joke/Any?type=single')
print(r.content)
prrr()
json_file = json.loads(r.content).items()
print(json_file)
prrr()
for section, commands in json_file:
    print(section, commands)
prrr()
for section, commands in json_file:
    if section == "joke":
        print("JOKE: ", commands)
