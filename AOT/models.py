from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class AOT(models.Model):
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name=models.CharField(max_length=64,help_text='Character name',default='AOT')
    description=models.TextField(default='description')
    img_url = models.TextField(default="NO Image")

    def __str__(self):
        return self.name
    # class Meta:
    #     ordering = ['name']

    # def get_absolute_url(self):
    #     return reverse('snack_detail', args=[str(self.id)])

        
        
        
