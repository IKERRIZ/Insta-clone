from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Image, Profile
from .forms import ProfileForm,ImageForm


# Create your views here.
@login_required(login_url='/account/login/')
def home(request):
    current_user = request.user
    all_images = Image.objects.all()
    
    return render(request,'home.html',{"all_images":all_images,"user":current_user})


@login_required(login_url='accounts/logi    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
n/')
def add_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()
        
            return redirect('home')
    else:
        form = ImageForm()


    return render(request,'image.html',{"form":form})


@login_required(login_url='/login')
def profile(request):
    current_user = request.user
    profile_details = Profile.objects.get(owner_id=current_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.owner = current_user
            profile.save()
    else:
        form=ProfileForm()
    return render(request, 'profile/new.html', {'form':form})

@login_required(login_url='/accounts/login/')
def display_profile(request, id):
    seekuser=User.objects.filter(id=id).first()
    profile = seekuser.profile
    profile_details = Profile.get_by_id(id)
    images = Image.get_profile_images(id)
    # print(images)
    print(profile.owner.id)
    print(request.user.id)

    return render(request,'profile/profile.html',{"profile_details":profile_details,"profile":profile,"images":images}) 
def search(request):
    profiles = User.objects.all()

    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        print(results)

        return render(request,'results.html', {'results': results,"profiles":profiles})

    return redirect(home