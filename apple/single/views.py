from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>My name is Aman</h1>")
def index(request):
  name='Aman'
  age='22'
  l=[2,3,4,4,5,5,4,3,3]
  return render(request,'home.html',{"data":name,"jhi":age,"list":l})

def hip(request):
   if request.method=="GET":
         name='Aman'
         return render(request,'home.html',{"ame":name})
   else:
     Name=request.POST["uname"]
     password=request.POST["psw"]
     rem=request.POST["remember"]
     it=request.POST['email']
      
     return render(request,'home.html',{'Name':Name,'password':password,'rem':rem,'it':it})

def addi(request):
    if request.method == 'POST':
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        options=request.POST['options']
        if options=='+':
            result=num1+num2
        elif options=='-':
            result=num1-num2
        elif options=='*':
            result=num1*num2
        elif options=='/':
            result=num1/num2
        
        return render(request, 'addi.html', {'result': result})
    
    return render(request, 'addi.html')

