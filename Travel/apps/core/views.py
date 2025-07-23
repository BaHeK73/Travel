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


def home_view(request):
    cities = [
        {'img': '/static/img/istanbul.jpg', 'name': 'Стамбул, Турция'},
        {'img': '/static/img/sydney.jpg', 'name': 'Сидней, Австралия'},
        {'img': '/static/img/baku.jpg', 'name': 'Баку, Азербайджан'},
        {'img': '/static/img/male.jpg', 'name': 'Мале, Мальдивы'},
        {'img': '/static/img/paris.jpg', 'name': 'Париж, Франция'},
        {'img': '/static/img/ny.jpg', 'name': 'Нью-Йорк, США'},
        {'img': '/static/img/london.jpg', 'name': 'Лондон, Великобритания'},
        {'img': '/static/img/tokyo.jpg', 'name': 'Токио, Япония'},
        {'img': '/static/img/dubai.jpg', 'name': 'Дубай, ОАЭ'},
    ]
    reviews = [
        {'author': 'Ольга', 'text': 'Настоящее чувство общности', 'desc': 'Очень благодарна за помощь и поддержку персонала в это непростое время. Отдельное спасибо Кэти за помощь даже когда я была за границей. Всегда на связи, когда нужно.', 'img': '/static/img/review1.jpg'},
        {'author': 'Томас', 'text': 'Отличные условия. Чисто, современно, светло.', 'desc': 'Настоящее чувство общности! Очень благодарна за помощь и поддержку персонала в это непростое время. Отдельное спасибо Кэти за помощь даже когда я была за границей. Всегда на связи, когда нужно.', 'img': '/static/img/review2.jpg'},
        {'author': 'Элиот', 'text': 'Настоящее чувство общности', 'desc': 'Настоящее чувство общности! Очень благодарна за помощь и поддержку персонала в это непростое время. Отдельное спасибо Кэти за помощь даже когда я была за границей. Всегда на связи, когда нужно.', 'img': '/static/img/review3.jpg'},
    ]
    return render(request, 'home/home.html', {'cities': cities, 'reviews': reviews})