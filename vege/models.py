from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=10)
    des=models.TextField()
    image=models.ImageField(upload_to='recipe')
    recipe_view_count=models.IntegerField(default=1)

