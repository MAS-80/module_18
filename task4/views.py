from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def main_page(request):
    title = "Главная страница"
    main_page = "Главная"
    shop = "Магазин"
    basket = "Корзина"

    context = {
        "title": title, "main_page": main_page, "shop": shop, "basket": basket,
    }
    return render(request, 'main_page.html', context)

def shop(request):
    game_dict = {'games': ['Ftomic Heart', 'Ciberpunk 2077', 'PayDay 77']}
    context = {'game_dict': game_dict,}
    return render(request, 'shop.html', context)

class Basket(TemplateView):
    template_name = ('basket.html')