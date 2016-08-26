from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext

from .forms import TaskForm

def home(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm()

    context = RequestContext(request, {
        'form':TaskForm
        })
    return render(
        request,
        'mvp/Tradester.html',
        context
    )
