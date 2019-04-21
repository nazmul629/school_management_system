from django.db import models

class Year(models.Model):
    year = models.IntegerField(unique=True)
    def __str__(self):
        return str(self.year)

class Month(models.Model):
    month = models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.month


class Select_Month(models.Model):
    year = models.ForeignKey(Year, on_delete = models.CASCADE)
    month = models.ForeignKey(Month, on_delete = models.CASCADE, unique=True)
    def __str__(self):
        return str(self.month)