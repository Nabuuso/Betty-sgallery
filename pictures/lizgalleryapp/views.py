from django.shortcuts import render
from django.templatetags.static import static
from django.shortcuts import render
from django.http import Http404
from .models import Location, Image, Category
from django.core.exceptions import ObjectDoesNotExist




# Create your views here.
def index(request):
    images = Image.objects.all()
    location = Location.get_location()
    locations = Location.get_location()
    return render(request, 'index.html', {"images":images, "location": location, "locations": locations})


def search_images(request):
    locations = Location.get_location()
    if 'keyword' in request.GET and request.GET["keyword"]:
        search_term = request.GET.get("keyword")
        searched_images = Image.search_by_categ(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message,"images": searched_images, "locations": locations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message, "locations":locations})


def get_image(request, id):
        locations = Location.get_location()
        try:
            image = Image.objects.get(pk = id)
            print(image)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return render(request, "images.html", { "image":image,"locations":locations})
    
    
def location(request, location):
    images = Image.search_by_location(location)
    locations = Location.get_location()
    message = f"{location}"
    return render(request, 'locations.html', {"message":message, "images":images, "locations":locations})


def category(request, category):
    images = Image.get_by_category(category)
    category = Category.get_location()
    locations = Location.get_location()
    message = f"{category}"
    return render(request, 'category.html', {"message":message,"image":images, "locations":locations})


def navlocation(request):
    
    locations = Location.get_location()

    return render(request, 'navbar.html', {"locations": locations})