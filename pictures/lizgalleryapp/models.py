from django.db import models

# Create your models here.
class Image(models.Model):
    caption=models.CharField(max_length=50)
    Image=models.ImageField(upload_to="img/%y")
    
    def __str__(self):
        return self.caption
        
