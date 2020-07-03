from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm 
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST) #create a form instance with "POST" data
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            #firstname=form.cleaned_data.get('firstname')
            #print("firstname="+firstname)
            messages.success(request,f'Account Created for the {username}! and you are now able to login')
            return redirect('login')
    else:
        form=UserRegisterForm()   #create a blank form
    return render(request,'users/register.html',{'form':form })

@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username =u_form.cleaned_data.get('username')
            messages.success(request,f'Profile Updated sucessfully')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={'u_form':u_form,'p_form':p_form}
    return render(request,'users/profile.html',context)