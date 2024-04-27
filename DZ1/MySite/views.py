import logging

from django.http import HttpResponse

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