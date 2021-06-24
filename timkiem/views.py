from django.shortcuts import render
from django.http import HttpResponse
from .forms import formtimkiem
from quanlysinhvien.models import sinhvien
from dienchinhsach.models import dienchinhsach
from khoa.models import khoa

# Create your views here.
def index(request):
	return render(request,'timkiem/timkiem.html')
def timkiemmssv(request):
    if request.method == 'POST':
        timkiem = request.POST['timkiem']
        if timkiem != '':
            tkmssv = sinhvien.objects.filter(mssv__contains = timkiem)
            tkten = sinhvien.objects.filter(tensv__contains = timkiem)
            tkkhoa = sinhvien.objects.filter(makhoa__tenkhoa__contains= timkiem  )
            tkdcs = sinhvien.objects.filter(madcs__tendcs__contains=timkiem)
            return render(request, 'timkiem/kqtimkiem.html', {'tkmssv':tkmssv,'timkiem':timkiem,'tkten':tkten,'tkkhoa':tkkhoa,'tkdcs':tkdcs,'tk':timkiem})
        else:
            return HttpResponse("Hãy nhập j đó")