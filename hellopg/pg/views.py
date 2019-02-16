from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView,DeleteView
from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from pg.forms import SignUpForm,UploadForm,UserUpdateForm,ProfileUpdateForm
from pg.models import UploadPG

@login_required
def DeletePostView(request,pk):
    if request.user.is_authenticated:
        obj= get_object_or_404(UploadPG,user=request.user,pk=pk)
        if request.method=='POST':
            obj.delete()
            messages.success(request,'You have successfully deleted the POST')
            return redirect('/dashboard')

        return render(request,'pg/uploadpg_confirm_delete.html',{'obj':obj})

@login_required
def ownerPGaroundKhrarListView(request):
    if request.user.is_authenticated:
        pg_list=UploadPG.objects.filter(user=request.user,location='pgaroundkhrar').order_by('-id')
        paginator=Paginator(pg_list,2)
        page_number=request.GET.get('page')
        try:
            pg_list=paginator.page(page_number)
        except PageNotAnInteger:
            pg_list=paginator.page(1)
        except EmptyPage:
            pg_list=paginator.page(paginator.num_pages)
        return render (request,'pg/ownerPGaroundKhrarList.html',{'pg_list' : pg_list})
    else :
        return render (request, 'pg/home.html')

@login_required
def editPostView(request, pk):
    if request.user.is_authenticated:
        obj= get_object_or_404(UploadPG,user=request.user, pk=pk)
        if request.method=='POST':
            form = UploadForm(request.POST,request.FILES, instance= obj)
            try:
                if form.is_valid():
                    obj= form.save(commit= False)
                    obj.save()
                    messages.warning(request, "You have successfully updated the post")
            except Exception as e:
                messages.warning(request,"Your Post was not saved due to {}".format(e))
        else:
            form = UploadForm(instance= obj)
    return render(request,'pg/update.html' , {'form': form,'obj':obj})

@login_required
def userProfileView(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            u_form= UserUpdateForm(request.POST,instance=request.user)
            p_form= ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your Profile is Updated!!')
                return redirect('/profile')
        else:
            u_form= UserUpdateForm(instance=request.user)
            p_form= ProfileUpdateForm(instance=request.user.profile)
        return render(request,'pg/profile.html',{'u_form':u_form,'p_form':p_form})

@login_required
def dashboardView(request):
    if request.user.is_authenticated:
        pg_list=UploadPG.objects.filter(user=request.user).order_by('-id')
        paginator=Paginator(pg_list,2)
        page_number=request.GET.get('page')
        try:
            pg_list=paginator.page(page_number)
        except PageNotAnInteger:
            pg_list=paginator.page(1)
        except EmptyPage:
            pg_list=paginator.page(paginator.num_pages)
        return render (request,'pg/dashboard.html',{'pg_list' : pg_list})
    else :
        return render (request, 'pg/home.html')



@login_required
def ownerPGinKhrarListView(request):
    if request.user.is_authenticated:
        pg_list=UploadPG.objects.filter(user=request.user,location='pginkhrar').order_by('-id')
        paginator=Paginator(pg_list,2)
        page_number=request.GET.get('page')
        try:
            pg_list=paginator.page(page_number)
        except PageNotAnInteger:
            pg_list=paginator.page(1)
        except EmptyPage:
            pg_list=paginator.page(paginator.num_pages)
        return render (request,'pg/ownerPGInKhrarList.html',{'pg_list' : pg_list})
    else :
        return render (request, 'pg/home.html')

@login_required
def uploadView(request):
    if request.method=='POST':
        upload=UploadForm(request.POST,request.FILES)
        if upload.is_valid():
            print("Form Validation Success....")
            print('Name:',upload.cleaned_data['ownername'])
            pg=upload.save(commit=False)
            pg.user=request.user
            pg.save()
            print('data inserted successfully')
            return HttpResponseRedirect('/dashboard')
    else:
        print("form is not validated")
        upload=UploadForm()
    document=UploadPG.objects.filter(user=request.user)
    return render(request,'pg/UploadForm.html',{'upload':upload,'document':document})


def signUpView(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            print("Form Validation Success....")
            user=form.save(commit=True)
            user.set_password(user.password)
            user.save()
            print('data inserted successfully')
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return HttpResponseRedirect('/accounts/login')
        else:
            print("form is not validated")
    return render(request,'pg/signup.html',{'form':form})

def homeView(request):
    return render(request,'pg/home.html')

class pgAroundKhrarView(ListView):
    model=UploadPG
    queryset = UploadPG.objects.filter(location='pgaroundkhrar')
    template_name='pg/pgAroundKhrar.html'
    context_object_name='pglist'
    paginate_by=2


class pgInKhrarView(ListView):
    model=UploadPG
    template_name='pg/pgInKhrar.html'
    queryset = UploadPG.objects.filter(location='pginkhrar')
    context_object_name='pglist'
    paginate_by=2

class roomDetailView(DetailView):
    model=UploadPG

    # template_name='pg/uploadpg.html'
    # context_object_name='pg_detail'


def tiffinView(request):

    return render(request,'pg/tiffin.html')

def teamView(request):

    return render(request,'pg/team.html')

def gallary1View(request):

    return render(request,'pg/gallary1.html')

def gallary2View(request):

    return render(request,'pg/gallary2.html')

def aboutView(request):

    return render(request,'pg/about.html',)

def contactView(request):

    return render(request,'pg/contact.html')

def logoutView(request):
    return render(request,'pg/logout.html')
#
# def uploadChoiceView(request):
#     return render(request,'pg/uploadchoice.html')
