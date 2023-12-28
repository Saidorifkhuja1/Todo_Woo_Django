from django.urls import path
from .views import TaskListView, TaskDetailView, CurrentTasksView, CompletedTasksView, UserLoginView, UserSignupView, HomeView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('current-tasks/', CurrentTasksView.as_view(), name='current-tasks'),
    path('completed-tasks/', CompletedTasksView.as_view(), name='completed-tasks'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('signup/', UserSignupView.as_view(), name='user-signup'),
]