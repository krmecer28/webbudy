from django.contrib import admin
from django.urls import path
from . import views

app_name = "webtemplates"

urlpatterns = [
    path('addtemplate/', views.addTemplate, name="addtemplate"),
    path('', views.templates, name="templates"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('delete/<int:id>', views.deleteTemplate, name="delete"),
    path('uploadimages/<int:id>', views.uploadImages, name="uploadimages"),
    path('template/<int:id>', views.detail, name="detail"),
]