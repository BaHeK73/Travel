from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from django import forms
from .models import Hotel, Room, Amenity
from Travel.apps.common.models import City

# Create your views here.

class HotelSearchForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=False, label='Город')
    date_from = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Дата заезда')
    date_to = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Дата выезда')
    guests = forms.IntegerField(min_value=1, initial=1, required=False, label='Гостей')
    stars = forms.ChoiceField(choices=[('', 'Любое')] + [(i, f'{i}★') for i in range(1, 6)], required=False, label='Звезды')
    min_price = forms.DecimalField(required=False, min_value=0, label='Цена от')
    max_price = forms.DecimalField(required=False, min_value=0, label='Цена до')
    amenities = forms.ModelMultipleChoiceField(queryset=Amenity.objects.all(), required=False, label='Удобства')
    rating = forms.FloatField(required=False, min_value=0, max_value=5, label='Рейтинг от')

class HotelSearchView(View):
    def get(self, request):
        form = HotelSearchForm(request.GET or None)
        return render(request, 'hotels/search.html', {'form': form})

class HotelListView(ListView):
    model = Hotel
    template_name = 'hotels/results.html'
    context_object_name = 'hotels'
    paginate_by = 12

    def get_queryset(self):
        qs = Hotel.objects.select_related('city').prefetch_related('amenities')
        form = HotelSearchForm(self.request.GET)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('city'):
                qs = qs.filter(city=data['city'])
            if data.get('stars'):
                qs = qs.filter(stars=data['stars'])
            if data.get('rating'):
                qs = qs.filter(rating__gte=data['rating'])
            if data.get('amenities'):
                for amenity in data['amenities']:
                    qs = qs.filter(amenities=amenity)
            if data.get('min_price') or data.get('max_price'):
                qs = qs.filter(rooms__is_available=True)
                if data.get('min_price'):
                    qs = qs.filter(rooms__price_per_night__gte=data['min_price'])
                if data.get('max_price'):
                    qs = qs.filter(rooms__price_per_night__lte=data['max_price'])
            qs = qs.distinct()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = HotelSearchForm(self.request.GET)
        return context

class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotels/detail.html'
    context_object_name = 'hotel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = self.object.rooms.filter(is_available=True)
        context['amenities'] = self.object.amenities.all()
        context['images'] = self.object.images.all()
        context['reviews'] = self.object.reviews.select_related('user').order_by('-created_at')[:5]
        return context
