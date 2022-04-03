from django.db import models
from django.db.models.deletion import CASCADE


class Category(models.Model):

    name = models.CharField(max_length=55)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.name




class Student(models.Model):

    student_code = models.CharField(max_length=13)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.first_name + " " + self.last_name




class Subject(models.Model):

    subject_code = models.CharField(max_length=22)
    subject_name_th = models.CharField(max_length=255)
    subject_name_en = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    student = models.ManyToManyField(
        Student, default=None, null=True, blank=True)

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.subject_name_th + " " + self.subject_name_en


