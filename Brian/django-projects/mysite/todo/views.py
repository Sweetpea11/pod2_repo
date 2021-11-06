from django.shortcuts import render
from .models import Todo
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TodoForm
from .models import Note
from .forms import NoteForm

# Create your views here.
def todo(request):
    if request.method == 'GET':
        # tasks is our QuerySet of Todo objects
        tasks = Todo.objects.all()
        # one instance of the TodoForm class
        form = TodoForm()
        return render(request = request, template_name = 'list.html', context = {'tasks': tasks, 'form':form})
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            # add new Todo object to Queryset
            Todo.objects.create(task=task)
            return HttpResponseRedirect(reverse('todo'))

def task(request, task_id):
    if request.method == 'GET':
        # looking up a specific Todo object
        todo = Todo.objects.get(pk=task_id)
        # a form, prepopulate the character field with the name of task
        form = TodoForm(initial = {'task': todo.task})
        return render(request=request, template_name='details.html', context = {'form':form, 'task_id':task_id})

    if request.method == 'POST':
        if 'save' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                task = form.cleaned_data['task']
                # update task attribute of the task of the correct task_id to match user input
                Todo.objects.filter(pk=task_id).update(task=task)
        if 'complete' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                task = form.cleaned_data['task']
                Todo.objects.filter(pk=task_id).update(completed=True)
                return HttpResponseRedirect(reverse('todo'))
        elif 'delete' in request.POST:
            Todo.objects.filter(pk=task_id).delete()
        return HttpResponseRedirect(reverse('todo'))

def note(request):
    if request.method == 'GET':
        # notes is our QuerySet of Todo objects
        notes = Note.objects.all().order_by('note_id')
        # one instance of the NoteForm class
        form = NoteForm()
        return render(request = request, template_name = 'note.html', context = {'notes' : notes, 'form' : form})
        
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.cleaned_data['note']
            # add new Note object to Queryset
            Note.objects.create(note_text=note)
        return HttpResponseRedirect(reverse('note'))