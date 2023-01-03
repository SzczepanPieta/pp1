import json

with open("08-DictionariesStacksAndQueues/sample1.json") as file:
    data = json.load(file)

for key,value in data.items():
    print(f"{key}: {value}")