from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('about/', views.about_page, name="about"),
    path('category/', views.category_page, name="category"),
    path('single-post/<slug:slug>', views.SinglePostView.as_view(), name="single-post"),
    path('read-later/', views.ReadLaterView.as_view(), name="read-later")
]
