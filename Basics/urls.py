
from django.urls import path
from Basics import views

urlpatterns = [

       path('Homepage/',views.homepage,name="Homepage"),
       path('Sum/',views.sum,name="Sum"),
       path('Calculator/',views.calculator,name="Calculator"),
       path('MarkList/',views.MarkList,name="MarkList"),

]
