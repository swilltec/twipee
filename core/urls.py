from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('tags/<str:tag>', views.TagsView.as_view(), name="tags"),
]
