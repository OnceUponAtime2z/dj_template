from distutils.sysconfig import PREFIX
from sre_constants import CATEGORY
from sys import prefix
from unicodedata import category
from django.db import models

CATEGORY_CHOICES = [
    (1, 'News'),
    (2, 'Advertisement'),
    (3, 'Memo'),
]

PREFIX_CHOICES = [
    (1, 'Mr'),
    (2, 'Miss'),
    (3, 'Mrs'),
]

# Create your models here.
class Blog(models.Model):

    title = models.CharField(max_length=255)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=1)
    content = models.TextField()
    date_updated = models.DateTimeField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse("Blog_detail", kwargs={"pk": self.pk})

class Author(models.Model):

    prefix = models.IntegerField(choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dateofbirth = models.DateField()

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.first_name +" "+self.last_name

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})

