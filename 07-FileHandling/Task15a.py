arr=["Godfather","Forest Gump","American Psycho","Jigsaw","Joker"]

file=open("07-FileHandling/film_titles.txt","w")
for x in range(len(arr)):
    file.write(arr[x])
    file.write("\n")
file.close()
