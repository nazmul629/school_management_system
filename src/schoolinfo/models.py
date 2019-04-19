from django.db import models


class Schoolinfo(models.Model):
    school_name = models.CharField(max_length=100,unique=True)
    school_img = models.ImageField()
    school_address=models.TextField()
    
    def __str__(self):
        return str(self.school_name)