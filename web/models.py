from django.db import models

# Create your models here.


class User(models.Model):
    """
    user table
    """

    name = models.CharField(verbose_name='name', max_length=64, unique=True)
    email = models.EmailField(verbose_name='email', unique=True)
    password = models.CharField(verbose_name='password', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'user'
