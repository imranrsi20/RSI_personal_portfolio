from django.shortcuts import render,HttpResponse

# Create your views here.
from .models import *

def home(request):
    info=Personal_info.objects.get(pk=1)
    about=About.objects.get(pk=1)
    skill=Skill.objects.get(pk=1)
    print(type(skill.python))
    experience=Experience.objects.all()
    work=Work.objects.all()
    context={
        "info":info,
        "about":about,
        "skill":skill,
        "experience":experience,
        "work":work,
    }
    return render(request,'index.html',context)


def About_info(request):
    info = Personal_info.objects.get(pk=1)
    about = About.objects.get(pk=1)
    skill = Skill.objects.get(pk=1)
    print(type(skill.python))
    experience = Experience.objects.all()
    work = Work.objects.all()
    context = {
        "info": info,
        "about": about,
        "skill": skill,
        "experience": experience,
        "work": work,
    }
    return render(request,'about-us.html',context)