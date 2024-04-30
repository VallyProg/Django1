import logging

from django.http import HttpResponse
from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

from .models import Order, Product

logger = logging.getLogger(__name__)

index_html = """<h1>Главная</h1>
<h3>И вот моя первая ступенька по созданию сайта!<br>Я вписываю первые предложения в историю этого сайта</h3>

"""

about_html = """<h1>О себе!</h1>
<h2> Меня зовут Михаил, мне 28 лет.</h2>
<p2>Я начинающий программист, и это мой первый сайт, так что не судите строго.</p2> """

def index(request):

    return HttpResponse(index_html)


def about_me(request):
    return HttpResponse(about_html)

def order_list(request):
    orders_last_week = Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=7))
    orders_last_month = Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=30))
    orders_last_year = Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=365))
    products = Product.objects.all().distinct()

    context = {
        'orders_last_week': orders_last_week,
        'orders_last_month': orders_last_month,
        'orders_last_year': orders_last_year,
        'products': products,
    }

    return render(request, 'orders/order_list.html', context)