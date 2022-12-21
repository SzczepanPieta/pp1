class Students():
    last_id=100000
    studies = "UEK Kraków"
    
    def __init__(self, name,surname,field):
        self.name = name
        self.surname = surname
        self.field = field
        self.id = Students.last_id
        Students.last_id+=1
    
    def __str__(self) ->str:
        return f"{self.name} {self.surname} ({self.id}), {self.field} {Students.studies}"
    

student1 = Students("Anna","Maj","Applied Informatics,")
print(student1)
student2 = Students("Jan","Baniek","Applied Informatics,")
print(student2)



