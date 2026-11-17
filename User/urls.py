
from django.urls import path
from User import views
app_name="User"
urlpatterns = [

       path('Homepage/',views.Homepage,name="Homepage"),
       path('MyProfile/',views.MyProfile,name="MyProfile"),
       path('EditProfile/',views.EditProfile,name="EditProfile"),
       path('ChangePassword/',views.ChangePassword,name="ChangePassword"),

       










]
