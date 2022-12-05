MeatAndFish=open("shoppinglist.txt","r")
GrainAndBread=open("shoppinglist.txt","r")
shoppinglist=open("shoppinglist.txt","w")

for lines in MeatAndFish:
    shoppinglist.write(lines)
shoppinglist.write("\n")
for lines in GrainAndBread:
    shoppinglist.write(lines)
    
MeatAndFish.close()
GrainAndBread.close()
shoppinglist.close()