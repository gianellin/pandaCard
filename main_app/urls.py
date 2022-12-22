from django.urls import path
from . import views


#used to define each route
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pandas/', views.pandas_index, name="index"),

]