from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage,name="home"),
    path('create_link',views.link_create,name ="create_link"),
    path('edit_link/<int:id>',views.link_edit,name ="edit_link"),
    path('delete_link/<int:id>',views.link_delete,name ="delete_link"),
    path('<str:code>' , views.redirect_url,name = "redirect"),
    path('links/',views.links,name ="links"),
]