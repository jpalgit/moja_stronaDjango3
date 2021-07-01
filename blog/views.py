from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post


def index(request):
    return HttpResponse("Tu indeks z bloga")


def lista_postow(request):

    lista = Post.opublikowane.all()
    paginator = Paginator(lista, 12)  # egzemplarz klasy Paginator,bierze z listy po 18 na każdej stronie
    page = request.GET.get('page')  # numer strony???
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # jeżeli zmienna page nie jest liczbą całkowitą
        posts = paginator.page(1)
    except EmptyPage:
        # jeżeli zmienna ma wartośc większą od numeru ostatniej strony->pobierz ostatnią strone
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html',
                  {'posts': posts,
                   'page': page})
# pobiera post o danym id, id_posta to zmienna formalna, może to być dowolna nazwa,
# ale taka sama jak w blog/urls.py
# 'id' to już nazwa pola z modelu (bazy)!


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             data_publikacji__year=year,
                             data_publikacji__month=month,
                             data_publikacji__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
