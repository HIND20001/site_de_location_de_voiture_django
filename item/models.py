from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class types(models.Model):
    car_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.car_type
    

class Cars(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=20)
    rent_price = models.DecimalField(max_digits=8, decimal_places=2 , null = False , default='0.00')
    image = models.ImageField(upload_to='item_images', blank= False, null=False,default='no image')
    is_reserved = models.BooleanField(default=False)
    categories = models.ForeignKey(types, related_name='items', on_delete= models.CASCADE, default='1')

    class Meta:
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f"{self.year} {self.make} {self.model}" 

class Reservation(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


    
        