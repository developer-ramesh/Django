from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    product_text = models.CharField(max_length=200)
    product_desc = models.TextField()
    pub_date = models.DateTimeField('date published')


class Menu(models.Model):
    menu_name = models.CharField(max_length=100)
    menu_desc = models.TextField()
    menu_pic = models.ImageField(upload_to='static/uploads/')
    menu_price = models.DecimalField(max_digits=8, decimal_places=2)
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def image(self):
            return '<img src="/%s"  width="50" height="50" />' % self.menu_pic
    image.allow_tags = True
