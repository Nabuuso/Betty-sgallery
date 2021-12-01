from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http.response import Http404

# Create your models here.
# class Image(models.Model):
#     caption=models.CharField(max_length=50)
#     Image=models.ImageField(upload_to="img/%y")
#     location = models.CharField(max_length= 100, blank =True)
    
#     def save_Image(self):
#         self.save()
    
#     def delete_Image(self):
#         self.delete()
        
#     @classmethod
#     def get_images(cls):
#         images = cls.objects.all()
#         return images
    
#     def __str__(self):
#         return self.caption
    
class Location(models.Model):
    location = models.CharField(max_length= 100, blank =True)
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations
    
    def __str__(self):
        return self.location
    
    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
        
class Category(models.Model):
    category = models.CharField(max_length= 150)
    
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
        
    @classmethod
    def get_category(cls):
        categories = cls.objects.all()
        return categories
    
    @classmethod
    def search_by_category(cls, search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images
    
    def __str__(self):
        return self.category
   
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    
class Image(models.Model):
    image_name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    image_file = models.ImageField(upload_to = 'images/', default='images/beagle.jpg', null=True)
    post = models.TextField(null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
       
    
    @classmethod
    def search_by_categ(cls, search_term):
        images = cls.objects.filter(category__category__icontains=search_term)
        return images
    
    @classmethod
    def search_by_location(cls, location):
        images = cls.objects.filter(location__location=location)
        return images
    
    @classmethod
    def get_by_category(cls, category):
        images = cls.objects.filter(category__category=category)
        return images
    
    @classmethod
    def get_image(request, id):
        locations = Location.get_location()
        try:
            image = Image.objects.get(pk = id)
            print(image)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return image
    
    def __str__(self):
        return self.image_name
    
    class Meta:
        ordering = ['image_name']
        verbose_name = 'My image'
        verbose_name_plural = 'Images'
        

        
