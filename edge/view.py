from django.shortcuts import render
from django.http import HttpResponseRedirect
from enrolldata.models import EnrollFormData
from login.models import loginac


def home(request):
    try:
        if request.method=="POST":
            Name=request.POST.get('name') 
            Email=request.POST.get('email') 
            Phone=request.POST.get('phone')
            data2=loginac(name=Name,email=Email,phone_no=Phone)
            data2.save()
            return HttpResponseRedirect("/about")
            # print(Name)
            # print(Email)
            # print(Phone)
    except:
        pass
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def blog(request):
    return render(request,"blog.html")

def posta(request):
    return render(request,"post.html")

def postb(request):
    return render(request,"post1.html")

def postc(request):
    return render(request,"post2.html")

def postd(request):
    return render(request,"post3.html")

def course(request):
    return render(request,"course.html")

def courseinner(request):
    return render(request,"course_inner.html")
    
def courseinner1(request):
    return render(request,"course_inner1.html")

def courseinner2(request):
    return render(request,"course_inner2.html")

def courseinner3(request):
    return render(request,"course_inner3.html")

def courseinner4(request):
    return render(request,"course_inner4.html")

def courseinner5(request):
    return render(request,"course_inner5.html")

def courseinner6(request):
    return render(request,"course_inner6.html")

def courseinner7(request):
    return render(request,"course_inner7.html")

def courseinner8(request):
    return render(request,"course_inner8.html")

def courseinner9(request):
    return render(request,"course_inner9.html")

def contact(request):
    return render(request,"contact.html")

def enroll(request):
    try:
        if request.method=="POST":
            Regno="edge"    
            Name=request.POST.get('name') 
            Fname=request.POST.get('fname')
            Mname=request.POST.get('mname')
            Dob=request.POST.get('dob')
            Email=request.POST.get('email')
            Phone=str(request.POST.get('phone'))
            Address=request.POST.get('addr')
            City=str(request.POST.get('city'))
            Gender=request.POST.get('gender')
            Photo=request.FILES['photo']
            Btime=str(request.POST.get('btime'))
            Pay_mode=str(request.POST.get('pay_mode'))
            Name_on_card=request.POST.get('name_on_card')
            Card_no=str(request.POST.get('card_no'))
            Expiry=str(request.POST.get('expiry'))
            Cvv=str(request.POST.get('cvv'))

            # data = EnrollFormData(regno=Regno,name=Name,fname=Fname,mname=Mname,dob=Dob,email=Email,phone=Phone,address=Address,city=City,gender=Gender,photo=Photo,btime=Btime,pay_mode=Pay_mode,name_on_card=Name_on_card,card_no=Card_no,expiry=Expiry,cvv=Cvv)
            # print(data)
            # data.save()
            data=EnrollFormData.objects.all().order_by('-id')[0]
            sid=data.id
            regno="edge"+str(sid)
            data = EnrollFormData(id=sid,regno=regno,name=Name,fname=Fname,mname=Mname,dob=Dob,email=Email,phone=Phone,address=Address,city=City,gender=Gender,photo=Photo,btime=Btime,pay_mode=Pay_mode,name_on_card=Name_on_card,card_no=Card_no,expiry=Expiry,cvv=Cvv)
            data.save()
            return HttpResponseRedirect("/view")
    except:
            pass
    return render(request,"enroll.html")

def view(request):
    data=EnrollFormData.objects.all()
    data1={
        'alldata':data
    }
    return render(request,"view.html",data1)

def delete(request,s_id):
    s=EnrollFormData.objects.get(pk=s_id)
    s.delete()
    return HttpResponseRedirect("/view")

def update(request,s_id):
    std=EnrollFormData.objects.get(pk=s_id)
    try:
        if request.method=="POST":
            Name=request.POST.get('name') 
            Fname=request.POST.get('fname')
            Mname=request.POST.get('mname')
            Dob=request.POST.get('dob')
            Email=request.POST.get('email')
            Phone=str(request.POST.get('phone'))
            Address=request.POST.get('addr')
            City=str(request.POST.get('city'))
            Gender=request.POST.get('gender')
            Photo=request.FILES['photo']
            Btime=str(request.POST.get('btime'))
            Pay_mode=str(request.POST.get('pay_mode'))
            Name_on_card=request.POST.get('name_on_card')
            Card_no=str(request.POST.get('card_no'))
            Expiry=str(request.POST.get('expiry'))
            Cvv=str(request.POST.get('cvv'))
            data=EnrollFormData.objects.all().order_by('-id')[0]
            sid=data.id
            regno="edge"+str(sid)
            data = EnrollFormData(id=s_id, regno=regno,name=Name,fname=Fname,mname=Mname,dob=Dob,email=Email,phone=Phone,address=Address,city=City,gender=Gender,photo=Photo,btime=Btime,pay_mode=Pay_mode,name_on_card=Name_on_card,card_no=Card_no,expiry=Expiry,cvv=Cvv)
            data.save()
            return HttpResponseRedirect("/view")
    except:
        pass


    return render(request,"update.html",{'std':std})
    
    # login account form
