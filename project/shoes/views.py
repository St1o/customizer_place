from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import *


def index(request):
    return render(request, template_name='includes/index.html')


def listing(request):
    articles_list = ShoesInfo.objects.filter(available=True)
    paginator = Paginator(articles_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'articles': page_obj, }
    return render(request, template_name='shoes/shoes.html', context=context)


def detail(request, articles_id):
    article = get_object_or_404(ShoesInfo, id=articles_id)
    all_img = ShoesPhoto.objects.filter(detail=article)
    context = {"article": article, 'all_img': all_img}
    return render(request, 'shoes/courousel.html', context)


@login_required(login_url='access')
@csrf_protect
def addShoes(request):
    owner_name = request.user
    owner = Owner.objects.filter(name=owner_name).first()
    if request.method == 'POST':
        data = request.POST
        photos = request.FILES.getlist('images')
        cover = request.FILES.get('cover')
        detail = ShoesInfo.objects.create(
            name=data['name'],
            owner=owner,
            description=data['description'],
            cover=cover,
            price=data['price']
        )
        for photo in photos:
            ShoesPhoto.objects.create(
                detail=detail,
                photo=photo
            )

        return redirect('owner_list')

    return render(request, 'shoes/add.html')


def search(request):
    query = request.GET.get('query')
    if not query:
        articles = ShoesInfo.objects.all()
    else:
        # title contains the query is and query is not sensitive to case.
        articles = ShoesInfo.objects.filter(name__icontains=query)
    if not articles.exists():
        articles = ShoesInfo.objects.filter(description__icontains=query)
    name = "Résultats pour la requête %s" % query
    context = {
        'articles': articles,
        'name': name
    }
    return render(request, 'shoes/search.html', context)


def contact(request):
    context = {"test": "test"}
    return render(request, template_name='shoes/contact.html', context=context)


def listing_shoes(request):
    articles_list = ShoesInfo.objects.filter(available=True)
    paginator = Paginator(articles_list, 3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    context = {
        'articles': articles,
        'paginate': True
    }
    return render(request, template_name='shoes/shoes.html', context=context)


@login_required(login_url='access')
@csrf_protect
def delete_by_id(request, articles_id):
    try:
        shoes = ShoesInfo.objects.get(id=articles_id)
    except ShoesInfo.DoesNotExist as e:
        return redirect('owner_list')
    if request.method == 'GET':
        shoes.delete()
        return redirect('owner_list')
    return redirect('owner_list')


@login_required(login_url='access')
def update_shoes(request, pk):
    if request.method == 'POST':
        data = request.POST
        photos = request.FILES.getlist('images')
        cover = request.FILES.get('cover')
        detail = ShoesInfo.objects.filter(id=pk).update(
            name=data['name'],
            description=data['description'],
            cover=cover,
            price=data['price']
        )

        for photo in photos:
            ShoesPhoto.objects.filter(id=pk).update(
                detail=detail,
                photo=photo
            )

        return redirect('owner_list')

    return render(request, 'shoes/add.html')
