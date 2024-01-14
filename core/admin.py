from django.contrib import admin
from .models import (ProductReview, Product, ProductImage, Order, OrderItem, Payment )



admin.site.register([ProductReview, Product, ProductImage, Order, OrderItem, Payment])
