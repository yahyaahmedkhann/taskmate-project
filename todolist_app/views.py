from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user 
            instance.save()
        messages.success(request,("New Task Added!"))
        return redirect('todolist')
    else:     
        all_tasks = TaskList.objects.filter(manage=request.user).order_by('-created_at')
        paginator = Paginator(all_tasks, 8)
        page = request.GET.get("page")
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})
    
# Delete tasks
@login_required
def delete_task(request, task_id):
        task = TaskList.objects.get(pk=task_id)
        if task.manage == request.user:
            task.delete()
        else:
            messages.error(request,("Access Restricted, You Are Not Allowed."))            
        return redirect('todolist')
   
# Edit tasks 
@login_required
def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save() 
        
        messages.success(request,("Task Updated!"))
        return redirect('todolist')
    else:     
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})
 
@login_required    
def complete_task(request, task_id):
        task = TaskList.objects.get(pk=task_id)
        if task.manage == request.user:
            task.done = True
            task.save()
        else:
            messages.error(request,("Access Restricted, You Are Not Allowed."))
                
        return redirect(request.META.get('HTTP_REFERER', 'todolist'))

@login_required    
def pending_task(request,task_id):
        task = TaskList.objects.get(pk=task_id)
        task.done = False
        task.save()
        return redirect(request.META.get('HTTP_REFERER', 'todolist'))   
    
def index(request):
    context = {
        "index_text": "Welcome to Index Page",
        
    }
    return render(request, 'index.html', context)


# Create your views here.
def contact(request):
    context = {
        "contact_text": "Welcome to contact page",
        
    }
    return render(request, 'contact.html', context)

# Create your views here.
def about(request):
    context = {
        "about_text": "Welcome to about page",
        
    }
    return render(request, 'about.html', context)


from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import get_template

