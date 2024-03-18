from django.urls import path

from my_site.blog import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]