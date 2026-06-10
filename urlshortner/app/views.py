from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import URLForm
from .models import *
from django.contrib import messages
from .utils import generate_code
from datetime import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request , 'app/home.html')

@login_required
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

        return render(request, "app/link_create.html", {"form": form})

def redirect_url(request, code):

    obj = get_object_or_404(
        ShortURL,
        short_code=code)

    if (obj.expires_at and obj.expires_at < timezone.now()):
        return HttpResponse("Link expired")

    obj.clicks += 1

    obj.save(update_fields=["clicks"])

    ClickLog.objects.create(
        url=obj,
        ip_address=request.META.get("REMOTE_ADDR", "0.0.0.0")
    )

    return redirect(obj.original_url)

@login_required
def link_delete(request , id):
    url = get_object_or_404(ShortURL , id =id , user= request.user )
    
    if request.method == "POST":

        url.delete()
        return redirect("home")

@login_required
def link_edit(request,id):
    url = ShortURL.objects.get(id=id)
    # url = get_object_or_404

    if url.user.id != request.user.id:
        messages.error(request,"Invalid URL")
        return redirect("home")

    if request.method == "GET":
        form = URLForm(instance=url)
        return render(request , 'app/link_edit.html',{"form":form})

    if request.method == "POST":
        form = URLForm(request.POST,instance=url)
        if form.is_valid():
            form.save()
            return redirect("home")
        
@login_required
def links(request):
    urls = ShortURL.objects.filter(user=request.user).order_by("-created_at")
    return render(request , "app/link.html",{"urls":urls})