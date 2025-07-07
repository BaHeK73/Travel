from django.urls import path
from .views import HotelSearchView, HotelListView, HotelDetailView

app_name = 'hotels'

urlpatterns = [
    path('search/', HotelSearchView.as_view(), name='search'),
    path('results/', HotelListView.as_view(), name='results'),
    path('<int:pk>/', HotelDetailView.as_view(), name='detail'),
] 