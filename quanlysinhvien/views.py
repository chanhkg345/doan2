from django.shortcuts import render
from django.http import HttpResponse
from .models import sinhvien
from khoa.models import khoa
from dienchinhsach.models import dienchinhsach
from .forms import thongkesvkh,thongkesvhp,thongkesvqq,thongkesvdcs,thongketc,thongketchk,thongkediemhp,tktcmax
from hocphan.models import hocphan,thamgiahocphan,hocky
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Avg, Count, Min, Sum, Max

# Create your views here.



def index(request):
	return render(request,'quanlysinhvien/trangchu.html')

def trangchu(request):
	result1 = sinhvien.objects.all().aggregate(ketqua=Count('mssv'))
	sv = result1['ketqua']
	result2 = dienchinhsach.objects.all().aggregate(ketqua=Count('tendcs'))
	dcs = result2['ketqua']
	result3 = khoa.objects.all().aggregate(ketqua=Count('tenkhoa'))
	kh = result3['ketqua']
	result4 = hocphan.objects.all().aggregate(ketqua=Count('tenhp'))
	hp = result4['ketqua']
	return render(request, 'quanlysinhvien/trangchu.html',{'sv':sv,'dcs':dcs,'kh':kh,'hp':hp})

def danhsachsv(request):
	danhsachsv = sinhvien.objects.all()
	sv = {'sv':danhsachsv}
	return render(request, 'quanlysinhvien/sinhvien.html',sv)

def danhsachhp(request):
    danhsachhp = hocphan.objects.all()
    hp = {'hp': danhsachhp}
    return render(request, 'quanlysinhvien/hocphan.html', hp)

def danhsachdcs(request):
    danhsachdcs = dienchinhsach.objects.all()
    dcs = {'dcs': danhsachdcs}
    return render(request, 'quanlysinhvien/dienchinhsach.html', dcs)

def chitietsv(request,mssv):
	ctsv = sinhvien.objects.filter(mssv = mssv)
	tghp = thamgiahocphan.objects.filter(masv__mssv=mssv)
	hk = hocky.objects.all()
	return render(request, 'quanlysinhvien/chitietsinhvien.html',{'ct': ctsv,'tghp':tghp,'hk':hk})
def chitietkhoa(request,tenkhoa):
	ctkh = sinhvien.objects.filter(makhoa__tenkhoa=tenkhoa)
	return render(request, 'quanlysinhvien/kqthongke.html', {'temp': ctkh})

def thongke(request):
    return render(request,'quanlysinhvien/thongke.html',{'tk1':thongkesvkh,'tk2':thongkesvdcs,'tk3':thongkesvhp,'tk4':thongkesvqq,'tk5':thongkediemhp})

def thongkediem(request):
	return render(request, 'quanlysinhvien/thongkediem.html',{'tk1': thongkesvhp,'tk2': thongkediemhp})

def thongketinchi(request):
    return render(request,'quanlysinhvien/thongketinchi.html',{'tk1':thongketc,'tk2':thongketchk,'tk3':tktcmax})

def kqthongkekh(request):
	if request.method == 'POST':
		thongke = thongkesvkh(request.POST)
		if thongke.is_valid():
			kh = thongke.cleaned_data['khoa']
			tkkhoa = sinhvien.objects.filter(makhoa=kh)
			return render(request,'quanlysinhvien/kqthongke.html',{'temp':tkkhoa})
		else:
			return HttpResponse("Chọn khoa cần thống kê")

def kqthongkedcs(request):
	if request.method == 'POST':
		thongke = thongkesvdcs(request.POST)
		if thongke.is_valid():
			dcs = thongke.cleaned_data['dienchinhsach']
			tkdcs = sinhvien.objects.filter(madcs=dcs)
			return render(request,'quanlysinhvien/kqthongke.html',{'temp':tkdcs})
		else:
			return HttpResponse("Chọn diện chính sách cần thống kê")

def kqthongkeqq(request):
	if request.method == 'POST':
		thongke = thongkesvqq(request.POST)
		if thongke.is_valid():
			qq = thongke.cleaned_data['quequan']
			tkqq = sinhvien.objects.filter(quequan=qq)
			return render(request,'quanlysinhvien/kqthongke.html',{'temp':tkqq})
		else:
			return HttpResponse("Chọn nơi cần thống kê")
def kqthongkehp(request):
	if request.method == 'POST':
		thongke = thongkesvhp(request.POST)
		if thongke.is_valid():
			hp = thongke.cleaned_data['hocphan']
			svhp = thamgiahocphan.objects.filter(mahp=hp)
			tkhp = []
			for item in svhp:
				tkhp.append(sinhvien.objects.filter(mssv=item.masv))
			return render(request, 'quanlysinhvien/thongkehp.html', {'temp': tkhp})
		else:
			return HttpResponse("Chọn học phần cần thống kê")
