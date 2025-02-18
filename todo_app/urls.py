from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index,name="index"),
    path('',views.IndexView.as_view(),name="index"),
    path('alltodo/',views.TodoView.as_view(),name="alltodo"),
]