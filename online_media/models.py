from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Picture(models.Model):
    picture = models.ImageField(upload_to = "pictures/",null = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    picture_name = models.CharField(max_length = 30,null = True)
    likes = models.IntegerField(default=0)
    picture_caption = models.TextField(null = True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    comments = models.IntegerField(default=0)


    def __str__(self):
    	return self.picture_name

    def delete_picture(self):
    	self.delete()

    def save_picture(self):
    	self.save()

    def update_caption(self,new_caption):
    	self.picture_caption = new_caption
    	self.save()


    @classmethod
    def get_pictures_by_user(cls,id):
        sent_pictures = Picture.objects.filter(user_id=id)
        return sent_pictures

    @classmethod
    def get_pictures_by_id(cls,id):
        fetched_picture = Picture.objects.get(id = id)
        return  fetched_picture

    class Meta:
    	ordering = ['-pub_date']


    def __str__(self):
    	return self.user.username

    def save_profile(self):
    	self.save()

class Profile(models.Model):
	username = models.CharField(default='User',max_length=30)
	profile_picture = models.ImageField(upload_to = "profile/",null=True)
	bio = models.TextField(default='',blank = True)
	first_name = models.CharField(max_length =30)
	last_name = models.CharField(max_length =30)

	def __str__(self):
		return self.username

	def delete_profile(self):
		self.delete()

	def save_profile(self):
		self.save()

	@classmethod
	def search_profile(cls,search_term):
		got_profiles = cls.objects.filter(first_name__icontains = search_term)
		return got_profiles
        
class Comment(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	picture = models.ForeignKey(Picture,on_delete=models.CASCADE,null= True,related_name='comment')
	comment= models.TextField( blank=True)
	
	def __str__(self):
		return self.comment


	def delete_comment(self):
		self.delete()

	def save_comment(self):
		self.save()

class Follow(models.Model):
	user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
	follower = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

	def __int__(self):
		return self.name

	def save_follower(self):
		self.save()

	def delete_follower(self):
		self.save()

class Unfollow(models.Model):
	user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
	follower = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

	def __int__(self):
		return self.name

class Likes(models.Model):
	user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
	

	def __int__(self):
		return self.name

	def unlike(self):
		self.delete()

	def save_like(self):
		self.save()
# Create your models here.
