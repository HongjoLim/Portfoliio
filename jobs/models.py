from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200, blank=False)
    company = models.CharField(max_length=200, blank=False)