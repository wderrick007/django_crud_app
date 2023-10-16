from django.db import models

# Create your models here.
 
class Person(models.Model):  
    person_id = models.CharField(max_length=20)  
    person_name = models.CharField(max_length=100)  
    person_email = models.EmailField()  
    person_contact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "person"  
