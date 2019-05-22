from django.db import models
from datetime import datetime

import datetime

from PIL import Image
import os

from django.conf import settings
#Image Uploade for category function

# def uplaod_location(instance,filename):
# 	return "%s/%s.%s" %('documents/category-image/cover-image',instance.name,filename)
def uplaod_location_test(instance,filename):

	name=str(instance.name)

	image=Image.open(instance.image)

	orginal_dir=settings.MEDIA_ROOT +'/documents/category-image/orginal/'
	resized_dir=settings.MEDIA_ROOT +'/documents/category-image/resized/'

	orginal_dir_url='documents/category-image/orginal/'
	resized_dir_url='documents/category-image/resized/'
	ext=instance.image.name.split('.')
	ext=ext[len(ext)-1]
	file_name =name+datetime.datetime.now().strftime('%Y%m%d%h%s') + "." + ext

	if instance.image:
		if os.path.exists(resized_dir):
			pass
		else:
			path=os.path.join(resized_dir)
			os.makedirs(path)	

		if os.path.exists(orginal_dir):
			pass
		else:
			path=os.path.join(orginal_dir)
			os.makedirs(path)


		imaged_resized = image.resize((32, 32), Image.ANTIALIAS)
		imaged_resized.save(resized_dir+file_name)
		instance.resized_image=resized_dir_url+file_name


		imaged = image.resize((128, 128), Image.ANTIALIAS)
		# imaged.save(orginal_dir+file_name)
		path=orginal_dir_url+file_name

		
		
		return path 



def uplaod_location(instance,filename):
	ext=instance.cover_image.name.split('.')
	ext=ext[len(ext)-1]
	file_name =instance.name+datetime.datetime.now().strftime('%Y%m%d%h%s') + "." + ext

	return "%s/%s" %('documents/category-image/cover-image',file_name)	

class Category(models.Model):
		
		name=models.CharField(max_length=120)
		tagline=models.CharField(max_length=255,null=True,blank=True)
		image=models.ImageField(upload_to=uplaod_location_test, height_field="height_field",
			width_field="width_field",null=True,blank=True,max_length=500)
		resized_image=models.ImageField(height_field="height_field",
			width_field="width_field",null=True,blank=True,max_length=500)

		cover_image=models.ImageField(upload_to=uplaod_location,height_field="height_field",
			width_field="width_field",null=True,blank=True)
		cover_video=models.CharField(max_length=255,null=True,blank=True)
		
		descriptions=models.TextField(null=True)
		height_field=models.IntegerField(default=0,null=True,blank=True)
		width_field=models.IntegerField(default=0,null=True,blank=True)
		created_at=models.DateTimeField(auto_now=False,auto_now_add=True)
		updated_at=models.DateTimeField(auto_now=True,auto_now_add=False)

		class Meta:
			db_table ='categories'

		def __str__(self):
			return self.name

		def base_url(self):
			return settings.BASE_URL
		
		@property
		def cover_photo_url(self):
			print 'll o'
			if self.cover_image and hasattr(self.cover_image, 'url'):
				print 'll e'
				return "/" + self.cover_image.url

		@property
		def image_url(self):
			print 'll'
			if self.image and hasattr(self.image, 'url'):
				print 'llp'
				return "/" + self.image.url
			else:
				return None


		@property
		def resized_image_url(self):
			print 'll'
			if self.resized_image and hasattr(self.resized_image, 'url'):
				print 'llp'
				return "/" + self.resized_image.url
			else:
				return None

