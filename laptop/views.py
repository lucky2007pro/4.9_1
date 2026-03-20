from django.shortcuts import render, redirect
from .models import Laptop
# Create your views here.
def laptop_list(request):
    laptop = Laptop.objects.all()
    return render(request,'laptop.html',{'laptop':laptop})

#     brand
#     model
#     videocard
#     year
#     ram
#     cpu
#     disk
#     price
def add_laptop(request):
    if request.method == "POST":
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        year = request.POST.get('year')
        videocard = request.POST.get('videocard')
        ram = request.POST.get('ram')
        cpu = request.POST.get('cpu')
        disk = request.POST.get('disk')
        price = request.POST.get('price')
        book = Laptop(brand=brand, model=model, year=year, videocard=videocard, ram=ram, cpu=cpu, disk=disk, price=price)
        book.save()

        return redirect('/')

    return render(request, 'add_laptop.html')
