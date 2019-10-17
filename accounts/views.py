from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.forms import RegistrationForm, EditProfileForm
from accounts.forms import ImageUploadForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.template import RequestContext, loader
from post.models import Post
from post.models import Comment
from post.forms import PostForm, CommentForm
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#Create your views here.	                                          
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/accounts/profile2')
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "reg_form.html",
                          context={"form":form})

    form = RegistrationForm
    return render(request = request,
                  template_name = "reg_form.html",
                  context={"form":form}) 

def index(request):
    template_name = 'users.html'    
    users = User.objects.all()  
    profile = UserProfile.objects.all()
    args = {
        'users': users,
        'profile': UserProfile
                   }
    return render(request, template_name, args)


def register_cont(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('http://localhost:8000/accounts/profile2/')
        else:
            
            return render(request = request,
                          template_name = "reg_form.html",
                          context={"form":form})

    form = ImageUploadForm
    return render(request = request,
                  template_name = "reg_form.html",
                  context={"form":form})                                                  

def view_profile(request):
	args = {'user': request.user},
	return render(request, 'profile.html')


def edit_profile(request):
    if request.method == "POST":
        form = EditProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/profile')
        else:

            return render(request = request,
                          template_name = "edit_profile.html",
                          context={"form":form})

    form = EditProfileForm
    return render(request = request,
                  template_name = "edit_profile.html",
                  context={"form":form}) 
    
	          
def users_list(request):
    template_name = 'users.html'    
    users = User.objects.all()  
    profile = UserProfile.objects.all()
    args = {
        'users': users,
        'profile': UserProfile
                   }
    return render(request, template_name, args)

	  
@login_required
def change_password(request):
	if request.method == 'POST':
            form = PasswordChangeForm(request.POST)
            if form.is_valid():
	              form.save()  
	              return redirect('http://127.0.0.1:8000/accounts/profile')
	else:
		           form = PasswordChangeForm(user=request.user)	
		           args = {'form': form}
		           return render(request, 'change_password.html', args)
		           
def view_results(request):
	model : UserProfile
	return render(request, 'result.html')
	

def view_resultss(request):
	model : UserProfile
	return render(request, 'results.html')
	
	
def success(request):
	return render(request, 'success.html')
	
def accounts(request):
	return render(request, 'account.html')


        
def profile(request):
	return render(request, 'profile2.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('http://127.0.0.1:8000/accounts/profile')
                
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})