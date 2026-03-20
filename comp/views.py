from django.shortcuts import render, redirect, get_object_or_404
from .models import Computer
from laptop.models import Laptop
# Create your views here.
#     year
#     brand
#     model
#     videocard
#     ram
#     cpu
#     disk
#     monitor
#     price
def add_computer(request):
    if request.method == "POST":
        computer = Computer(brand=request.POST.get('brand'),
                            model=request.POST.get('model'),
                            year=request.POST.get('year'),
                            videocard=request.POST.get('videocard'),
                            ram=request.POST.get('ram'),
                            cpu=request.POST.get('cpu'),
                            disk=request.POST.get('disk'),
                            monitor=request.POST.get('monitor'),
                            price=request.POST.get('price')
                            )
        computer.save()
        return redirect('/')
    return render(request, 'add_comp.html')

def home_page(request):
    computer = Computer.objects.all()
    laptop = Laptop.objects.all()
    return render(request, 'home_page.html', {'computer':computer, 'laptop':laptop})

def comp_list(request):
    computer = Computer.objects.all()
    return render(request,'comp.html',{'computer':computer})

def computer_info(request, pk):
    item = get_object_or_404(Computer, pk=pk)
    return render(request, 'info.html', {'item': item, 'type': 'Kompyuter'})


def delete_computer(request, pk):
    comp = get_object_or_404(Computer, pk=pk)
    if request.method == "POST":
        comp.delete()
        return redirect('/')
    return render(request, 'delete.html', {'item': comp})