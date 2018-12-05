from django.shortcuts import render,redirect
from perfil.forms import *
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



def do_login(request):
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'], password =  request.POST['password'])
		if user is not None:
			login(request,user)
			return redirect('/perfil/'+str(user.id), user)
	return render(request, 'perfil/login.html')

def do_logout(request):
	logout(request)
	return redirect('/login')

@login_required	
def go_perfil(request, perfil_id):
	perfil = User.objects.get(id=perfil_id)
	return render(request, 'perfil/perfil.html',{'perfil':perfil, 'contests':Contest.objects.all, 
		'tipies':Tips.objects.all, 'lotteries':Lottery.objects.all})

def palpitar(request, lottery_id):
	lottery = Lottery.objects.get(id=lottery_id)
	pass
	form = TenTipsModelForm()
	return render(request, 'perfil/palpitar.html', {'lottery':lottery, 'form':form, 'range': range(lottery.number_ten+1)})