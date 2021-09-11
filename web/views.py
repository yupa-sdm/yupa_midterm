from web.models import Hospital
from django.shortcuts import render

# Create your views here.
def หน้าแรก(request):
    context = {}
    context['hospitals'] = Hospital.objects.all()
    return render(request, 'หน้าแรก.html', context)

def detail(request, id):
    context = {}
    hospitals = Hospital.objects.filter(id=id)
    for hospital in hospitals:
        context['hospital'] = hospital

    return render(request, "detail.html", context)

def รายชื่อโรงพยาบาล(request):
    return render(request, 'รายชื่อโรงพยาบาล.html')

def รายชื่อแพทย์(request):
    return render(request, 'รายชื่อแพทย์.html')

def รายชื่อผู้ป่วย(request):
    return render(request, 'รายชื่อผู้ป่วย.html')