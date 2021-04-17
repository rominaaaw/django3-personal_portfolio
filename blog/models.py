from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()


    def __str__(self):
        return self.title
