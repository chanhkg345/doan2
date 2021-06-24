from django.shortcuts import render
from django.http import HttpResponse
from .models import dienchinhsach
# Create your views here.




def index(request):
	return render(request,'dienchinhsach/dienchinhsach.html')

def danhsachdcs(request):
	danhsachdcs = dienchinhsach.objects.all()
	dcs = {'dcs':danhsachdcs}
	return render(request, 'dienchinhsach/dienchinhsach.html',dcs)




