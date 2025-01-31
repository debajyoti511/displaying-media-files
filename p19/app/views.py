from django.shortcuts import render
from .forms import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    EUFO = UserForm()
    EPFO = ProfileForm()
    d = {'EUFO': EUFO,'EPFO': EPFO}
    if request.method == 'POST':
        UFDO = UserForm(request.POST)
        PFDO = ProfileForm(request.POST, request.FILES)
        if UFDO.is_valid() and PFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO = PFDO.save(commit=False)
            MPFDO.username = MUFDO
            MPFDO.save()
            return HttpResponse('DONE...')
        return HttpResponse('Invalid Data')
    return render(request, 'register.html', d)


def users(request):
    profiles = Profile.objects.all
    d = {'profiles':profiles}
    return render(request,'users.html', d)