from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=20)
    price = models.FloatField(default=100)
    pub_date = models.DateField(default="1898-8-25")

    def __str__(self):
        return self.title


class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=(('male', "男"), ('female', "女")), default="male")
    content = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
