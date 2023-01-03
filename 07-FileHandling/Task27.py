import csv
with open("07-FileHandling/students.txt",newline='') as f:
    spamreader=csv.DictReader(f)
    for row in spamreader:
        if int(row["age"])<30:
            print(row["first_name"],row["last_name"],row["email"])
        
f.close()



dids={
    "imie":"frodo",
    "rasa":"PIEZ",
    "wiek":2

}

print(dids["imie"])
    