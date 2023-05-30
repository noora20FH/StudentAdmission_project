from django.db import models

class AdminApp(models.Model):
    name = models.CharField(max_length=50, default='')
    reportScore = models.CharField(max_length=50)
    achievement = models.CharField(max_length=50)
    skill = models.CharField(max_length=50)
    interview = models.CharField(max_length=50)
    SchoolAcc = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
