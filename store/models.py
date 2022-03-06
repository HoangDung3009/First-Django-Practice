from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Customer
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=500, null=True, blank=True)
    birthday = models.DateField(null=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname


# Category
class Category(models.Model):
    cat_name = models.CharField(max_length=500, blank=True, null=True)
    cat_description = models.TextField(max_length=500, blank=True, null=True)
    isPublished = models.BooleanField(default=True, null=True, blank=True)
    createdAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cat_name


# Product
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    product_name = models.CharField(max_length=500, blank=True, null=True)
    price = models.FloatField(default=0.00, null=True)
    discount = models.FloatField(default=0.00, null=True)
    product_thumb = models.ImageField(null=True, blank=True)
    product_description = models.TextField(blank=True, null=True)
    unit_in_stock = models.IntegerField(null=True)
    isActive = models.BooleanField(null=True, default=True)
    createdAt = models.DateField(auto_now_add=True)
    modifiedAt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    @property
    def imageURL(self):
        try:
            url = self.product_thumb.url
        except:
            url = ''
        return url


# Order
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    ship_date = models.DateField(null=True)
    total_money = models.FloatField(null=True)
    isCancelled = models.BooleanField(default=True)
    isPaid = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


# Order details
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.FloatField(null=True)
    amount = models.IntegerField(null=True)
    discount = models.FloatField(null=True)
    create_date = models.DateField(auto_now_add=True)
    total_money = models.FloatField(null=True)


# Payment method
class PaymentMethod(models.Model):
    payment_method = models.CharField(null=True, blank=True, max_length=500)


# Payment
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    payment_mtd = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, blank=True, null=True)


# Shipping Address
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.TextField(null=True)
    city = models.CharField(null=True, max_length=500)
    country = models.CharField(max_length=500, null=True)
    zip_code = models.IntegerField(null=True)
    addedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
