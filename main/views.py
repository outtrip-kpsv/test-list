from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
from .models import Worker, Department, Language
from .forms import AddWorkerForm, AddDepartmentForm, AddLanguageForm



def list_workers(request):
    workers = Worker.objects.all()
    context = {
        'current': 'workers',
        'workers': workers,
    }
    return render(request, template_name='main/list_workers.html', context=context)


def add_worker(request):
    if request.method == 'POST':
        form = AddWorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddWorkerForm()
    context = {
        'var': 'сотрудника',
        'form': form
    }
    return render(request, template_name='main/add_worker.html', context=context)


def edit_worker(request, id_worker):
    worker = get_object_or_404(Worker, id=id_worker)
    if request.method == 'POST':
        form = AddWorkerForm(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddWorkerForm(instance=worker)
    context = {

        'form': form
    }
    return render(request, template_name='main/add_worker.html', context=context)


def delete_worker(request, id_worker):
    worker = get_object_or_404(Worker, id=id_worker)
    worker.delete()
    return redirect('/')

def list_departments_languages(request):
    departments = Department.objects.all()
    languages = Language.objects.all()

    context = {
        'current': 'depandlangs',
        'departments': departments,
        'languages': languages
    }
    return render(request, template_name='main/list_departments.html', context=context)

def add_department(request):
    if request.method == 'POST':
        form = AddDepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddDepartmentForm()
    context = {
        'var': 'отдела',
        'form': form
    }
    return render(request, template_name='main/add_worker.html', context=context)

def add_language(request):
    if request.method == 'POST':
        form = AddLanguageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddLanguageForm()
    context = {
        'var': 'языка программирования',
        'form': form
    }
    return render(request, template_name='main/add_worker.html', context=context)