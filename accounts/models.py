from django.db import models
from django.contrib.auth.models import AbstractUser
# from .managers import CustomUserManager
from .sendmails import *


#creating an id for registration
def customer_generate_id():
    try:
        id=Registration.objects.count()
        if id is not None:
            return f"VA{2003+id}"
        else:
            return f"VA{2003}"
    except Exception as e:
        print(e)


#Registration table:
class Registration(AbstractUser):
    username=models.CharField(max_length=40,unique=True)
    id=models.CharField(max_length=10, default=customer_generate_id,primary_key=True,editable=False)
    first_name=models.CharField(max_length=60, null=True, blank=True) 
    last_name=models.CharField(max_length=60, null=True, blank=True)
    email=models.CharField(max_length=60,unique=True,verbose_name='email',null=True, blank=True)
    location=models.TextField(null=True,blank=True)
    gender=models.CharField(max_length=6,null=True,blank=True)
    profile_pic=models.ImageField(upload_to='image',null=True,blank=True)
    mobile_no=models.CharField(max_length=13)
    birth_place=models.CharField(max_length=30,null=True,blank=True)
    otp=models.IntegerField(default=0)
    occupation=models.CharField(max_length=40,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username + " " + self.email
    
    
    
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    # objects = CustomUserManager()

    class Meta:
        verbose_name_plural='user'


