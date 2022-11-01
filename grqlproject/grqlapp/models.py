from django.db import models


class Bio(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    native=models.CharField(max_length=20)

    def __str__(self):
        return self.name