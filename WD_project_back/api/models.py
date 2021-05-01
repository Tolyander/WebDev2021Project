from django.db import models


class Category(models.Model):
    name = models.CharField('category', max_length=300)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Laptop(models.Model):
    name = models.CharField('name_laptops', max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField('price')
    rating = models.FloatField('rating')
    description = models.CharField('description', max_length=300)
    image = models.CharField('image', max_length=300)
    url = models.CharField('url', max_length=300)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'rating': self.rating,
            'description': self.description,
            'address': self.url,
            'image': self.image
        }


class Phone(models.Model):
    name = models.CharField('name_phones', max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField('price')
    rating = models.FloatField('rating')
    description = models.CharField('description', max_length=300)
    image = models.CharField('image', max_length=300)
    url = models.CharField('url', max_length=300)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'rating': self.rating,
            'description': self.description,
            'address': self.url,
            'image': self.image
        }


class Accessory(models.Model):
    name = models.CharField('name_accessories', max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField('price')
    rating = models.FloatField('rating')
    description = models.CharField('description', max_length=300)
    image = models.CharField('image', max_length=300)
    url = models.CharField('url', max_length=300)

    class Meta:
        verbose_name = 'Accessory'
        verbose_name_plural = 'Accessories'

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'rating': self.rating,
            'description': self.description,
            'address': self.url,
            'image': self.image
        }


class OfferedProduct(models.Model):
    name = models.CharField('name2', max_length=300)
    price = models.FloatField('price')
    company = models.CharField('company', max_length=300)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'company': self.company
        }


