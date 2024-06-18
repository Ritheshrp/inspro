from django.db import models

# Create your models here.
class feedbackData(models.Model):
    name = models.CharField(max_length=20)
    rating = models.IntegerField()
    feedback = models.CharField(max_length=10)
    create_at=models.DateTimeField(auto_now=True)
class courseData(models.Model):
    courseno=models.IntegerField()
    coursename=models.CharField(max_length=20)
    timings=models.CharField(max_length=70)
    startdate=models.DateField()
    duration=models.CharField(max_length=20)
    coursefee=models.IntegerField()
    trainername=models.CharField(max_length=20)