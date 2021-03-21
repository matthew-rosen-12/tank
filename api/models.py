from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
# class Client(models.Model):
# 	user = models.OneToOneField(User, null=True,on_delete=models.cascade)
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=120)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ('name',)


class Tank(models.Model):
    title = models.CharField(max_length=120)
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Fish(models.Model):
    breed = models.CharField(max_length=50)
    speed = models.SmallIntegerField()
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)

    def __str__(self):
        return self.breed

    class Meta:
        ordering = ('tank',)

    def save(self, *args, **kwargs):
        validBreeds = ['sun']
        if self.breed in validBreeds:
            super(Fish, self).save(*args, **kwargs)
        else:
            raise Exception("Invalid Breed")
