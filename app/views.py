from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def home(request):

    read = Read.objects.all()

    context = {
        'read':read
    }
    return render(request, 'index.html', context)


def add(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        read = Read(
            name = name,
            email = email,
            address = address,
            phone = phone,
        )

        read.save()
        return redirect('home')

    return render(request, 'index.html')

def edit(request):

    read = Read.objects.all()

    context = {
        'read':read
    }
    return render(request, 'index.html', context)


def update(request,id):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        read = Read(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone,
        )

        read.save()
        return redirect('home')

    return render(request, 'index.html')


def delete(request,id):

    read = Read.objects.filter(id = id)

    read.delete()

   

    return redirect('home')

   