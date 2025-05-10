from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Destination, SliderImage, Hotel

def home(request):
    destinations = Destination.objects.all()
    slider_images = SliderImage.objects.all()
    
    search_query = request.GET.get('search', '')
    if search_query:
        destinations = destinations.filter(
            Q(name__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(tags__name__icontains=search_query)
        ).distinct()
        
        hotels = Hotel.objects.filter(
            Q(name__icontains=search_query) |
            Q(destination__name__icontains=search_query) |
            Q(destination__location__icontains=search_query) |
            Q(description__icontains=search_query)
        ).distinct()
    else:
        hotels = Hotel.objects.none()
    
    return render(request, 'main/index.html', {
        'destinations': destinations,
        'slider_images': slider_images,
        'hotels': hotels,
        'search_query': search_query,
    })


def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'main/destination_details.html', {'destination': destination})