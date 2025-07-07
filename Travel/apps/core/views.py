from django.shortcuts import render
from django.views.generic import TemplateView
from Travel.apps.common.models import City
from Travel.apps.reviews.models import HotelReview


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Выбираем 8 популярных городов (можно заменить на фильтр по популярности)
        context['popular_cities'] = City.objects.select_related('country')[:8]
        context['latest_reviews'] = HotelReview.objects.select_related('user', 'hotel').order_by('-created_at')[:3]
        return context