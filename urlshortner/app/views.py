from django.shortcuts import render , redirect
from .forms import URLForm
from .models import *
from django.contrib import messages
from .utils import generate_code
# Create your views here.
def homepage(request):
    return render(request , 'app/home.html')

def link_create(request):
    if request.method =="GET":
        form = URLForm()
        return render(request , 'app/link.html',{"form":form})
    if request.method == "POST":
        form = URLForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)

            if not instance.short_code:
                while True:
                    instance.short_code = generate_code()

                    if not ShortURL.objects.filter(
                        short_code=instance.short_code
                    ).exists():
                        break
                #db+integrity errors could be efficient

            instance.user = request.user
            instance.save()
            print(instance.short_code)
            return redirect("home")

        return render(request, "app/link.html", {"form": form})

def redirect_url(request):
    pass

def link_delete(request , id):
    url = ShortURL.objects.get(id =id)
    
    if url.user.id != request.user.id:
        messages.error(request,"Invalid URL")
        return redirect("home")
    
    if request.method == "DELETE":

        if url.user.id != request.user.id:
            messages.error(request,"Invalid URL")
            return redirect("home")
        
        url.delete()
        return redirect("home")

def link_edit(request,id):
    url = ShortURL.objects.get(id=id)

    if url.user.id != request.user.id:
        messages.error(request,"Invalid URL")
        return redirect("home")

    if request.method == "GET":
        form = URLForm(instance=url)
        return render(request , 'app/link.html',{"form":form})

    if request.method == "POST":
        form = URLForm(request.POST,instance=url)
        if form.is_valid():
            form.save()
            return redirect("home")
        