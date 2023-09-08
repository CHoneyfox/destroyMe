from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/', views.delete, name="delete"),
    path('list/', views.List.as_view(), name="list"),
    path('<int:file_id>/details/', views.details, name="details"),
]
