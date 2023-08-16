from django.shortcuts import render, redirect
from .models import User, Fileu
from .forms import UserForm, FileuForm


def base_view(request):
    return render(request, 'base.html')


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'user_detail.html', {'user': user})


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})


def user_update(request, pk):
    user = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})


def user_delete(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return redirect('user_list')


def fileu_list(request):
    files = Fileu.objects.all()
    return render(request, 'fileu_list.html', {'files': files})


def fileu_detail(request, pk):
    file = Fileu.objects.get(pk=pk)
    return render(request, 'fileu_detail.html', {'file': file})


def fileu_create(request):
    if request.method == 'POST':
        form = FileuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fileu_list')
    else:
        form = FileuForm()
    return render(request, 'fileu_form.html', {'form': form})

def fileu_delete(request, pk):
    file = Fileu.objects.get(pk=pk)
    file.delete()
    return redirect('fileu_list')

# Create your views here.
