from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('search', views.search, name='search'),
    path('newpage', views.newPage, name='newPage'),
    path('randomPage', views.randomPage, name='randomPage'),
    path('wiki/<str:title>', views.title, name='title'),
]
