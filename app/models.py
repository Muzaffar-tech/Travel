from django.db import models

# Create your models here.

class HotelCategory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='hotel/images/')
    price = models.IntegerField()
    stars = models.IntegerField()
    hotel_category = models.ForeignKey(HotelCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Video(models.Model):
    video = models.FileField()

    def __str__(self):
        return self.video.name


class Tur(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    video = models. ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

