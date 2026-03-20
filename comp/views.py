from django.shortcuts import render, redirect
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