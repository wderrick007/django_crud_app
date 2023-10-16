
from django.shortcuts import render, redirect  
from local.forms import PersonForm  
from local.models import Person  
#from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.  
def index(request):  
   
    
    
        
        
    
  

    if request.method == "POST":  
        form = PersonForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = PersonForm()  
    return render(request,'index.html',{'form':form})  


    
def show(request):  
    person1 = Person.objects.all()  
    return render(request,"show.html",{'person1':person1})  
def edit(request, id):  
    person2 = Person.objects.get(id=id)  
    return render(request,'edit.html', {'person2':person2})  
def update(request, id):  
    person2 = Person.objects.get(id=id)  
    form = PersonForm(request.POST, instance = person2)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'person2': person2})  
def destroy(request, id):  
    person2 = Person.objects.get(id=id)  
    person2.delete()  
    return redirect("/show")  