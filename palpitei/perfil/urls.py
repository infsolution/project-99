from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),
 path('cadastro/', views.cadastro, name='cadastro'),
 path('login/',views.do_login, name='login'),
 path('logout/',views.do_logout, name='logout'),
 path('teste/',views.testeauth, name='teste'),
 #path('criar/<int:user_id>')
]