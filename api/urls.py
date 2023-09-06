from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('test/', views.testhello),
    path('new-user/', views.NewUser),
    path('edit-user/', views.EditUser),
    path('filter-users/', views.filterUsers),
    path('user-info/', views.userInfo),
    path('delete-user/', views.deleteUser),
    path('new-post/', views.NewPost),
    path('get-posts/', views.GetPosts),
    path('new-flashcard/', views.NewFlashcard),
    path('get-flashcards/', views.UserFlashcards),
    path('delete-flashcard/', views.DeleteFlashcard), 
]
