from django.shortcuts import render, get_object_or_404, redirect
from .forms import CategoryForm, NewsForm
from .models import News


def home(request):
    news_list = News.objects.all()
    return render(request, 'home.html', {'news_list': news_list})


def news_details(request, id):
    news_item = get_object_or_404(News, id=id)
    return render(request, 'news_details.html', {'news_item': news_item})


def categories_form(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            return redirect('home-page')
    else:
        form = CategoryForm()

    return render(request, 'categories_form.html', {'form': form})


def news_form(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = NewsForm()

    return render(request, 'news_form.html', {'form': form})
