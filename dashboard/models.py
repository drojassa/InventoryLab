from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY= (
    ('Osciladores','Osciladores'),
    ('Cinemática','Cinemática'),
    ('Dinámica','Dinámica'),
)

class Material(models.Model):
    name = models.CharField(max_length=100, null= True) 
    category = models.CharField(max_length=20, choices=CATEGORY ,null= True)
    quantity = models.PositiveIntegerField(null =True)

    def __str__(self):
        return f'{self.name}-{self.quantity}'
    
    class Meta:
        verbose_name_plural = 'Material'

class Pedido(models.Model):
    material= models.ForeignKey(Material, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(User, models.CASCADE, null = True)
    pedido_quantity= models.PositiveBigIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.material} ordered  by {self.staff.username}'
    class Meta:
        verbose_name_plural = 'Pedido'
