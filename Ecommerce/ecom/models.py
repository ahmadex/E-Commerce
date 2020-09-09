
from django.db import models
# Create your models here.

class  Product(models.Model):
    product_name = models.CharField(max_length=256)
    product_price = models.IntegerField(default=0)
    category = models.CharField(max_length=256)
    sub_category = models.CharField(max_length=256)
    description = models.TextField()
    product_image = models.ImageField(default='')
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.product_name


class ContactUs(models.Model):
    name = models.CharField(max_length=256)
    phone_no = models.IntegerField(default=0)
    email = models.EmailField()
    query = models.TextField()


    def __str__(self):
        return self.name


class Order(models.Model):
    item_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    address = models.CharField(default="", max_length=256)
    city = models.CharField(default="",max_length=256)
    state = models.CharField(default="",max_length=256, null=True)
    zipcode = models.CharField(max_length=6)
    phone_no = models.CharField(default="", max_length=10)

    def __str__(self):
        return self.name

class OrderUpdate(models.Model):
    order_id = models.IntegerField(default='')
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:10] + '....'
