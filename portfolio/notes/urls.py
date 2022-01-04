from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_home, name='notes_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NotesDetailView.as_view(), name='notes-detail'),
    path('<int:pk>/update', views.NotesUpdateView.as_view(), name='notes-update'),
    path('<int:pk>/delete', views.NotesDeleteView.as_view(), name='notes-delete')
]
