from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    num_pages = models.IntegerField()

    def __str__(self):
        return self.title
