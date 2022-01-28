from django.db import models

from authapp.models import MyUser


class Article(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title



class Profile(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    TRANSGENDER = 'transgender'
    OTHERS = 'others'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (TRANSGENDER, 'Transgender'),
        (OTHERS, 'Others'),
    ]

    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio ...", max_length=300)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True)
    image = models.ImageField(upload_to='avatar', default="avatar/default.png")

    def __str__(self):
        return self.user.email
