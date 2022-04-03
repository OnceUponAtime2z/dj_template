from django.db import models
from django.db.models.deletion import CASCADE

class Reporter(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name
    

class Article(models.Model):
    head_line = models.CharField(max_length=255)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
