from django.db import models

class  Worker(models.Model):
    ename=models.CharField(max_length=30)
    salary=models.IntegerField()
    city=models.CharField(max_length=30)
    def __str__(self):
        return self.ename


