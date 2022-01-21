from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def notes_home(request):
    notes = Articles.objects.all()
    return render(request, 'notes/notes_home.html', {'notes': notes})


class NotesDetailView(DetailView):
    model = Articles
    template_name = 'notes/details_view.html'
    context_object_name = 'article'


class NotesDeleteView(DeleteView):
    model = Articles
    success_url = '/notes/'
    template_name = 'notes/notes-delete.html'


class NotesUpdateView(UpdateView):
    model = Articles
    success_url = '/notes/'
    template_name = 'notes/edit_note.html'

    form_class = ArticlesForm


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_home')
        else:
            error = 'Форма была не верной'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'notes/create.html', data)
