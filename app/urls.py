from django.urls import path
from. views import Home_Page, Todo_Create_view, Todo_Update_View, Todo_Delete_View

app_name = 'todo'

urlpatterns = [
    path('', Home_Page.as_view(), name='home'),
    path('create-todo', Todo_Create_view.as_view(), name='create-todo'),
    path('update-todo/<int:pk>/', Todo_Update_View.as_view(), name='update-todo'),
    path('delete-todo/<int:pk>/', Todo_Delete_View.as_view(), name='delete-todo'),
]