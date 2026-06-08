from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage,name="home"),
    path('create_link',views.createlink,name ="create_link")
]