from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200, blank=False)
    company = models.CharField(max_length=200, blank=False)
    startdate = models.DateField(blank = False)
    enddate = models.DateField(blank = False)
    detail = models.TextField(max_length=1000, blank=False , default="")

    def __str__(self):
        return self.title