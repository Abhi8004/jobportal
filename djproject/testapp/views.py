from django.shortcuts import render
from testapp.models import*
# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def hydjobs_view(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',my_dict)

def bangjobs_view(request):
    jobs_list=bangjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/bangjobs.html',my_dict)

def chennaijobs_view(request):
    jobs_list=chennaijobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/chennaijobs.html',my_dict)

def punejobs_view(request):
    jobs_list=punejobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/punejobs.html',my_dict)
