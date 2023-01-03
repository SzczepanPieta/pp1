film_titles=["Godfather\n","Forest Gump\n","American Psycho\n","Jigsaw\n","Joker"]
file = open('07-FileHandling/films.txt','w')
for film_title in film_titles:
    file.write(film_title)
file.close()