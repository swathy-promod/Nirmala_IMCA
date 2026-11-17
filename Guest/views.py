from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import *

# Create your views here.
def UserRegistration(request):
    dis=tbl_district.objects.all()
    if request.method == "POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        password=request.POST.get("txt_password")
        placeid=tbl_place.objects.get(id=request.POST.get("sel_place"))
        photo=request.FILES.get("file_photo")
        tbl_user.objects.create(user_name=name,user_email=email,user_contact=contact
        ,user_address=address,user_photo=photo,user_password=password,place=placeid)
        return render(request,"Guest/UserRegistration.html",{"district":dis})

    return render(request,"Guest/UserRegistration.html",{"district":dis})


def ajaxplace(request):
    districtid=request.GET.get('did')
    placeid=tbl_place.objects.filter(district=districtid)
    return render(request,"Guest/AjaxPlace.html",{'placeid':placeid})

def login(request):
    if request.method == "POST":
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()

        if admincount > 0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect("Admin:Homepage")
        elif usercount > 0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            if userdata.user_status == 0:
                request.session['uid']=userdata.id
                return redirect("User:Homepage") 
            else:
                return render(request,"Guest/Login.html",{'msg':'You Are Blocked'})

        else:
            return render(request,"Guest/Login.html")

    return render(request,"Guest/Login.html")