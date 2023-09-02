from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout


from .form import AuthForm
from .models import *


@csrf_protect
def inscription(request):
    form = AuthForm()
    if request.method == 'POST':
        try:
            name = request.POST.get('username')
            telephone = request.POST.get('telephone')
            email = request.POST.get('email')
            client = Client(name=name, telephone=telephone, email=email)
            client.save()
        except Exception:
            pass
        form = AuthForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('access_client')
    context = {'form': form}
    return render(request, 'client/inscription.html', context)


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
        client = authenticate(username=username, password=password)
        if client:
            login(request, client)
            return redirect('/')
        return redirect('inscription_client')
    context = {'form': form}
    return render(request, 'client/access.html', context)


@csrf_protect
def quiter(request):
    logout(request)
    return redirect('/')
