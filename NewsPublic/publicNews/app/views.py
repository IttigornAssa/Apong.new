from django.shortcuts import render
from .models import MOU,Student
from .forms import MOUForm,StudentForm
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q

# Create your views here.
def news_public(request):
    all_public = MOU.objects.all().order_by('-expire_date')
    all_student = Student.objects.all()

    query = request.GET.get('q')
    if query:
        all_public = all_public.filter(
            Q(title__icontains = query) | 
            Q(tpye__icontains = query)
            ).distinct()

    return render(request, 'news.html',{'all_public':all_public , 'all_student':all_student})

def all_tun(request):
    all_public = MOU.objects.all().order_by('-expire_date')
    return render(request, 'uni1.html',{'all_public':all_public})    

def detail_public(request,id):
    news = MOU.objects.get(pk=id)
    return render(request, 'detial.html',{'news':news})

def public_upload(request):
    if request.method == 'POST':
        form = MOUForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MOUForm()
    return render(request, 'upload.html', {
        'form': form
    })

def student_upload(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()
    return render(request, 'upload.html', {
        'form': form
    })

def pub_update(request,id):
    u = MOU.objects.get(pk=id)
    if not u:
        print("error")
    if request.method == 'POST':
        form = MOUForm(request.POST, request.FILES,instance=u)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MOUForm(instance=u)
    return render(request, 'update_form.html', {
        'form': form
    })

def public_delete(request,id):
   #+some code to check if New belongs to logged in user
   u = MOU.objects.get(pk=id).delete()
   return HttpResponseRedirect("/")

from django.contrib.auth import authenticate, login as auth_login

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('pass')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect("/upload")
    else:
        return render(request,'login.html')



def page(request,id):
    obj  = Student.objects.get(pk=id)
    return render(request,'page.html',{'obj':obj})        