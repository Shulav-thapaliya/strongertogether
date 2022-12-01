from lib2to3.pgen2.token import COMMENT
from multiprocessing import reduction
from django.shortcuts import render ,redirect
from .models import share
from .forms import Phase1form,commentform

# form page (test page function)
def form (request):
    
    new = Phase1form()
    
    if request.method == 'POST':
        new = Phase1form(request.POST)
        if new.is_valid():
            new.save()
            return redirect('res')
    x = {'newf':new}
    return render (request, 'homepage/test.html',x)        
# end of test page function

# home page function

def home(request):
    return render(request,'homepage/homepage.html')

# end of home page function

# database page function
def story(request):
    # form has been added 
    

    

    dataBase = share.objects.filter(Privacy='Y')
    y = {'data':dataBase}

    return render(request,'homepage/story.html',y)

def comform(request):
    
    com = commentform()
    if request.method == 'POST':
        com  = commentform(request.POST)
        if com.is_valid():
            com.save()
            return redirect('str')
   
    var = {'newform':com}

    return render(request,'homepage/comment.html',var)

# end of database page function


    
   

