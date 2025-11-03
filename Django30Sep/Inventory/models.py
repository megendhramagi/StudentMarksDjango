from django.db import models

# Create your models here.
class StuMarks(models.Model):
    s_name = models.CharField(max_length=30)
    s_class = models.IntegerField()
    tamil_mark = models.IntegerField()
    english = models.IntegerField()
    maths = models.IntegerField()


