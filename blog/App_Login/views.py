from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

def register(request):
    form = UserCreationForm()
    registered = False

    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            registered = True

    dict = {'form':form,'registered':registered}
    return render(request,'App_login/sign_up.html',context = dict)

def login_user(request):

    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                # return redirect('')
                return HttpResponseRedirect(reverse('blog:home'))
    return render(request,'App_login/login.html',{'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:home'))

@login_required
def user(request):
    return HttpResponse("User")
