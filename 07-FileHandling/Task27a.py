import csv

file=open("07-FileHandling/students.txt",newline='')
reader=csv.DictReader(file)
for row in reader:
    if int(row["age"])<30:
        print(row["first_name"],row["last_name"],row["email"])

file.close()
    
