from django.shortcuts import render , redirect
from .forms import URLForm
from .models import *
from django.contrib import messages
from .utils import generate_code
# Create your views here.
def homepage(request):
    return render(request , 'app/home.html')

def createlink(request):
    if request.method =="GET":
        form = URLForm()
        return render(request , 'app/create_link.html',{"form":form})
    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

        custom = form.cleaned_data["custom_code"]
        if custom:
            if ShortURL.objects.filter(short_code=custom).exists():
                messages.error(request,"Already taken")

                return redirect("home")

            code = custom
        else:
            while True:
                code = generate_code()
                if not ShortURL.objects.filter(short_code=code).exists():
                    break

        instance.user = request.user
        instance.short_code = code
        instance.save()
        print(code)
        return redirect("home")

