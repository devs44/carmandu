import datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.enums import Choices
from django.utils import timezone
# Create your models here.

LOCATION = (
    ('Kathmandu','Kathmandu'),
    ('Bhaktapur', 'Bhaktapur'),
    ('Lalitpur', 'Lalitpur'),
)

COLOR = (
    ('Red', 'Red'),
    ('White', 'Red'),
    ('Grey', 'Grey'),
)

YEAR = (
    ('2015','2015'),
    ('2016','2016'),
    ('2017','2017'),
    ('2018','2018'),
    ('2019','2019'),
)

GENDER = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
)

class DateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self, hard=False):
        if not hard:
            self.deleted_at = timezone.now()
            return super().save()
        else:
            return super().delete()

class Account(User):
    mobile = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    image = models.ImageField(upload_to='user')

    class Meta:
        verbose_name = ('Account')
        verbose_name_plural = ('Accounts')
        ordering = ['username']

    def __str__(self):
        return self.username

# Customer Model


class Customer(User):
    GENDER = (('Male', 'Male'),
              ('Female', 'Female'),
              ('Others', 'Others'),)
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices = GENDER)
    is_customer = models.BooleanField(default=False)

    class Meta:
        verbose_name = ('Customer')
        verbose_name_plural = ('Customers')
        ordering = ['-username']

    def __str__(self):
        return self.first_name



class Brand(DateTimeModel):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = ('Brand')
        verbose_name_plural = ('Brands')
        ordering = ['-title']

    def __str__(self):
        return self.title

class Model(DateTimeModel):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = ('Model')
        verbose_name_plural = ('Models')
        ordering = ['-title']

    def __str__(self):
        return self.title

class Type(DateTimeModel):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = ('Type')
        verbose_name_plural = ('Types')
        ordering = ['-title']

    def __str__(self):
        return self.title

class Category(DateTimeModel):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categorys')
        ordering = ['-title']

    def __str__(self):
        return self.title

class Features(DateTimeModel):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = ('Feature')
        verbose_name_plural = ('Features')
        ordering = ['-title']

    def __str__(self):
        return self.title

class Car(DateTimeModel):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    features = models.ForeignKey(Features, on_delete=models.CASCADE)
    location = models.CharField(max_length=200, choices=LOCATION)
    year = models.CharField(max_length=200, choices=YEAR)
    color = models.CharField(max_length=200, choices=COLOR)
    transmission = models.CharField(max_length=200)
    image = models.ImageField(upload_to='cars')
    price = models.PositiveIntegerField()
    description = RichTextField()
    is_on_sale = models.BooleanField("On Sale", default=False)
    is_on_rent = models.BooleanField("On Rent", default=False)
    is_featured = models.BooleanField("Featured", default=False)

    class Meta:
        verbose_name = ('Car')
        verbose_name_plural = ('Cars')
        ordering = ['-name']

    def __str__(self):
        return self.name

class CarImage(DateTimeModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars/images/')
    
    class Meta:
        verbose_name = ('CarImage')
        verbose_name_plural = ('CarImages')

    def __str__(self):
        return self.car.name

class About(DateTimeModel):
    image = models.ImageField(upload_to='about')
    description = RichTextField()

    class Meta:
        verbose_name = ('About')
        verbose_name_plural = ('Abouts')

    def __str__(self):
        return self.description

class Team(DateTimeModel):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team')

    class Meta:
        verbose_name = ('Team')
        verbose_name_plural = ('Teams')
        ordering = ['-name']

    def __str__(self):
        return self.name


class Services(DateTimeModel):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services')
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name = ('Service')
        verbose_name_plural = ('Services')
        ordering = ['-title']

    def __str__(self):
        return self.title


class ServicesVideo(DateTimeModel):
    video = models.FileField(upload_to='servicevideo')
    description = RichTextField()

    class Meta:
        verbose_name = ('ServicesVideo')
        verbose_name_plural = ('ServicesVideos')


    def __str__(self):
        return self.description

class Contact(DateTimeModel):
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    fax = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=200)

    class Meta:
        verbose_name = ('Contact')
        verbose_name_plural = ('Contacts')

    def __str__(self):
        return self.email
