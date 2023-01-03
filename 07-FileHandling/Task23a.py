list1=open("07-FileHandling/GrainAndBread.txt","r")
list2=open("07-FileHandling/MeatAndFish.txt","r")
shop=open("07-FileHandling/shoppinglist.txt","w")
for line in list1:
    shop.write(line)
for line in list2:
    shop.write(line)
list1.close()
list2.close()
shop.close()