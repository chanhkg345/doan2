from django import forms
from .models import sinhvien
from khoa.models import khoa
from hocphan.models import hocphan,hocky
from quanlysinhvien.models import quequan
from dienchinhsach.models import dienchinhsach
class thongketchk(forms.Form):
    sinhvien = forms.ModelChoiceField(queryset=sinhvien.objects.all(),required=True)
    hocky = forms.ModelChoiceField(queryset=hocky.objects.all(),required=True)
class thongketc(forms.Form):
    sinhvien = forms.ModelChoiceField(queryset=sinhvien.objects.all(),required=True)

class tktcmax(forms.Form):
    hocky = forms.ModelChoiceField(queryset=hocky.objects.all(),required=True)

class thongkesvkh(forms.Form):
    khoa = forms.ModelChoiceField(queryset=khoa.objects.all(),required=True)

class thongkesvhp(forms.Form):
    hocphan = forms.ModelChoiceField(queryset=hocphan.objects.all(), required=True)
class thongkediemhp(forms.Form):
    hocphan = forms.ModelChoiceField(queryset=hocphan.objects.all(), required=True)

class thongkesvdcs(forms.Form):
    dienchinhsach = forms.ModelChoiceField(queryset=dienchinhsach.objects.all(), required=True)

class thongkesvqq(forms.Form):
    quequan = forms.ModelChoiceField(queryset=quequan.objects.all(), required=True)
