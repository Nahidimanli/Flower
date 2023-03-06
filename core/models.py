from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.text import slugify
from django.urls import reverse

from  embed_video.fields  import  EmbedVideoField
#Create your models here.
class  tutorial(models.Model):
	tutorial_Title = models.CharField(max_length=200)
	tutorial_Body = models.TextField()
	tutorial_Video = EmbedVideoField()

	class  Meta:
		verbose_name_plural = "Tutorial"

	def  __str__(self):
		return  str(self.tutorial_Title) if  self.tutorial_Title  else  " "


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
    email = models.CharField(max_length=70)
   

    def __str__(self):
     return "Settings"


class ContactUs(AbstractBaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=100)
    is_check = models.BooleanField(default=True)


    
class Gallery(AbstractBaseModel):
    flow1 = models.ImageField(upload_to= 'media/ Galery')

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
    slug = models.SlugField(max_length=100, null=False, unique=True, db_index=True, editable=False, )

    def __str__(self):
       return self.title

    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blogdetails', kwargs={'slug': self.slug})


class Advertisement(AbstractBaseModel):
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to= 'media/Advertisement')

    def __str__(self):
       return self.title


    

class Catagory(AbstractBaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = ("Catagory")
    
    def get_absolute_url(self):
        return reverse('catagory', args=[self.name])


class Shop(AbstractBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    body = models.CharField(max_length=70)
    catagory = models.ForeignKey(Catagory, related_name="names", on_delete=models.CASCADE)
    image = models.ImageField(upload_to= 'media/blog')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField( null=False, blank=True, unique=True, db_index=True ,  editable=False)

    def __str__(self):
       return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)



        