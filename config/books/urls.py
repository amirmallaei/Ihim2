from django.urls import path
from books.views import HomeView, BookDetailView

app_name = "books"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('detail/<uuid:pk>/', BookDetailView.as_view(), name='details')
]