from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index,name="index"),
    path('index/',views.IndexView.as_view(),name="index"),
    path('',views.TodoView.as_view(),name="alltodo"),
    path('<int:todo_id>/',views.TodoDetailView.as_view(),name="todo_detail"),
]