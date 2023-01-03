import json

favourite={
    "book":"Fall of Malasian Empire",
    "food":"grandma's",
    "hobby":"Hating on minorietes",
    "sport":"tenis",
    "game":"minecraft"
}

out_file = open("08-DictionariesStacksAndQueues/favourite.json", "w")
  
json.dump(favourite, out_file, indent = 4)
  
out_file.close()
