from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from .models import Todo 
from django.contrib.auth.decorators import login_required
from datetime import datetime 

# Create your views here.
@login_required
def homepage(request):
    # if request.method == 'GET':
    incomplete_todo = Todo.objects.filter(user_id = request.user.id,datecomplete__isnull = True)
    return render(request, 'index.html', {'incomplete_todo': incomplete_todo})
    # else: 
    #     return render(request, 'index.html',{'error': 'Invalid request made'})

@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else: 
        todo = Todo.objects.create(title = request.POST['title'], message = request.POST['message'], user_id = request.user.id)
        todo.save()
        return redirect('homepage')

@login_required
def completed(request):
    completed_todo = Todo.objects.filter(user_id = request.user.id,datecomplete__isnull = False)
    return render(request, 'completed.html', {'completed_todo': completed_todo})

@login_required
def update(request, todo_id):
    todo = get_object_or_404(Todo, id = todo_id)
    if todo.user_id == request.user.id: #check if the user is trying to edit own page
        if todo.datecomplete is None: 
            todo.datecomplete = datetime.now()
            todo.save()
            return redirect('homepage')
        else: 
            todo.datecomplete = None
            todo.save()
            return redirect('homepage')
    else:
        return redirect('homepage')