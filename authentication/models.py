from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
import uuid
from django.contrib.auth.models import PermissionsMixin
# logo
# banner
# tagline

class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SiteBanner(BaseModel):
    logo = models.ImageField(upload_to='SiteImages/')
    banner = models.ImageField(upload_to='SiteImages/')
    tagline = models.CharField(max_length=2000,default="")


class User(BaseModel,AbstractBaseUser,PermissionsMixin):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30,unique=True)
	password = models.CharField(max_length=200)
	mobile = models.CharField(max_length=30 , blank=True, null=True)
	is_superuser = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	# is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['mobile','first_name','last_name']

	objects = UserManager()

	def __str__(self):
		return self.email