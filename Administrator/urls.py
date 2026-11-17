
from django.urls import path
from Administrator import views
app_name="Admin"
urlpatterns = [

       path('Homepage/',views.homepage,name="Homepage"),
       path('District/',views.District,name="District"),
       path('AdminRegistration/',views.AdminRegistration,name="AdminRegistration"),
       path('Category/',views.Category,name="Category"),
       path('deletedistrict/<int:did>',views.deletedistrict,name="deletedistrict"),
       path('deletecategory/<int:did>',views.deletecategory,name="deletecategory"),
       path('deleteadmin/<int:did>',views.deleteadmin,name="deleteadmin"),
       path('editdistrict/<int:eid>',views.editdistrict,name="editdistrict"),
       path('Place/',views.Place,name="Place"),
       path('Subcategory/',views.Subcategory,name="Subcategory"),
       path('deleteplace/<int:did>',views.deleteplace,name="deleteplace"),
       path('editplace/<int:eid>',views.editplace,name="editplace"),
       path('Userlist/',views.userlist,name="userlist"),
       path('Block/<int:bid>',views.Block,name="Block"),
       path('UnBlock/<int:ubid>',views.UnBlock,name="UnBlock"),











]
