from django.db import models
from dienchinhsach.models import dienchinhsach
from khoa.models import khoa

class quequan(models.Model):
	tenqq=models.CharField(max_length = 500)
	def __str__(self):
		return self.tenqq
class sinhvien(models.Model):
	mssv = models.CharField(primary_key = True,max_length = 8,default='')
	tensv=models.CharField(max_length = 500)
	ngaysinh=models.DateField()
	nam = 'Nam'
	nu = 'Nữ'
	phaichon = [(nam, 'Nam'), (nu, 'Nữ')]
	phai= models.CharField(max_length = 3, choices = phaichon, default = nam)
	quequan= models.ForeignKey(quequan,on_delete=models.CASCADE)
	madcs = models.ForeignKey(dienchinhsach,on_delete=models.CASCADE)
	makhoa = models.ForeignKey(khoa,on_delete=models.CASCADE)
	def __str__(self):
		return self.mssv

