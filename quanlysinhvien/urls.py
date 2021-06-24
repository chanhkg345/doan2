from django.urls import path
from . import views
app_name = 'sinhvien'
urlpatterns = [
    path('',views.trangchu, name= 'index' ),
    path('sv/',views.danhsachsv, name= 'dssv' ),
    path('hocphan/',views.danhsachhp, name= 'hocphan' ),
    path('dienchinhsach/',views.danhsachdcs, name= 'dcs' ),
    path('chitetsv/<mssv>',views.chitietsv, name= 'ctsv' ),
    path('chitetkhoa/<tenkhoa>',views.chitietkhoa, name= 'ctkh' ),
    path('thongke/',views.thongke, name = 'thongke'),
    path('thongkediem/',views.thongkediem, name = 'thongkediem'),
    path('thongketinchi/',views.thongketinchi, name = 'thongketinchi'),
    path('kqthongketinchi/',views.kqthongketinchi, name = 'kqthongketinchi'),
    path('kqthongketinchihk/',views.kqthongketinchihk, name = 'kqthongketinchihk'),
    path('kqthongketinchihkmax/',views.kqthongketinchihkmax, name = 'kqthongketinchihkmax'),
    path('kqthongkekh/',views.kqthongkekh, name = 'kqthongkekh'),
    path('kqthongkedcs/',views.kqthongkedcs, name = 'kqthongkedcs'),
    path('kqthongkeqq/',views.kqthongkeqq, name = 'kqthongkeqq'),
    path('kqthongkehp/',views.kqthongkehp, name = 'kqthongkehp'),
    path('kqthongkediemhp/',views.kqthongkediemhp, name = 'kqthongkediemhp'),
    path('kqthongkediemmax/',views.kqthongkediemmax, name = 'kqthongkediemmax'),
    path('kqthongkett/',views.kqthongkett, name = 'kqthongkett'),

]
