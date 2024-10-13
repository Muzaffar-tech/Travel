from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Hotel, HotelCategory, Video, Tur
from .serializers import HotelSerializer, HotelCategorySerializer, VideoSerializer, TurSerializer


# Create your views here.

class HotelApiView(APIView):
    def get(self, request: Request, pk=None):
        if not pk:
            hotels = Hotel.objects.all()
            return Response(HotelSerializer(hotels, many=True).data)
        try:
            hotel = Hotel.objects.get(pk=pk)
            return Response(HotelSerializer(hotel).data)
        except:
            return Response({'Error':'Hotel not found'})

    def post(self, request: Request):
        serializer = HotelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        hotel = serializer.save()

        return Response(HotelSerializer(hotel).data)

    def put(self, request: Request, pk=None):
        if not pk:
            return Response({"Error": "Method PUT not allowed"})
        try:
            hotel = Hotel.objects.get(pk=pk)
            serializer = HotelSerializer(hotel, data=request.data, partial=True, context={'request':request})
            serializer.is_valid(raise_exception=True)
            updated_hotel = serializer.update(hotel, serializer.validated_data)
            return Response(HotelSerializer(updated_hotel).data)

        except:
            return Response({"Error": "Hotel not found for update"})

    def delete(self, request: Request, pk=None):
        if not pk:
            return Response({"Error": "Method DELETE not allowed"})
        try:
            hotel = Hotel.objects.get(pk=pk)
            hotel.delete()
            return Response({"Message": "Hotel deleted successfully"})
        except:
            return Response({"Error": "Hotel not found"})


class HotelCategoryApiView(APIView):
    def get(self, request: Request, pk=None):
        if not pk:
            hotel_categories = HotelCategory.objects.all()
            return Response(HotelCategorySerializer(hotel_categories, many=True).data)
        try:
            hotel_category = HotelCategory.objects.get(pk=pk)
            return Response(HotelCategorySerializer(hotel_category).data)
        except:
            return Response({'Error':'Hotel Category not found'})

    def post(self, request: Request):
        serializer = HotelCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        hotel = serializer.save()

        return Response(HotelCategorySerializer(hotel).data)

    def put(self, request: Request, pk=None):
        if not pk:
            return Response({"Error": "Method PUT not allowed"})
        try:
            hotel_category = HotelCategory.objects.get(pk=pk)
            serializer = HotelCategorySerializer(hotel_category, data=request.data, partial=True, context={'request':request})
            serializer.is_valid(raise_exception=True)
            updated_hotel_category = serializer.update(hotel_category, serializer.validated_data)
            return Response(HotelCategorySerializer(updated_hotel_category).data)

        except:
            return Response({"Error": "Hotel Category not found for update"})

    def delete(self, request: Request, pk=None):
        if not pk:
            return Response({"Error": "Method DELETE not allowed"})
        try:
            hotel_category = HotelCategory.objects.get(pk=pk)
            hotel_category.delete()
            return Response({"Message": "Hotel Category deleted successfully"})
        except:
            return Response({"Error": "Hotel Category not found"})


class VideoApiView(APIView):
    def get(self, request: Request, pk=None):
        if not pk:
            videos = Video.objects.all()
            return Response(VideoSerializer(videos, many=True).data)
        try:
            video = Video.objects.get(pk=pk)
            return Response(HotelSerializer(video).data)
        except:
            return Response({'Error':'Video not found'})

    def post(self, request: Request):
        serializer = VideoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        video = serializer.save()

        return Response(VideoSerializer(video).data)

    def put(self, request: Request, pk=None):
        if not pk:
            return Response({"Error": "Method PUT not allowed"})
        try:
            video = Video.objects.get(pk=pk)
            serializer = VideoSerializer(video, data=request.data, partial=True, context={'request':request})
            serializer.is_valid(raise_exception=True)
            updated_video = serializer.update(video, serializer.validated_data)
            return Response(VideoSerializer(updated_video).data)

        except:
            return Response({"Error": "Video not found for update"})

    def delete(self, request: Request, pk=None):
        if not pk:
            return Response({"Error": "Method DELETE not allowed"})
        try:
            video = Video.objects.get(pk=pk)
            video.delete()
            return Response({"Message": "Video deleted successfully"})
        except:
            return Response({"Error": "Video not found"})


class TurApiView(APIView):
    def get(self, request: Request, pk=None):
        if not pk:
            turs = Tur.objects.all()
            print(request.data, '---------------------------******************')
            return Response(TurSerializer(turs, many=True).data)
        try:
            tur = Tur.objects.get(pk=pk)
            return Response(TurSerializer(tur).data)
        except:
            return Response({'Error':'Tur not found'})

    def post(self, request: Request):
        serializer = TurSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tur = serializer.save()

        return Response(TurSerializer(tur).data)

    def put(self, request: Request, pk=None):
        if not pk:
            return Response({"Error": "Method PUT not allowed"})
        try:
            tur = Tur.objects.get(pk=pk)
            serializer = TurSerializer(tur, data=request.data, partial=True, context={'request':request})
            serializer.is_valid(raise_exception=True)
            updated_tur = serializer.update(tur, serializer.validated_data)
            return Response(TurSerializer(updated_tur).data)

        except:
            return Response({"Error": "Tur not found for update"})

    def delete(self, request: Request, pk=None):
        if not pk:
            return Response({"Error": "Method DELETE not allowed"})
        try:
            tur = Tur.objects.get(pk=pk)
            tur.delete()
            return Response({"Message": "Tur deleted successfully"})
        except:
            return Response({"Error": "Tur not found"})

