from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'Basics/Homepage.html')

def sum(request):
    if request.method == "POST":
        number1 = int(request.POST.get("txt_num1"))
        number2 = int(request.POST.get("txt_num2"))
        result =  number1+number2
        return render(request,'Basics/Sum.html',{'Sum':result})
    else:
        return render(request,'Basics/Sum.html')


def calculator(request):
    if request.method == "POST":
        number1 = int(request.POST.get("txt_num1"))
        number2 = int(request.POST.get("txt_num2"))
        operator = request.POST.get("btn_operator")
        if operator == "+":
            result = number1 + number2
        elif operator == "-":
            result = number1 - number2
        elif operator == "*" :
            result = number1 * number2
        elif operator == "/":
            result = number1 / number2
        else :
            result = "Undefinded"
        return render(request,'Basics/Calculator.html',{'result':result})
    else:
        return render(request,'Basics/Calculator.html')

def MarkList(request):
    return render(request,'Basics/MarkList.html')

