from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator
from Components.models import Product

phone_regex = RegexValidator(regex=r'^\+?1?\d{10,11}$', message="Enter a valid Phone number. Don't Add +91 or 0")

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name=models.CharField(max_length=25)
    phone=models.CharField(validators=[phone_regex], max_length=10)     
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Quantity=models.PositiveIntegerField(default=1)
    Pid=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'
    

class Address(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    Name=models.CharField(max_length=30,blank=False,null=False)
    Phone=models.CharField(max_length=15,blank=False)
    Pincode=models.CharField(max_length=6,blank=False)
    State=models.CharField(max_length=20,blank=False)
    Street_Address=models.CharField(max_length=50,blank=False,null=False)
    Landmark=models.CharField(max_length=75,blank=True,null=False)

    def __str__(self):
        return f"{self.user}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Quantity=models.PositiveIntegerField(default=1)
    Pid=models.ForeignKey(Product,on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Time=models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f'{self.user}'

