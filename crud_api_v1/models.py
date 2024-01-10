from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    # phone_number = models.
    
    def __str__(self) -> str:
        return f"Full Name: {self.first_name} {self.last_name}, Email: {self.email}, Age: {self.age}, roll_no: {self.roll_no}"
    
