from django.urls import path
from . import views
app_name = 'timkiem'
urlpatterns = [
    path('kqtk/',views.timkiemmssv, name = 'timkiemmssv'),

]
