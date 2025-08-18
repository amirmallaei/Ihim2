from django.urls import path
from books.views import HomeView

app_name = "books"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
]