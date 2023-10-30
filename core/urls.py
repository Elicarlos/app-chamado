from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboad/', views.dasboard, name='dashboard'),
    path("cad-produtos/",views.cadastro_produto ,name="cad-produto"),
    path('cad-funcionario/', views.cadastro_funcionario, name='cad-funcionario'),
    path('chamados/', views.chamados, name='abrir-chamados'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
