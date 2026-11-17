from django.shortcuts import render
from Guest.models import *
# Create your views here.
def Homepage(request):
    return render(request,"User/Homepage.html")

def MyProfile(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    return render(request,"User/MyProfile.html",{'userdata':userdata})

def EditProfile(request):
    edit=tbl_user.objects.get(id=request.session['uid'])
    if request.method == "POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        edit.user_name=name
        edit.user_email=email
        edit.user_contact=contact
        edit.user_address=address
        edit.save()
        return render(request,"User/EditProfile.html",{'msg':'Profile Updated'})

    return render(request,"User/EditProfile.html",{'edit':edit})

def ChangePassword(request):
    update=tbl_user.objects.get(id=request.session['uid'])
    if request.method == "POST":
        oldpass=request.POST.get('txt_oldpass')
        newpass=request.POST.get('txt_newpass')
        retypepass=request.POST.get('txt_retypepass')
        if update.user_password == oldpass:
            if newpass == retypepass:   
                update.user_password=newpass
                update.save()
                return redirect("User:MyProfile")
            else:
                return render(request,"User/ChangePassword.html",{'msg':'New and Retyped password Not correct'})
        else:
                return render(request,"User/ChangePassword.html",{"msg":"Invalid"})
 
    return render(request,"User/ChangePassword.html")