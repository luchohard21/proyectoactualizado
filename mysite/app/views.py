from django.http.request import *
from django.shortcuts import render


# Create your views here.
#vista pagina 1
def index(request):
    return render(request, 'index.html')

#vista pagina 2
def nosotros(request):
    return render(request, 'nosotros.html')

#vista pagina 3    
def servicios(request):
    return render(request, 'servicios.html')

#vista pagina 4
def cita(request):
    return render(request, 'cita.html')

#vista pagina 5
def contactanos(request):
    return render(request, 'contactanos.html')

#vista pagina 6
def opinion(request):
    return render(request, 'opinion.html')    



def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request, 'posts/create.html')  

        else:
                return render(request,'posts/create.html')