from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    code = models.CharField(max_length=254)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.code

    def get_name(self):
        return self.name

class Subcategory(models.Model):

    class Meta:
        verbose_name_plural = 'Subcategories'

    code = models.CharField(max_length=254)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.code

    def get_name(self):
        return self.name

class Subscription_Type(models.Model):

    code = models.CharField(max_length=254)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.code

    def get_name(self):
        return self.name


class Sizes(models.Model):

    class Meta:
        verbose_name_plural = 'Sizes'

    code = models.CharField(max_length=254)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.code

    def get_name(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    subcategory = models.ForeignKey('Subcategory', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    code = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    subscription = models.BooleanField(default=False, null=True, blank=True)
    subscription_type = models.ManyToManyField('Subscription_Type')
    size = models.ManyToManyField('Sizes')
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True,
                                 blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    colour = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product_Subscription(models.Model):

    code = models.CharField(max_length=254)
    product = models.ForeignKey('Product', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    subscription_type = models.ForeignKey('Subscription_Type', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    size = models.ForeignKey('Sizes', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    quantity_available = models.DecimalField(max_digits=6, decimal_places=0, null=True,
                                 blank=True)

    def __str__(self):
        return self.code

    def get_name(self):
        return self.name