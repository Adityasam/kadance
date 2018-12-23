from django.shortcuts import render, HttpResponse, redirect
from django import template
from .models import center,distribution, chennai
from django.contrib import messages
from django import forms
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout
# Create your views here.

register = template.Library()

center_name=['chennai', 'mumbai']

def home(request):
    if request.user.is_authenticated:

        if request.user.is_superuser:
            return redirect("main:admin_page")
        
        else:
            return redirect("main:centers")

    else:
        return render(request, 'home.html')

def centers(request):
    if request.user.is_superuser:
        return redirect('main:admin_login')
    else:
        free=[]
        engaged=[]
        dat=chennai.objects.filter(at=request.user.id,received=True)
        ct=chennai.objects.filter(at=request.user.id,received=True).count()
        data=distribution.objects.filter(at=request.user.id)
        tobe=chennai.objects.filter(at=request.user.id,received=False).count()
        over=0
        over_array=[]
        for d in data:
            if date.today() > d.end_date:
                over_array.append(d.imei)
            engaged.append(d.imei)
        for da in dat:
            if da.imei not in engaged:
                free.append(da)
        return render(request, "point.html",{'dat':dat, 'tobe':tobe, 'free':free, 'engaged':engaged, 'ct':ct, 'data':data, 'over_array':over_array, 'center_id':request.user.id})

def admin_page(request):
    return render(request, "admin_page_new.html")

def add_data(request,center_id):
    if request.method == "POST":
        cen=chennai.objects.all()
        counting=request.POST['count']
        for i in range(int(counting)+1):
            imname='im'+str(i)
            imeivalue=request.POST.get(imname)

            idname='tid'+str(i)
            tid=request.POST.get(idname)

            dat=request.POST.get('date')
            if imeivalue is not None:
                ch=chennai()
                ch.center_id=center_id
                ch.imei=imeivalue
                ch.t_id=tid
                ch.date=dat
                ch.at=center_id
                ch.save()

                cen=center.objects.get(center_id=center_id)
                a=cen.allotted
                newal=a+1
                cen.allotted=newal
                cen.save()

        return render(request, "success.html", {'center_id':center_id})

def update_data(request,cid):
    if request.method=="POST":
        cen=center.objects.all()
        ch=center.objects.get(id=cid)
        nm=request.POST.get('name')
        allot=request.POST.get('allot')
        dat=request.POST.get('date')
        ch.name=nm
        ch.allotted=allot
        ch.date=dat
        ch.save()
        return render(request, "admin_page_new.html")

def del_data(request, cid):
    center.objects.filter(id=cid).delete()
    return render(request, "admin_page.html")

def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pas=request.POST.get('pass')
        user=authenticate(username=un,password=pas)
        if user is not None:
            if user.is_active:
                if user.is_superuser:
                    auth_login(request,user)
                    return redirect('main:admin_page')
                else:
                    auth_login(request,user)
                    data=center.objects.filter(name=request.user.username)
                    dat=distribution.objects.filter(center_id=request.user.id)
                    return redirect('main:centers')
            else:
                return HttpResponse("Your login has been deactivated")

        else:
            messages.error(request,"Wrong username or password")
            return render(request,'login.html')
    else:
        return render(request,'login.html')


def logouts(request):
    logout(request)
    return redirect('main:home')

def add_center_data(request,center_id):
    if request.method=="POST":
        counting=request.POST.get('count')
        avail=distribution.objects.filter(center_id=center_id)
        tt=chennai.objects.filter(center_id=center_id)
        
        for i in range(int(counting)+1):
            imname='im'+str(i)
            idn='tid'+str(i)
            allotname='allot'+str(i)
            sdname='s_date'+str(i)
            edname='e_date'+str(i)

            im=request.POST.get(imname)
            ids=request.POST.get(idn)
            allot=request.POST.get(allotname)
            sd=request.POST.get(sdname)
            ed=request.POST.get(edname)
            

            if im is not None:
                d=distribution()
                d.center_id=request.user.id
                d.imei=im
                d.tablet_id=ids
                d.allotted_to=allot
                d.start_date=sd
                d.end_date=ed
                d.at=request.user.id
                d.save()
        return render(request, 'c_success.html')
        # else:
        #     messages.error(request,'You have only '+ str(ch) + ' tablets available')
        #     return render(request,"center.html" ,{'data':data, 'dat':dat, 'tot':tot})
    else:
        return redirect('main:centers')

