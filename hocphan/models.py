from django.db import models
from quanlysinhvien.models import sinhvien
class hocky(models.Model):
	tenhk = models.CharField(max_length=50)
	def __str__(self):
		return self.tenhk

class hocphan(models.Model):
	mahp = models.CharField(primary_key = True,max_length = 8,default='')
	tenhp=models.CharField(max_length = 50)
	lythuyet = 'Lý thuyết'
	thuchanh = 'Thực hành'
	sotinchi = models.IntegerField(default = 1)
	loaihpchon = [(lythuyet, 'Lý thuyết'), (thuchanh, 'Thực hành')]
	loaihp= models.CharField(max_length = 20, choices = loaihpchon, default = lythuyet)
	mahk = models.ForeignKey(hocky, on_delete=models.CASCADE)
	def __str__(self):
		return self.tenhp
class thamgiahocphan(models.Model):
	mahp = models.ForeignKey(hocphan, on_delete=models.CASCADE)
	masv = models.ForeignKey(sinhvien, on_delete=models.CASCADE)
	mahk = models.ForeignKey(hocky, on_delete=models.CASCADE)
	ngaybd = models.DateField()
	ngaykt = models.DateField(blank=True, null=True, default=None)
	diem = models.FloatField(default=0)
