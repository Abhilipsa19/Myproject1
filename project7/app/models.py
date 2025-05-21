from django.db import models

# Create your models here.
class Employee(models.Model):
    empno = models.IntegerField(primary_key= True)
    ename = models.CharField(max_length = 50)
    pno = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    add = models.TextField(max_length = 50)
    gender = models.CharField(max_length = 50)

    def __str__(self):
        return self.ename
