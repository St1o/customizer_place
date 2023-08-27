from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_protect


from .models import *


def listing(request):
    articles_list = CollectionInfo.objects.filter(available=True)
    paginator = Paginator(articles_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'articles': page_obj, }
    return render(request, template_name='collection/list.html', context=context)


def detail(request, articles_id):
    article = get_object_or_404(CollectionInfo, id=articles_id)
    all_img = CollectionPhoto.objects.filter(detail=article)
    context = {"article": article, 'all_img': all_img}
    return render(request, 'collection/detail_collection.html', context)


@csrf_protect
@login_required(login_url='access')
def addCollections(request):
    owner_name = request.user
    owner = Owner.objects.filter(name=owner_name).first()
    if request.method == 'POST':
        data = request.POST
        photos = request.FILES.getlist('images')
        cover = request.FILES.get('cover')
        detail = CollectionInfo.objects.create(
            name=data['name'],
            owner=owner,
            description=data['description'],
            cover=cover,
            price=data['price']
        )
        for photo in photos:
            CollectionPhoto.objects.create(
                detail=detail,
                photo=photo
            )
        return redirect('owner_list')

    return render(request, 'collection/add.html')


@login_required(login_url='access')
@csrf_protect
def delete_by_id(request, articles_id):
    try:
        shoes = CollectionInfo.objects.get(id=articles_id)
    except CollectionInfo.DoesNotExist as e:
        return redirect('/')
    if request.method == 'GET':
        shoes.delete()
        return redirect('owner_list')
    return redirect('owner_list')


# def search(request):
#     query = request.GET.get('query')
#     if not query:
#         articles = Collection.objects.all()
#     else:
#         # title contains the query is and query is not sensitive to case.
#         articles = Collection.objects.filter(name__icontains=query)
#     if not articles.exists():
#         articles = Collection.objects.filter(description__icontains=query)
#     name = "Résultats pour la requête %s" % query
#     context = {
#         'articles': articles,
#         'name': name
#     }
#     return render(request, 'collection/search.html', context)