def update_center(request,did):
    if request.method=='POST':
        dats=distribution.objects.get(id=did)
        dat=distribution.objects.filter(center_id=request.user.id)
        tota=0
        for d in dat:
            tota+=d.allotment
        data=center.objects.get(name=request.user.username)
        ch=data.allotted - tota

        allot=request.POST.get('allotment')

        final= ch - int(allot)
        if final>=0:
            sd=request.POST.get('s_date')
            ed=request.POST.get('e_date')
            po=request.POST.get('point')
            dats.distribution_point=po
            dats.allotment=allot
            dats.start_date=sd
            dats.end_date=ed
            dats.save()
            return redirect('main:centers')
        else:
            messages.error(request,"You don't have enough tablets!")
            return redirect('main:centers')

    else:
        messages.error(request,"You don't have enough tablets")
        return redirect('main:centers')

def detail(request,center_id):
    free=[]
    engaged=[]
    dat=chennai.objects.filter(at=center_id)
    data=distribution.objects.filter(at=center_id)
    over_array=[]
    for d in data:
        print(d.end_date)
        print(date.today())
        if date.today() > d.end_date:
            over_array.append(d.imei)
        engaged.append(d.imei)
    for da in dat:
        if da.imei not in engaged:
            free.append(da)
    ct=chennai.objects.filter(at=center_id).count()
    tobe=chennai.objects.filter(at=center_id,received=False).count()
    name=User.objects.get(id=center_id)
    return render(request, "center.html",{'dat':dat, 'tobe':tobe, 'data':data, 'free':free, 'engaged':engaged, 'over':over_array, 'name':name, 'center_id':center_id, 'ct':ct})

def center_detail(request,center_id):
    free=[]
    engaged=[]
    request.session['cid']=center_id
    dat=chennai.objects.filter(at=center_id)
    data=distribution.objects.filter(at=center_id)
    name=User.objects.get(id=center_id)
    over_array=[]
    for d in data:
        if date.today() > d.end_date:
            over_array.append(d.imei)
        engaged.append(d.imei)
    for da in dat:
        if da.imei not in engaged:
            free.append(da) 
    return render(request, 'center_detail.html',{'free':free, 'name':name, 'engaged':engaged, 'dat':dat, 'data':data, 'over':over_array})

def mark(request,mid):
    data=distribution.objects.get(id=mid)
    data.complete=True
    data.save()
    return redirect('main:centers')

def transfer(request,tid):
    data=distribution.objects.get(tablet_id=tid)
    return render(request, 'transfer.html', {'data':data})

def transfer_from_center(request,tid,cid):
    data=chennai.objects.get(t_id=tid)
    return render(request, 'transfer.html', {'data':data, 'cid':cid, 'tid':tid})

def damaged(request,tid):
    tab=distribution.objects.get(id=tid)
    tab.condition=True
    tab.save()
    return redirect('main:centers')

def tobe(request):
    tabs=chennai.objects.filter(at=request.user.id,received=False)
    return render(request,'received.html',{'tab':tabs})

def mark_received(request,tid):
    tabs=chennai.objects.get(at=request.user.id, id=tid)
    tabs.received=True
    tabs.receive_date=date.today()
    tabs.save()
    return redirect('main:tobe')

def transfer_tab(request):
    if request.method == "POST":
        imei=request.POST.get('im0')
        tab=request.POST.get('tid0')
        date=request.POST.get('date')
        center=request.POST.get('center')
        cid=request.POST.get('cid')
    
        ch=chennai()
        ch.center_id=center
        ch.imei=imei
        ch.t_id=tab
        ch.date=date
        ch.at=center
        ch.save()
        
        de=chennai.objects.get(center_id=cid, t_id=tab)
        de.at=0
        de.save()

        return render(request, 'transfer_success.html',{'center_id':cid})
        # free=[]
        # engaged=[]
        # dat=chennai.objects.filter(center_id=cid)
        # data=distribution.objects.filter(center_id=cid)
        # name=User.objects.get(id=cid)
        # return render(request, 'center_detail.html',{ 'name':name, 'dat':dat, 'data':data})

def orignal_home(request):
    return render(request, 'home.html')