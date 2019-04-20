from django.db import models

class Schoolallclass(models.Model):
    Class = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.Class)

class class_section(models.Model):
    section = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return str(self.section)
    

class StudentInfo(models.Model):
    
    Student_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender_list = (('Male',"Male"),('FeMale','Female'))
    gender = models.CharField(max_length=10, choices = gender_list)
    Class = models.ForeignKey(Schoolallclass, on_delete = models.CASCADE)
    roll= models.IntegerField(unique=True)
    scation = models.ForeignKey(class_section, on_delete = models.CASCADE)
    fathers_name = models.CharField(max_length=50)
    mothers_name =  models.CharField(max_length=50)
    address = models.TextField()
    mobile = models.CharField(max_length=16)
    

    def __str__(self):
        return self.Student_name
    