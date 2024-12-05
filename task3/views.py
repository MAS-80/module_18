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

class Shop(TemplateView):
    template_name = ('shop.html')

class Basket(TemplateView):
    template_name = ('basket.html')