from django.urls import path

from . import views

app_name = "dictionary"

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home),
    path('words_list/', views.words_list, name="list"),
    path('add_word/', views.AddWordView.as_view(), name="add_word")
]
