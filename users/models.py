from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,PermissionsMixin,BaseUserManager
from .managers import CustomUserManager
import uuid

# class UserManager(BaseUserManager):
#     def create_user(self,email,password=None,**extra_fields):
#         if not email:
#             raise ValueError('Email alani gereklidir!')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self,email,password=None, **extra_fields):
#         '''
#             Super kullanici olusturuluyor
#         '''
#         extra_fields.setdefault('is_staff',True)
#         extra_fields.setdefault('is_superuser',True)
        
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Süper kullanıcı is_staff=True değerine sahip olmalıdır.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Süper kullanıcı is_superuser=True değerine sahip olmalıdır.')
        
#         return self.create_user(email,password,**extra_fields)
    
    
# class User(AbstractBaseUser,PermissionsMixin):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=30)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
    
#     objects = UserManager()
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name','last_name'] 
    
#     def __str__(self):
#         return self.email  
    
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'
        
        
class User(AbstractUser):
    id = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4,editable=False)
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(('email address'))
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.username
    