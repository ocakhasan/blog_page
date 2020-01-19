from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList, name='home'),
   path("<slug:slug>/", views.post_detail, name="post_detail"),
   path("about", views.about, name="about"),
   path("contact", views.contact, name="contact"),
]