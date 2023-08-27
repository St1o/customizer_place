import time
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from .models import *
from collection.models import CollectionInfo
from client.models import Client


def added(request):
    context = {}
    return render(request, 'orders/added.html', context)


def backet(request, articles_id):
    client_name = request.user
    client = Client.objects.filter(name=client_name).first()
    if client:
        if ShoesInfo.objects.filter(id=articles_id).exists():
            shoes = ShoesInfo.objects.get(id=articles_id)
            Orders.objects.create(
                articles_name=shoes.name,
                articles_price=shoes.price,
                articles_photo=shoes.cover,
                name=client,
            )
            return redirect('shoes')

        if CollectionInfo.objects.filter(id=articles_id).exists():
            collections = CollectionInfo.objects.get(id=articles_id)
            Orders.objects.create(
                articles_name=collections.name,
                articles_price=collections.price,
                articles_photo=collections.cover,
                name=client,
            )
            return redirect('collection')
    return redirect('access_client')


@csrf_protect
def achat(request):
    client_name = request.user
    client = Client.objects.filter(name=client_name).first()
    if client:
        qs = Orders.objects.filter(name=client).order_by('created_at').values("articles_name", "articles_price", "id")
        tot = 0
        indx = []
        for price in qs:
            tot += int(price['articles_price'])
        for i in range(len(qs)):
            indx.append(i + 1)
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        context = {"date": dt, "total": tot, "qs": qs, "client": client}
        return render(request, 'orders/achats.html', context)

    return redirect('access_client')


@login_required(login_url='access')
@csrf_protect
def delete_by_uid(request, pk):
    try:
        orders = Orders.objects.get(id=pk)
    except Orders.DoesNotExist as e:
        return redirect('achat')
    if request.method == 'GET':
        orders.delete()
        return redirect('achat')
    return redirect('achat')


def paiement(request):
    client_name = request.user
    client = Client.objects.filter(name=client_name).first()
    if client:
        qs = Orders.objects.filter(name=client).order_by('created_at').values("articles_name", "articles_price", "id", )
        tot = 0
        for price in qs:
            tot += int(price['articles_price'])
        context = {"total": tot, "qs": qs, "name": client}
        return render(request, 'orders/paiement.html', context)

    return redirect('access_client')


def after_paiement(request):
    name = request.user
    client = Client.objects.filter(name=name).first()
    if client:
        qs = Orders.objects.filter(name=client).order_by('created_at').values("articles_name", "articles_price", "id", )
        tot = 0
        for price in qs:
            tot += int(price['articles_price'])
        list_art = []
        for art in qs:
            list_art.append(art["articles_name"])
        Commandes.objects.create(
            total=tot,
            products=list_art,
            name=client
        )
        time.sleep(5)
        orders = Orders.objects.filter(name=name).all()
        if request.method == 'GET':
            orders.delete()
            return redirect('allcmd')
    return redirect('/')


def allCommades(request):
    name = request.user
    qs = Commandes.objects.filter(name=name).values("products", "total", "id", )
    context = {"qs": qs}
    return render(request, 'orders/allCommandes.html', context)


@login_required(login_url='access')
@csrf_protect
def delete_by_uid_commandes(request, pk):
    try:
        cmd = Commandes.objects.get(id=pk)
    except Orders.DoesNotExist as e:
        return redirect('allcmd')
    if request.method == 'GET':
        cmd.delete()
        return redirect('allcmd')
    return redirect('achat')
