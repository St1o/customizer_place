from itertools import chain

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout

from shoes.models import ShoesInfo

from collection.models import CollectionInfo
from .form import AuthForm
from .models import *


@csrf_protect
def inscription(request):
    form = AuthForm()
    if request.method == 'POST':
        try:
            name = request.POST.get('username')
            telephone = request.POST.get('telephone')
            shop_name = request.POST.get('shop_name')
            shop_address = request.POST.get('shop_address')
            email = request.POST.get('email')
            shop = Shop(name=shop_name, address=shop_address)
            shop.save()
            owner = Owner(name=name, telephone=telephone, email=email, shop=shop)
            owner.save()
        except Exception:
            pass
        form = AuthForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('access')
    context = {'form': form}
    return render(request, 'owner/inscription.html', context)


@csrf_protect
def access(request):
    """
    le client se connect et est redirige vers sa boutik
    :param request:
    :return:
    """
    # TODO: le client doit voir que ses infos / admin voit tout
    form = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if request.POST.get('username') == 'admin':
                return redirect('all_shop_articles')
            return redirect('owner_list')
        return redirect('inscription')
    context = {'form': form}
    return render(request, 'owner/access.html', context)


@csrf_protect
@login_required(login_url='access')
def get_articles_by_owner(request):
    """
    obtenir tous les articles de la boutik (vue par les boutikiers)
    :param request:
    :return:
    """
    owner_name = request.user
    owner = Owner.objects.filter(name=owner_name)
    if owner:
        shoes = ShoesInfo.objects.filter(owner__name=owner_name)
        collections = CollectionInfo.objects.filter(owner__name=owner_name)
        articles_list = list(chain(shoes, collections))
        paginator = Paginator(articles_list, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'articles': page_obj,
            'shoes': shoes,
            'collections': collections
        }
        return render(request, 'owner/gallery.html', context)
    return redirect('/')


@csrf_protect
@login_required(login_url='access')
def get_all_shop_articles(request):
    """
    obtenir tous le nom des boutik (seul l'admin)
    :param request:
    :return:
    """
    if str(request.user) == 'admin':
        shops = Shop.objects.all()
        shoes = ShoesInfo.objects.all()
        collections = CollectionInfo.objects.all()
        articles_list = list(chain(shoes, collections))
        paginator = Paginator(articles_list, 9)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'articles': page_obj,
            'shops': shops,
            'shoes': shoes,
            'collections': collections
        }
        return render(request, 'owner/admin.html', context)
    return redirect('owner_list')


@csrf_protect
@login_required(login_url='access')
def get_all_owner(request):
    user = request.user
    shop = request.GET.get('shop')
    if shop is None:
        owner = Owner.objects.filter(name=user)
    else:
        owner = Owner.objects.filter(shop__name=shop)
    shops = Shop.objects.all()
    context = {'shops': shops, 'owner': owner}
    return render(request, 'owner/admin.html', context)


@csrf_protect
def quiter(request):
    logout(request)
    return redirect('/')


@csrf_protect
@login_required(login_url='access')
def get_collection_by_owner(request):
    """
    obtenir la collection pour chaque boutik (chak boutik voit ses chaussures)
    :param request:
    :return:
    """
    owner_name = request.user
    if owner_name == 'admin':
        articles_list = CollectionInfo.objects.all()
    else:
        articles_list = CollectionInfo.objects.filter(owner__name=owner_name)
    paginator = Paginator(articles_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'articles': page_obj,
    }
    return render(request, 'owner/collection_owner.html', context)


@login_required(login_url='access')
@csrf_protect
def get_shoes_by_owner(request):
    """
    chak boutik voit ses chaussures
    :param request:
    :return:
    """
    owner_name = request.user
    if owner_name == 'admin':
        articles_list = ShoesInfo.objects.all()
    else:
        articles_list = ShoesInfo.objects.filter(owner__name=owner_name)
    paginator = Paginator(articles_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'articles': page_obj,
    }
    return render(request, 'owner/shoes_owner.html', context)
