from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):    
    
    use_in_migrations = True    
    
    def create_user(self, email, nickname, password=None):        
        
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            email = self.normalize_email(email),            
            nickname = nickname        
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user     
    def create_superuser(self, email, username,password ):        
       
        user = self.create_user(            
            email = self.normalize_email(email),            
            nickname = nickname,            
            password=password        
        )        
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user

class User(AbstractBaseUser,PermissionsMixin):    
    
    objects = UserManager()
    
    email = models.EmailField(        
        max_length=255,        
        unique=True,    
    )    
    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True,
    )
    username = None
    # username = models.CharField(
    #     max_length=20,
    #     null=False,
    #     unique=True,
    # )
    profile_image = models.URLField(null=True)
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)     
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email
