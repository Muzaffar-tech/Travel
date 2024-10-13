from django.urls import path

from .views import HotelApiView, HotelCategoryApiView, VideoApiView, TurApiView

urlpatterns = [
    path('hotel/', HotelApiView.as_view()),
    path('hotel/<int:pk>/', HotelApiView.as_view()),
    path('hotel_category/', HotelCategoryApiView.as_view()),
    path('hotel_category/<int:pk>', HotelCategoryApiView.as_view()),
    path('video/', VideoApiView.as_view()),
    path('video/<int:pk>/', VideoApiView.as_view()),
    path('tur/', TurApiView.as_view()),
    path('tur/<int:pk>', TurApiView.as_view())
]
