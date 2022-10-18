from django.db import models

# Create your models here.

class Students(models.Model):
    stdId=models.CharField(primary_key=True, max_length=6)
    stdFName=models.CharField(max_length=15)
    stdLName=models.CharField(max_length=15)
    stdEmail=models.EmailField(max_length=254)

class Courses(models.Model):
    crsId=models.CharField(primary_key=True, max_length=7)
    crsName=models.CharField(max_length=50)
    meets=models.CharField(max_length=50)

class Faculty(models.Model):
    ftyId=models.CharField(primary_key=True, max_length=6)
    ftyFName=models.CharField(max_length=15)
    ftyLName=models.CharField(max_length=15)

class Assignments(models.Model):
    asgmtId=models.CharField(primary_key=True, max_length=9)
    crsId=models.CharField(max_length=7)
    asgmtName=models.CharField(max_length=25)
    dateGiven=models.DateField
    dateDue=models.DateField
    attempts=models.IntegerField
