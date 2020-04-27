from django.db import models


# Create your models here.

class Subjects(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return '%s' % self.name


class Question(models.Model):
    SUBJECTS = [
        ('Mathematics', 'Mathematics'),
        ('English', 'English'),
        ('Civic', 'Civic'),
        ('Data processing','Data Processing'),
        ('Computer Studies', 'Computer Studies'),
        ('Fishery','Fishery'),
        ('Islamic Studies', 'Islamic Studies'),
    ]

    subject = models.CharField(max_length=20, choices=SUBJECTS)
    question_text = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=1000, default='none')
    option2 = models.CharField(max_length=1000,default='none')
    option3 = models.CharField(max_length=1000,default='none')
    options4 = models.CharField(max_length=1000,default='none')

    def __str__(self):
        return '%s' % self.subject


    def __str__(self):
        return '%s' % self.subject

