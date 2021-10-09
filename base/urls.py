from django.urls import path
from django.views.generic.edit import DeleteView
from .views import TaskList
from .views import TaskDetail, TaskCreate, TaskUpdate, DeleteTask, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='task'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='taskdetail'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),
    path('edit-task/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('delete-task/<int:pk>/', DeleteTask.as_view(), name='task-delete'),

]
