from django.db import models

# Create your models here.
# AbstractUser : Auth 관련 기본적인 필드를 제공
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass