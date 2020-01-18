from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User
from .forms import SignUpForm,SellerForm

# Create your views here.

@csrf_exempt
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            user = User()
            # user.first_name = form.cleaned_data['first_name']
            # user.last_name  = form.cleaned_data['last_name']
            username   = form.cleaned_data['username']
            email      = form.cleaned_data['email']
            password1  = form.cleaned_data['password1']
            password2  = form.cleaned_data['password2']

            # print(request.POST.get('first_name'))
            # print(form.cleaned_data['last_name'])
            # print(form.cleaned_data['username'])
            # print(form.cleaned_data['email'])
            # print(form.cleaned_data['password1'])
            # print(form.cleaned_data['password2'])
            # print(request.POST.get('cat'))

            completed = request.POST.get('cat')
            if completed == 'True':
                user.user_type = 'True'
                # def create_user(username,email,password1):
                #     new_user = User.objects.create_user(username, email, password1)
                #     # new_user.first_name = request.POST.get('first_name')
                #     # new_user.last_name  = request.POST.get('last_name')
                #     new_user.password1  = passwaord1
                #     new_user.password2  =password2
                #     new_user.save()
                user.save()
                pk = user.pk
                return HttpResponseRedirect(reverse('seller', kwargs={'pk':pk}))
            else:
                user.save()
                return HttpResponseRedirect('/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()

    return render(request, 'form.html', {'form': form})


def get_seller(request,pk):
    user = User.objects.get(pk = pk)
    form = SellerForm()
    if user.user_type == 'True':
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = SellerForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                user.sell = form.cleaned_data['sell']
                user.save()
                # pk = user.pk
                return HttpResponseRedirect('/')
        # if a GET (or any other method) we'll create a blank form
        else:
            form = form


    return render(request, 'seller.html',{'form':form})
