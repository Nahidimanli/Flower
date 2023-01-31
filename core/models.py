from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class AbstractBaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)


    class Meta:
        abstract = True

class Contact(AbstractBaseModel):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    is_check = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name


class Setting(AbstractBaseModel):
    logo = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    insta1 = models.CharField(max_length=100)
    insta2 = models.CharField(max_length=100)
    insta3 = models.CharField(max_length=100)
    insta4 = models.CharField(max_length=100)
    insta5= models.CharField(max_length=100)
    insta6 = models.CharField(max_length=100)


    def __str__(self):
     return "Settings"


class ContactUs(AbstractBaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    Message = models.TextField(max_length=100)
    is_check = models.BooleanField(default=False)

    def __str__(self):
     return "Conact_us"
        

    
class Gallery(AbstractBaseModel):
    flow1 = models.ImageField(upload_to= 'media/ Galery')
    flow2 = models.ImageField(upload_to= 'media/ Galery')
    flow3 = models.ImageField(upload_to= 'media/ Galery')
    flow4 = models.ImageField(upload_to= 'media/ Galery')
    flow5 = models.ImageField(upload_to= 'media/ Galery')
    flow6 = models.ImageField(upload_to= 'media/ Galery')
    flow7 = models.ImageField(upload_to= 'media/ Galery')
    flow8 = models.ImageField(upload_to= 'media/ Galery')


    def __str__(self):
     return "Gallery"


class About(AbstractBaseModel):
    about_flowers = models.CharField(max_length=10000)
    flow9 = models.ImageField(upload_to= 'media/About')
    flow10 = models.ImageField(upload_to= 'media/About')

    def __str__(self):
     return "About"



class Why(AbstractBaseModel):
    Why_chooses_us = models.CharField(max_length=1000)

    def __str__(self):
     return "Why"


class Customer(AbstractBaseModel):
    Customers_say1 = models.CharField(max_length=1000)
    Customers_say2 = models.CharField(max_length=1000)
    Customer1 = models.ImageField(upload_to= 'media/Customer')
    Customer2 = models.ImageField(upload_to= 'media/Customer')

    def __str__(self):
     return "Customer"


class Blog(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to= 'media/blog')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
       return self.title


class Advertisement(AbstractBaseModel):
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to= 'media/Advertisement')

    def __str__(self):
       return self.title


    


        