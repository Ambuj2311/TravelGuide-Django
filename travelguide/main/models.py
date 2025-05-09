from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='destinations/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    location = models.CharField(max_length=100)  # e.g. "Goa", "Kerala"
    category = models.CharField(max_length=50, choices=[
        ('beach', 'Beach'),
        ('mountain', 'Mountain'),
        ('heritage', 'Heritage'),
        ('spiritual', 'Spiritual'),
        ('wildlife', 'Wildlife'),
    ])
    tags = models.ManyToManyField('Tag', blank=True)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotels/')
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    amenities = models.ManyToManyField('Amenity', blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.destination.name}"

class Amenity(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    
    def __str__(self):
        return self.name

class SliderImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider/')
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    check_in = models.DateField()
    check_out = models.DateField()
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    special_requests = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.destination.name}"