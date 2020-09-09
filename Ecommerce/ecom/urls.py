from django.urls import path
from . import views

app_name = 'ecom'

urlpatterns = [

    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('product/<str:pk>',views.product, name='product'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('checkout', views.checkout, name='checkout'),
    path('tracker', views.tracker, name='tracker'),
    path('handlequest', views.handlerequest, name='handlerequest'),



]