def kqthongkediemhp(request):
	if request.method == 'POST':
		thongke = thongkesvhp(request.POST)
		if thongke.is_valid():
			hp = thongke.cleaned_data['hocphan']
			svhp = thamgiahocphan.objects.filter(mahp = hp)
			sv=sinhvien.objects.all()
			return render(request,'quanlysinhvien/Diemhp.html',{'temp':svhp,'sv':sv})
		else:
			return HttpResponse("Chọn học phần cần thống kê")

def kqthongkediemmax(request):
	if request.method == 'POST':
		thongke = thongkediemhp(request.POST)
		if thongke.is_valid():
			hp = thongke.cleaned_data['hocphan']
			result = thamgiahocphan.objects.filter(mahp = hp).aggregate(ketquamax=Max('diem'))
			max = result['ketquamax']
			svhp = thamgiahocphan.objects.filter(mahp__tenhp = hp,diem = max)
			tkdiemhp = []
			for item in svhp:
				tkdiemhp.append(sinhvien.objects.filter(mssv=item.masv))
			return render(request,'quanlysinhvien/Diemmax.html',{'temp':tkdiemhp,'max':max,'hp':hp})
		else:
			return HttpResponse("Chọn học phần cần thống kê")

def kqthongkett(request):
		kh = khoa.objects.all()
		kq = []
		for item in kh:
			result = sinhvien.objects.filter(makhoa=item.id).aggregate(sl=Count('mssv'))
			sluongsv = result['sl']
			temp = [item.tenkhoa,sluongsv]
			kq.append(temp)
		return render(request,'quanlysinhvien/thongkett.html',{'kq':kq,'kh':kh})


def kqthongketinchi(request):
	if request.method == 'POST':
		thongke = thongketc(request.POST)
		if thongke.is_valid():
			sv = thongke.cleaned_data['sinhvien']
			result1 = thamgiahocphan.objects.filter(masv__mssv = sv,mahp__loaihp ='Lý thuyết').aggregate(lt=Sum('mahp__sotinchi'))
			result2 = thamgiahocphan.objects.filter(masv__mssv=sv,mahp__loaihp ='Thực hành' ).aggregate(th=Sum('mahp__sotinchi'))
			lt = result1['lt']
			th = result2['th']
			if th == None:
				th=0
			if lt == None:
				lt = 0
		return render(request,'quanlysinhvien/kqthongketinchi.html',{'lt':lt,'th':th,'sv':sv})
	else:
		return HttpResponse("Chọn sinh viên cần thống kê")




def kqthongketinchihk(request):
	if request.method == 'POST':
		thongke = thongketchk(request.POST)
		if thongke.is_valid():
			sv = thongke.cleaned_data['sinhvien']
			hk = thongke.cleaned_data['hocky']
			result1 = thamgiahocphan.objects.filter(masv__mssv = sv,mahp__loaihp ='Lý thuyết',mahk__tenhk = hk).aggregate(lt=Sum('mahp__sotinchi'))
			result2 = thamgiahocphan.objects.filter(masv__mssv =sv,mahp__loaihp ='Thực hành',mahk__tenhk = hk ).aggregate(th=Sum('mahp__sotinchi'))
			lt = result1['lt']
			th = result2['th']
			if th == None:
				th=0
			if lt == None:
				lt = 0
		return render(request,'quanlysinhvien/kqthongketinchihk.html',{'lt':lt,'th':th,'sv':sv,'hk':hk})
	else:
		return HttpResponse("Chọn sinh viên cần thống kê")



def kqthongketinchihkmax(request):
	if request.method == 'POST':
		thongke = tktcmax(request.POST)
		if thongke.is_valid():
			hk = thongke.cleaned_data['hocky']
			sv =sinhvien.objects.all()
			max = 0;
			dssv = []
			for item in sv:
				result = thamgiahocphan.objects.filter(masv__mssv = item.mssv,mahk__tenhk = hk).aggregate(tc=Sum('mahp__sotinchi'))
				tc = result['tc']
				if tc == None:
					tc = 0
				if tc >= max:
					max = tc
			for i in sv:
				result2 = thamgiahocphan.objects.filter(masv__mssv=i.mssv, mahk__tenhk=hk).aggregate(tc=Sum('mahp__sotinchi'))
				tc2 = result2['tc']
				if tc2 == max:
					dssv.append(i)
		return render(request,'quanlysinhvien/kqthongketinchimax.html',{'sv':dssv,'tc':max,'hk':hk})
	else:
		return HttpResponse("Chọn sinh viên cần thống kê")