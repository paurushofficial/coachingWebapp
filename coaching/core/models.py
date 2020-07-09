from django.db import models

class subject(models.Model):
    course = models.CharField(max_length=225,default="none")
    name = models.CharField(max_length=225)
    paper = models.CharField(max_length=225)
    def __str__(self):
        return self.name
class student(models.Model):
    name = models.CharField(max_length=255)
    fathersName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    admissionClass = models.CharField(max_length=255)
    contact = models.CharField(max_length=25)
    subject1 = models.CharField(max_length=225)
    subject2 = models.CharField(max_length=225)
    subject3 = models.CharField(max_length=225)
    subject4 = models.CharField(max_length=225)
    subject5 = models.CharField(max_length=225)
    email = models.CharField(max_length=255, default='NA')
    aadhar = models.CharField(max_length=255, default='NA')
    
    def __str__(self):
        return self.name

    