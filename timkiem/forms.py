from django import  forms
from quanlysinhvien.models import sinhvien

class formtimkiem(forms.Form):
    timkiem = forms.CharField(max_length=500, label='Tìm kiếm')