from main.models import center,center_name
from django.contrib.auth.models import User

def center_name_processor(request):
    c_name = center_name.objects.all()            
    return {'center_name': c_name}

def center_data_processor(request):
    c_data = center.objects.all()            
    return {'center_data': c_data}


