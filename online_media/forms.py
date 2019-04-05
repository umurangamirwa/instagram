from django import forms
from .models import Comment,Profile,Image
from django.contrib.auth.forms import AuthenticationForm

class ProfileForm(forms.ModelForm):
	model = Profile
	username = forms.CharField(label='Username',max_length = 30)
	
	bio = forms.CharField(label='Image Caption',max_length=500)
	profile_picture = forms.ImageField(label = 'Image Field')


class ProfileUploadForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		exclude = ['user']

class RatingForm(forms.ModelForm):
	class Meta:
		model = Comment
		
		exclude = ['user','picture',]
class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		
		exclude = ['user']

class ImageUploadForm(forms.ModelForm):
	class Meta:
		model = Image
		
		exclude = ['user']
