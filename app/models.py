from django.db import models

# Create your models here.
class Faculty(models.Model):
    Sr            = models.CharField(max_length = 200, blank = True)
    name          =  models.CharField(max_length = 200)
    designation   =  models.CharField(max_length = 200)
    qualification = models.CharField(max_length = 200)

    def __str__(self):
        return self.name


class Strength(models.Model):
    klass = models.CharField(max_length = 10)
    strength = models.CharField(max_length = 10)

    def __str__(self):
        return self.klass

class Infrastructure(models.Model):
    title = models.CharField(max_length = 100)
    detail = models.CharField(max_length = 100)

    def __str__(self):
        return self.title



class Notice(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=200)
    notice = models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Syllabus(models.Model):
    sr = models.IntegerField()
    Class = models.CharField(max_length=200)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.Class

class Book_list(models.Model):
    sr = models.IntegerField()
    session = models.CharField(max_length=200)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.session
