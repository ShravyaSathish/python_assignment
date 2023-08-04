from django.db import models
import uuid
from enum import Enum
from django.utils.timezone import now
from .manager import UserManger
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role_choices =  (
         ('publisher', 'Publisher'),
        ('author', 'Author')
    )
    username = models.CharField(max_length=288)
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=288)
    role = models.CharField(max_length=10, choices=role_choices)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManger()

    def __str__(self):
        return self.email
    


# class Refresh_Token(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     refresh_token = models.TextField(unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     expiration_date = models.DateTimeField(default=now)

#     def __str__(self):
#  
#        return f"Refresh token for {self.user.email}"


class StatusChoices(Enum):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    REJECTED = 'rejected'

class ArticlesModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publisher = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='published_articles', null=True, blank=True)
    article_title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    file_url = models.ImageField(upload_to='articles/')
    status = models.CharField(max_length=20, choices=[(status.value, status.name) for status in StatusChoices])
    is_editted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.file_url.name}"
    


