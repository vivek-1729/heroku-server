from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), #if no extension is provided, then default to index
    path('<str:name>/draft/', views.draft, name='room'), #call the draft function, and pass the name of the person as an argument. For example, http://127.0.0.1:8000/Vivek/draft/
    #would call the draft function and pass in 'Vivek' as the argument for the name parameter. 
]