from django.db import models


class User(models.Model):

    username = models.CharField(max_length = 12)
    unit = models.CharField(max_length= 12)
    personal_code = models.IntegerField(max_length = 6)


class Fileu(models.Model):

    user=models.ForeignKey(User, on_delete = models.CASCADE)
    datepublish=models.DateField()
    filz=models.FileField(upload_to = "upload/")


# Create your models here.
