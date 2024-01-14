from django.db import models
from accounts import models as usermodel


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_image')
    alt = models.CharField(max_length=20)
    

    def __str__(self) -> str:
        return self.image.url
    

class Product(models.Model):

    CATEGORY = (
        ('fresh fruit', 'fresh fruit'),
        ('vegetables', 'vegetables'),
        ('cooking', 'cooking'),
        ('snacks', 'snacks'),
        ('beverages', 'beverages'),
        ('beauty & health', 'beauty & health'),
        ('bread & Bakery', 'bread & Bakery')
    )


    name = models.CharField(max_length = 200)
    sku = models.PositiveIntegerField()
    sale_price = models.DecimalField(decimal_places = 2, max_digits = 10)
    discount_price = models.DecimalField(decimal_places = 2, max_digits = 10)
    description = models.TextField()
    brand = models.ImageField(upload_to='product_brand')
    category = models.CharField(max_length = 20, choices = CATEGORY)
    # tags = models.ManyToManyFiel
    color = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ManyToManyField(ProductImage, related_name='product_image')

    def __str__(self):
        return self.name
    

class ProductReview(models.Model):
    reviewer = models.ForeignKey(usermodel.CUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    ratings = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    

class Order(models.Model):

    STATUS = (
        ('pending', 'pending'),
        ('shipped', 'shipped'),
        ('delivered', 'delivered')
    )

    user = models.ForeignKey(usermodel.CUser, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # payment method
    # transaction id

