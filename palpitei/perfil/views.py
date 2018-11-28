from django.shortcuts import render,redirect
from perfil.forms import UserModelForm
from perfil.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 

def index(request):
    return render(request, 'perfil/index.html', {'contests':Contest.objects.all})


def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'perfil/cadastro.html', context)
@login_required
def testeauth(request):
	return render(request, 'perfil/index.html', {'teste':'Pagina protegida por autenticação!'})


def do_login(request):
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'], password =  request.POST['password'])
		if user is not None:
			login(request,user)
			return redirect('/teste', user)
	return render(request, 'perfil/login.html')

def do_logout(request):
	logout(request)
	return redirect('/login')
