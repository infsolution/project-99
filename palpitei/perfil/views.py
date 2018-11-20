from django.shortcuts import render
from perfil.forms import UserModelForm
def index(request):
    return render(request, 'perfil/index.html')


def cadastro(request):
    form = UserModelForm(request.POST or None)
    context = {'form':form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'perfil/cadastro.html', context)
