from django.urls import path
from web.views import about, contact, index, หน้าแรก

urlpatterns = [
    path('', หน้าแรก, name='หน้าแรก'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact')
]
