from django.urls import path
from web.views import หน้าแรก, รายชื่อโรงพยาบาล, รายชื่อแพทย์, รายชื่อผู้ป่วย,  detail

urlpatterns = [
    path('', หน้าแรก, name='หน้าแรก'),
    path('รายชื่อโรงพยาบาล/', รายชื่อโรงพยาบาล, name='รายชื่อโรงพยาบาล'),
    path('รายชื่อแพทย์/', รายชื่อแพทย์, name='รายชื่อแพทย์'),
    path('รายชื่อผู้ป่วย/', รายชื่อผู้ป่วย, name='รายชื่อผู้ป่วย'),
    path('detail/<int:id>', detail, name='detail'),
]
