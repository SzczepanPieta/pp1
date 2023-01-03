MeatAndFish=open("07-FileHandling/MeatAndFish.txt","r")
GrainAndBread=open("07-FileHandling/GrainAndBread.txt","r")
shoppinglist=open("07-FileHandling/shoppinglist.txt","w")

for lines in MeatAndFish:
    shoppinglist.write(lines)
for lines in GrainAndBread:
    shoppinglist.write(lines)
    
MeatAndFish.close()
GrainAndBread.close()
shoppinglist.close()