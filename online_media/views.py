from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . forms import ProfileUploadForm,CommentForm,ProfileForm
from django.http  import HttpResponse
from . models import Picture ,Profile, Likes, Follow, Comment,Unfollow
from django.conf import settings


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
      title = 'Instagram'
      picture_posts = Picture.objects.all()
      
      print(picture_posts)
      return render(request, 'index.html', {"title":title,"picture_posts":picture_posts})


@login_required(login_url='/accounts/login/')
def comment(request,id):
	
	post = get_object_or_404(Picture,id=id)	
	current_user = request.user
	print(post)

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = current_user
			comment.picture = post
			comment.save()
			return redirect('index')
	else:
		form = CommentForm()

	return render(request,'comment.html',{"form":form})  


@login_required(login_url='/accounts/login/')
def profile(request):
	 current_user = request.user
	 profile = Profile.objects.all()
	 follower = Follow.objects.filter(user = profile)

	 return render(request, 'profile.html',{"current_user":current_user,"profile":profile,"follower":follower})

@login_required(login_url='/accounts/login/')
def timeline(request):
	current_user = request.user 
	Myprofile = Profile.objects.order_by('-time_uploaded')
	comment = Comment.objects.order_by('-time_comment')
	

	return render(request, 'media/timeline.html',{"Myprofile":Myprofile,"comment":comment})

@login_required(login_url='/accounts/login/')
def single_picture(request,picture_id):
	picture = picture.objects.get(id= picture_id)

	return render(request, 'media/single_picture.html',{"picture":picture})

@login_required(login_url='/accounts/login/')
def like(request,pic_id):
	Picture = Picture.objects.get(id=picture_id)
	like +=1
	save_like()
	return redirect(timeline)

def search_results(request):
    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        searched_profiles = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search_picture.html',{"message":message,"pictures": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search_picture.html',{"message":message})


@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user 
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                
                requested_profile.profile_pic = form.cleaned_data['profile_picture']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.username = form.cleaned_data['username']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()
    except:
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(profile_picture = form.cleaned_data['profile_picture'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()


    return render(request,'upload_profile.html',{"title":title,"current_user":current_user,"form":form})

@login_required(login_url='/accounts/login/')
def upload_images(request):
    current_user = request.user 
    title = 'Upload Images'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES)

            if form.is_valid():
                
                requested_profile.profile_pic = form.cleaned_data['profile_picture']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.username = form.cleaned_data['username']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileForm()
    except:
        if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(profile_picture = form.cleaned_data['profile_picture'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect( images )
        else:
            form = ProfileForm()


    return render(request,'upload_profile.html',{"title":title,"current_user":current_user,"form":form})




