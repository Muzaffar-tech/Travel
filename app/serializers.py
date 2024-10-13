from rest_framework import serializers

from .models import Hotel, HotelCategory, Video, Tur

class HotelSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Hotel
        fields = '__all__'
        depth = 1

class HotelCategorySerializer(serializers.Serializer):
    class Meta:
        model = HotelCategory
        fields = '__all__'

class VideoSerializer(serializers.Serializer):
    class Meta:
        model = Video
        fields = '__all__'

class TurSerializer(serializers.Serializer):
    class Meta:
        model = Tur
        fields = '__all__'
        depth = 2
