from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class UserProfileModel(AbstractUser):
    phone_number = models.CharField(
        null=True,
        blank=True,
        max_length=12
    )

    is_dealer = models.BooleanField(
        default=False
    )

    interested_in_stocking = models.BooleanField(
        default=False
    )

    is_consumer = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.email


class CompanyModel(models.Model):
    company_name = models.CharField(max_length=255),
    company_number = models.CharField(max_length=12),
    company_type = models.CharField(max_length=128),
    address = models.CharField(max_length=512),
    city = models.CharField(max_length=128),
    country = models.CharField(max_length=128),
    post_code = models.CharField(max_length=128)
    owner = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name


class NewsModel(models.Model):
    news_text = models.TextField(
    )

    created_at = models.DateTimeField(
        default=timezone.now
    )
    image = models.ImageField(upload_to='NewsImages', blank=True)


class CollectionModel(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(blank=True, max_length=2048)
    image = models.ImageField(upload_to='CollectionsImages', blank=True)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(blank=True, max_length=2048)
    image = models.ImageField(upload_to='ProductTypesImages', blank=True)
    collection = models.ForeignKey(CollectionModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    IN_STOCK = 'In Stock'
    SOLD_OUT = 'Sold Out'
    AVAILABILITY_CHOICES = (
        (IN_STOCK, 'In Stock'),
        (SOLD_OUT, 'Sold Out'),
    )
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='ProductsImages', blank=True)
    product_code = models.CharField(blank=False, max_length=20)
    size = models.CharField(max_length=128)
    availability = models.CharField(
        choices=AVAILABILITY_CHOICES, max_length=10
    )
    weight = models.CharField(max_length=128)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    material = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.name
