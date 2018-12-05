from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),
 path('cadastro/', views.cadastro, name='cadastro'),
 path('login/',views.do_login, name='login'),
 path('logout/',views.do_logout, name='logout'),
 path('perfil/<int:perfil_id>', views.go_perfil, name='perfil'),
 path('palpitar/<int:lottery_id>', views.palpitar, name='palpitar'),
]