from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import *

# Create your views here.

def homepage(request):
    return render(request,'Administrator/Homepage.html')

def District(request):
    districts=tbl_district.objects.all()
    if request.method=="POST":
       name=request.POST.get("txt_district")
       tbl_district.objects.create(district_name=name)
       return render(request,"Administrator/District.html",{'district':districts})
    else:
        return render(request,"Administrator/District.html",{'district':districts})


def Category(request):
    categories=tbl_category.objects.all()
    if request.method=="POST":
       name=request.POST.get("txt_category")
       tbl_category.objects.create(category_name=name)
       return render(request,"Administrator/Category.html",{'category':categories})
    else:
        return render(request,"Administrator/Category.html",{'category':categories})

def AdminRegistration(request):
    admins=tbl_admin.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        tbl_admin.objects.create(admin_name=name,admin_email=email,admin_password=password)
        return render(request,"Administrator/AdminRegistration.html",{'admin':admins})
    else:
        return render(request,"Administrator/AdminRegistration.html",{'admin':admins})

 
def deletedistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:District")

def deletecategory(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:Category")

def deleteadmin(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:AdminRegistration")

def editdistrict(request,eid):
    districts=tbl_district.objects.all()
    edit=tbl_district.objects.get(id=eid)
    if request.method == "POST":
        disname=request.POST.get("txt_district")
        edit.district_name=disname
        edit.save()
        return redirect("Admin:District")
    return render(request,"Administrator/District.html",{'edit':edit,'district':districts})

def Place(request):
    district=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        placename=request.POST.get("txt_place")
        districtid=tbl_district.objects.get(id=request.POST.get("sel_district"))
        tbl_place.objects.create(place_name=placename,district=districtid)
        return render(request,"Administrator/Place.html",{"district":district,'place':place})
    else:
        return render(request,"Administrator/Place.html",{"district":district,'place':place})

def Subcategory(request):
    category=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.all()
    if request.method=="POST":
        subcategoryname=request.POST.get("txt_subcategory")
        categoryid=tbl_category.objects.get(id=request.POST.get("sel_category"))
        tbl_place.objects.create(subcategory_name=subcategoryname,category=categoryid)
        return render(request,"Administrator/SubCategory.html",{"category":category,'place':place})

    else:
        return render(request,"Administrator/SubCategory.html",{"category":category,'place':place})

def deleteplace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Admin:Place")

def editplace(request,eid):
    district=tbl_district.objects.all()
    edit=tbl_place.objects.get(id=eid)
    if request.method == "POST":
        placename=request.POST.get("txt_place")
        districtid=tbl_district.objects.get(id=request.POST.get("sel_district"))
        edit.place_name=placename
        edit.district=districtid
        edit.save()
        return redirect("Admin:Place")
    else:
        return render(request,"Administrator/Place.html",{'edit':edit,'district':district})

def userlist(request):
    userdata=tbl_user.objects.all()
    return render(request,"Administrator/UserList.html",{'userdata':userdata})

def Block(request,bid):
    block=tbl_user.objects.get(id=bid)
    block.user_status = 1
    block.save()
    return render(request,"Administrator/UserList.html",{'msg':'User Blocked'})

def UnBlock(request):
    unblock=tbl_user.objects.get(id=ubid)
    unblock.user_status = 0
    unblock.save()
    return render(request,"Administrator/UserList.html",{'msg':'User UnBlocked'})