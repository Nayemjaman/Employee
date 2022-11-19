from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name





class Role(models.Model):
    name = models.CharField(max_length=100,null=False)

    def __str__(self) -> str:
        return self.name



class Employee(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100,null=False)
    salary = models.IntegerField(null=False,default=0)
    bonus = models.IntegerField(null=False,)
    phone_number = models.CharField(max_length=100,null=False)
    hire_date = models.DateField()

    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)

    
    def __str__(self) -> str:
        return '%s %s' %(self.first_name,self.last_name)