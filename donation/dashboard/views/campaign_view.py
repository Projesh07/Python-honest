# Create your views here.
from formtools.wizard.views import SessionWizardView
from django.shortcuts import render_to_response
from django.shortcuts import redirect
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User


from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import ListView,TemplateView,DetailView
from campaign.models import Campaign,Tag,Documents,Category,Donate
from django.core.urlresolvers import reverse

from campaign.forms.campaign_forms import CampaignForm,CampaignForm2
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import json
from django.http import JsonResponse, HttpResponse
from dashboard.tables.tables import CampaignTable,PaymentCampaignTable,PaymentUserTable,HighlightedCampaignTable
from django.template.defaultfilters import slugify
from table.views import FeedDataView
import datetime
import urllib

from PIL import Image


class CampaignList(TemplateView):
	model=Campaign
	template_name='campaign/campaign_list.html'
	form_class = CampaignForm

	def get_context_data(self,**kwargs):
		context=super(CampaignList,self).get_context_data(**kwargs)
		# context['categories']=Category.objects.all()
		page_title="Campaign List"
		context['title']=page_title
		context['url_create']='create_campaign'
		context['breadcrumb']='Create'
		context['url_delete']='delete_campaign'
		context['url_update']='update_campaign'
		form_val=self.request.GET.get('search')
		context['campaign_table']=CampaignTable()

		context["form"] = CampaignForm()  # instance= None

		# print settings.MEDIA_URL
		today_date = datetime.datetime.now().strftime('%Y-%m-%d')
		context["today_date"] = datetime.datetime.now().strftime('%d %B')
		context["today_day"] = datetime.datetime.now().strftime('%A')
		context['ongoing_camp_today'] = Campaign.objects.filter(status=1,start_date__lte=today_date, end_date__gte=today_date)
		context["tags"] =Tag.objects.all()

		if form_val:
			context['campaignes']=Campaign.objects.filter(title__icontains=form_val)
		else:
			context['campaignes']=Campaign.objects.all()
		return context

		def get_success_url(self):
			return reverse('list_campaign')

	def post(self, request, *args, **kwargs):
		context = super(CampaignList,self).get_context_data(**kwargs)
		# context['form'] = CampaignForm(self.request.POST,self.request.FILES or None);
		form = CampaignForm(self.request.POST,self.request.FILES or None);

		# if context["form"].is_valid():
		if form.is_valid():
			# context["form"].save(commit=False)
			# campaign=context["form"].save()
			form.save(commit=False)
			campaign=form.save()
			return redirect('update_campaign/' + campaign.id)		


		return super(CampaignList, self).render_to_response(context)

class CampaignTableList(FeedDataView):

    token = CampaignTable.token

    def get_queryset(self):

    	if self.request.GET.get('is_highlighted'):
    		return super(CampaignTableList, self).get_queryset().filter(is_highlighted=1)
        
        return super(CampaignTableList, self).get_queryset()	


class HighlightedCampaignList(ListView):
	model=Campaign
	template_name='campaign/highlighted_list.html'
		
	def get_context_data(self,**kwargs):
		context=super(HighlightedCampaignList,self).get_context_data(**kwargs)
		# context['categories']=Category.objects.all()
		page_title="Highlighted Campaign List"
		context['title']=page_title
		context['url_create']='create_campaign'
		context['breadcrumb']='Highlighted'
		context['url_delete']='delete_campaign'
		context['url_update']='update_campaign'
		form_val=self.request.GET.get('search')
		context['campaign_table']=HighlightedCampaignTable()

		# print settings.MEDIA_URL
		today_date = datetime.datetime.now().strftime('%Y-%m-%d')
		context["today_date"] = datetime.datetime.now().strftime('%d %B')
		context["today_day"] = datetime.datetime.now().strftime('%A')
		# context['ongoing_camp_today'] = Campaign.objects.filter(status=1,start_date__lte=today_date, end_date__gte=today_date)
		

		# if form_val:
		# 	context['campaignes']=Campaign.objects.filter(title__icontains=form_val,is_highlighted=1)
		# else:
		# 	context['campaignes']=Campaign.objects.filter(is_highlighted=1)
		return context

class HighlightedCampaignTableList(FeedDataView):

    token = HighlightedCampaignTable.token

    def get_queryset(self):
    		return super(HighlightedCampaignTableList, self).get_queryset().filter(is_highlighted=1)
	


class CampaignCreate(TemplateView):
	# form_list = [CampaignForm]
	# template_name='campaign/crud.html'
	template_name='campaign/campaign_create.html'
	form_class = CampaignForm

	# /media_cdn/documents/

	def post(self, request, *args, **kwargs):
		context = self.get_context_data()
		context['form'] = CampaignForm(self.request.POST,self.request.FILES or None);
		links =self.request.POST.getlist('link[]')
		# documents= self.request.POST.getlist('document[]') request.FILES['file']
		documents= self.request.FILES.getlist('document[]')
		images= self.request.FILES.getlist('image[]')
		tags=self.request.POST.getlist('tags_val[]')
		
		cover_image= self.request.FILES.get('cover_image')
		cover_video_link= self.request.POST.get('cover_video')

		# print self.request.POST
		
		if context["form"].is_valid():

			# context["form"].fields.slug = slugify(self.request.POST.get('title'))
			
			context["form"].save(commit=False)
			campaign=context["form"].save()
			c_id=campaign.id

			print 'self.request.POST'

			if links is not None:
				for link in links:				
					content_type='link'
					Documents.objects.create(content=link,content_type=content_type,campaign_id=c_id)
			
			if documents is not None:
				for document in documents:
					content_type='file'
					dirname=settings.MEDIA_ROOT + '/documents/campaign-file'

					if os.path.exists(dirname):
						pass

					else:
						os.mkdir(os.path.join('/file', dirname))

					fs = FileSystemStorage(location=dirname)

					ext = document.name.split('.')
					ext = ext[ len(ext) - 1 ]
				
					file_name = str(c_id) + datetime.datetime.now().strftime('%Y%m%d%h%s') + "." + ext
					uploaded_file_url= settings.MEDIA_URL +  'documents/campaign-file/'+ file_name
					
				
					fname=fs.save(file_name,document)
					
					# uploaded_file_url='documents/campaign-file/'+document.name				
					
					Documents.objects.create(content=uploaded_file_url,content_type=content_type,campaign_id=c_id)			
			
			if images is not None:
				dirname=settings.MEDIA_ROOT + '/documents/campaign-image/orginal/'
				dirname2=settings.MEDIA_ROOT + '/documents/campaign-image/resize/'
				if os.path.exists(dirname):
					print "os exists"
					pass

				else:
					#os.mkdir(os.path.join('/image', dirname))
					print "dirname"
					path=os.path.join(dirname)
					os.makedirs(path)

				if os.path.exists(dirname2):
					pass
					print "os  exists 2"
				else:
					print "dirname2"
					# os.mkdir(os.path.join('/image', dirname))
					path=os.path.join(dirname2)
					os.makedirs(path)



				for image in images:
					content_type='image'
					image2=Image.open(image)
					# fs = FileSystemStorage(location=dirname)
				
					ext = image.name.split('.')
					ext = ext[ len(ext) - 1 ]
					file_name = str(c_id) + datetime.datetime.now().strftime('%Y%m%d%h%s') +"."+ ext
					uploaded_file_url= settings.MEDIA_URL +  'documents/campaign-image/orginal/'+ file_name
					uploaded_file_resized_url= settings.MEDIA_URL +  'documents/campaign-image/resize/'+ file_name
								
					# fname=fs.save(file_name,image)
					imaged_resized = image2.resize((324, 216), Image.ANTIALIAS)
					imaged_resized.save(dirname+file_name)

					# imaged_resized = image2.resize((128, 128), Image.ANTIALIAS)
					# imaged_resized.save(dirname2+file_name)
					Documents.objects.create(content_resized=uploaded_file_resized_url,content=uploaded_file_url,content_type=content_type,campaign_id=c_id)			


			if tags is not None:
				for tag in tags:

					if not tag.isnumeric():
						new_tag = Tag.objects.create(name=tag)
						campaign.tags.add(new_tag)
					else:
						tag = Tag.objects.get(id=tag)
						campaign.tags.add(tag)

			return redirect('update_campaign',id= campaign.id)	


		return super(CampaignCreate, self).render_to_response(context)


	def get_context_data(self, **kwargs):
		context = super(CampaignCreate, self).get_context_data(**kwargs)
		
		page_title="Campaign Create"
		context['title']=page_title

		form = CampaignForm()  # instance= None
	
		tag_db=Tag.objects.all()
		context["form"] = form
		context['tags']=tag_db


		return context

	def render_to_response(self, context, **response_kwargs):

		if self.request.is_ajax():
			tag=self.request.GET.get('select_val')
			# if not Tag.objects.filter(name=tag).exists():
			# 	Tag.objects.create(name=tag)	
			return JsonResponse(json.dumps(tag),safe=False, **response_kwargs)
		else:
			return super(CampaignCreate,self).render_to_response(context, **response_kwargs)


class AJAXDocumentDelete(TemplateView):

	template_name=None

	def post(self, request, *args, **kwargs):
		response_data={}
		if self.request.is_ajax():
			file_id = request.POST.get('file_id')
			
			if Documents.objects.filter(id=file_id).exists():
				file = Documents.objects.get(id=file_id)
				Documents.objects.filter(id=file_id).delete()
				response_data['success'] = True
				from django.core import serializers
				# unlink( settings.MEDIA_ROOT + file.content )
				try:
				    os.remove(settings.MEDIA_ROOT + file.content)
				except OSError:
				    pass
				# response_data['file']=serializers.serialize('json', [file])
				# response_data['file']=json.dumps(file)
				response_data['file_path']=json.dumps(settings.MEDIA_ROOT + file.content)
			else:
				response_data['success'] = False
		else:
			response_data['success'] = False
		return HttpResponse(json.dumps(response_data), content_type="application/json")	
	# def render_to_response(self, context, **response_kwargs):

	# 	if self.request.is_ajax():
	# 		file_id = self.request.POST.get('file_id')
	# 		if Document.objects.filter(id=file_id).exists():
	# 			file = Document.objects.filter(id=file_id)
	# 			print file
	# 			response_data={}
	# 			response_data['success'] = True
	# 			response_data['file']=file
	# 			return HttpResponse(json.dumps(response_data), content_type="application/json")
	# 		else:
	# 			return JsonResponse(json.dumps([('supccess', False) ]),safe=False, **response_kwargs)
	# 	else:
	# 		return JsonResponse(json.dumps([('succesis', False) ]),safe=False, **response_kwargs)

	

class CampaignUpdate(TemplateView):

	template_name='campaign/campaign_update.html'

	def get_context_data(self,**kwargs):

		context = super(CampaignUpdate, self).get_context_data(**kwargs)
		camp=Campaign.objects.get(id=self.kwargs['id'])
		form = CampaignForm(self.request.POST or None,self.request.FILES or None,instance=camp)  # instance= None
		context["form"] = form

		page_title="Campaign Update"
		context['title']=page_title
		context['breadcrumb']='Update'

		context['campaign']=camp

		context['documents']=Documents.objects.filter(campaign_id=self.kwargs['id'])
		feature_image = Documents.objects.filter(campaign_id=self.kwargs['id'],is_featured = 1)
		cover_image = Documents.objects.filter(campaign_id=self.kwargs['id'],content_type='cover_image')
		cover_video_link = Documents.objects.filter(campaign_id=self.kwargs['id'],content_type='cover_video_link')
		context['featured_image_path'] = "" if not feature_image else feature_image[0].base_url() + feature_image[0].content
		context['cover_image_path'] = "" if not cover_image else cover_image[0].base_url() + cover_image[0].content
		context['cover_video_path'] = "" if not cover_video_link else cover_video_link[0].content
		
		context['featured_image'] = None if not feature_image else feature_image[0]

		tag = camp.tags.all()
		context["camp_tags"]=tag

		context["tags"] =Tag.objects.all()
		
		return context

	def post(self, request, *args, **kwargs):

		context = self.get_context_data()
		links =self.request.POST.getlist('link[]')
		vidlinks =self.request.POST.getlist('vidlink[]')
		documents= self.request.FILES.getlist('document[]')
		
		images= self.request.FILES.getlist('image[]')

		tags=self.request.POST.getlist('tags_val[]')

		cover_image= self.request.FILES.get('cover_image')
		cover_video_link= self.request.POST.get('cover_video')

		print self.request.FILES.get('is_highlighted')

		if context["form"].is_valid():

			print 'lol'
			
			context["form"].save(commit=False)
			# print context["form"].fields.slug
			campaign=context["form"].save()
			c_id=campaign.id

			print cover_video_link

			# deleting existing links for restore.. 
			Documents.objects.filter(campaign_id=c_id,content_type='link').delete()
			Documents.objects.filter(campaign_id=c_id,content_type='videolink').delete()

			# campaign video link update.
			if cover_video_link is not None:
				Documents.objects.filter(content_type='cover_video_link',campaign_id=c_id).delete()
				Documents.objects.create(content=cover_video_link,content_type='cover_video_link',campaign_id=c_id)

			# campaign cover image update.

			if cover_image is not None:
				dirname=settings.MEDIA_ROOT + '/documents/campaign-image/orginal/'
				dirname2=settings.MEDIA_ROOT + '/documents/campaign-image/resize/'
				if os.path.exists(dirname):
					print "os exists"
					pass

				else:
					#os.mkdir(os.path.join('/image', dirname))
					print "dirname"
					path=os.path.join(dirname)
					os.makedirs(path)

				if os.path.exists(dirname2):
					pass
					print "os  exists 2"
				else:
					print "dirname2"
					# os.mkdir(os.path.join('/image', dirname))
					path=os.path.join(dirname2)
					os.makedirs(path)

				content_type='cover_image'
				image2=Image.open(cover_image)
				# fs = FileSystemStorage(location=dirname)
			
				ext = cover_image.name.split('.')
				ext = ext[ len(ext) - 1 ]
				file_name = str(c_id) + datetime.datetime.now().strftime('%Y%m%d%h%s') +"."+ ext
				uploaded_file_url= settings.MEDIA_URL +  'documents/campaign-image/orginal/'+ file_name
				uploaded_file_resized_url= settings.MEDIA_URL +  'documents/campaign-image/resize/'+ file_name
							
				# fname=fs.save(file_name,image)
				imaged_resized = image2.resize((960, 350), Image.ANTIALIAS)
				imaged_resized.save(dirname+file_name)

				imaged_resized = image2.resize((128, 128), Image.ANTIALIAS)
				imaged_resized.save(dirname2+file_name)
				Documents.objects.create(content_resized=uploaded_file_resized_url,content=uploaded_file_url,content_type=content_type,campaign_id=c_id)			


			if links is not None:
				for link in links:
				
					content_type='link'
					Documents.objects.create(content=link,content_type=content_type,campaign_id=c_id)

			if vidlinks is not None:
				for link in vidlinks:
				
					content_type='videolink'
					link = link.replace("watch?v=","embed/")
					Documents.objects.create(content=link,content_type=content_type,campaign_id=c_id)
			
			if documents is not None:
				for document in documents:
					content_type='file'
					dirname=settings.MEDIA_ROOT + '/documents/campaign-file'
					# print document.type

					if os.path.exists(dirname):
						pass

					else:
						os.mkdir(os.path.join('/file', dirname))

					fs = FileSystemStorage(location=dirname)

					ext = document.name.split('.')
					ext = ext[ len(ext) - 1 ]
				
					file_name = str(c_id) + datetime.datetime.now().strftime('%Y%m%d%h%s') + "." + ext
					uploaded_file_url= settings.MEDIA_URL +  'documents/campaign-file/'+ file_name
					
					fname=fs.save(file_name,document)

					# print 'test : ' + fname


				
					Documents.objects.create(content=uploaded_file_url,content_type=content_type,campaign_id=c_id)			
			
			if images is not None:
				dirname=settings.MEDIA_ROOT + '/documents/campaign-image/orginal/'
				dirname2=settings.MEDIA_ROOT + '/documents/campaign-image/resize/'
				if os.path.exists(dirname):
					print "os exists"
					
					pass

				else:
					#os.mkdir(os.path.join('/image', dirname))
					print "dirname"
					path=os.path.join(dirname)
					os.makedirs(path)

				if os.path.exists(dirname2):
					pass
					print "os  exists 2"
				else:
					print "dirname2"
					# os.mkdir(os.path.join('/image', dirname))
					path=os.path.join(dir)
				for image in images:
					content_type ='image'
					is_featured = 1
					image2=Image.open(image)

					ext = image.name.split('.')
					ext = ext[ len(ext) - 1 ]

					file_name = str(c_id) + datetime.datetime.now().strftime('%Y%m%d%h%s') +"."+ ext
					uploaded_file_url= settings.MEDIA_URL +  'documents/campaign-image/orginal/'+ file_name
					uploaded_file_resized_url= settings.MEDIA_URL +  'documents/campaign-image/resize/'+ file_name
								
					# fname=fs.save(file_name,image)
					imaged_resized = image2.resize((324, 216), Image.ANTIALIAS)
					imaged_resized.save(dirname+file_name)

					# imaged_resized = image2.resize((128, 128), Image.ANTIALIAS)
					# imaged_resized.save(dirname2+file_name)
					Documents.objects.filter(campaign_id=c_id).update(is_featured=0)
					Documents.objects.create(content_resized=uploaded_file_resized_url,content=uploaded_file_url,content_type=content_type,campaign_id=c_id,is_featured = is_featured )			

			if tags is not None:
				print 'after tags'
				# print tags[2]
				used_tag_list = []
				for tag in tags:
					if not tag.isnumeric():
						new_tag = Tag.objects.filter(name=tag)
						if not new_tag.exists():
							new_tag = Tag.objects.create(name=tag)
							print new_tag.id
						else:
							new_tag = new_tag[0].id						
						campaign.tags.add(new_tag)
						used_tag_list.append(int(new_tag.id))
					else:
						if not campaign.tags.filter(id=tag,campaign__id=c_id).exists():
							campaign.tags.add(tag)
						used_tag_list.append(int(tag))
				# used_tag_lis = [49]
				print used_tag_list
				print campaign.tags.filter(campaign__id=c_id).exclude(id__in=used_tag_list).delete()


			return redirect('update_campaign_photos',id=c_id )		


		return super(CampaignUpdate, self).render_to_response(context)


		# def get_success_url(self,**kwargs):
		# 	return reverse('update_campaign_photos')

class CampaignUpdatePhotos(TemplateView):
	
	template_name='campaign/campaign_update_photos.html'

	def get_context_data(self,**kwargs):

		context = super(CampaignUpdatePhotos, self).get_context_data(**kwargs)
		camp=Campaign.objects.get(id=self.kwargs['id'])
		form = CampaignForm(self.request.POST or None,self.request.FILES or None,instance=camp)  # instance= None
		context["form"] = form

		page_title="Campaign Gallery"
		context['title']=page_title

		context['campaign']=camp
		
		context['documents']=Documents.objects.filter(campaign_id=self.kwargs['id'])
		
		return context

	def post(self, request, *args, **kwargs):
		response_data={}
		if self.request.is_ajax():
			image = request.FILES.get('file')
			campaign_id = self.kwargs['id']

			ext = image.name.split('.')
			ext = ext[ len(ext) - 1 ]

			print campaign_id

			file = None

			if image is not None and ext in ['png','PNG','jpg','JPG','jpeg','JPEG','bmp','BMP']:
				dirname=settings.MEDIA_ROOT + '/documents/campaign-image/orginal/'
				dirname2=settings.MEDIA_ROOT + '/documents/campaign-image/resize/'
				if os.path.exists(dirname):
					print "os exists"
					
					pass

				else:
					#os.mkdir(os.path.join('/image', dirname))
					print "dirname"
					path=os.path.join(dirname)
					os.makedirs(path)

				if os.path.exists(dirname2):
					pass
					print "os  exists 2"
				else:
					print "dirname2"
					# os.mkdir(os.path.join('/image', dirname))
					path=os.path.join(dir)

				#saving image
				content_type='image'
				image2=Image.open(image)

				ext = image.name.split('.')
				ext = ext[ len(ext) - 1 ]
				file_name = str(campaign_id) + datetime.datetime.now().strftime('%Y%m%d%h%s') +"."+ ext
				uploaded_file_url= settings.MEDIA_URL +  'documents/campaign-image/orginal/'+ file_name
				uploaded_file_resized_url= settings.MEDIA_URL +  'documents/campaign-image/resize/'+ file_name
							
				# fname=fs.save(file_name,image)
				imaged_resized = image2.resize((324, 216), Image.ANTIALIAS)
				imaged_resized.save(dirname+file_name)

				# imaged_resized = image2.resize((128, 128), Image.ANTIALIAS)
				# imaged_resized.save(dirname2+file_name)
				file = Documents.objects.create(content_resized=uploaded_file_resized_url,content=uploaded_file_url,content_type=content_type,campaign_id=campaign_id)			

			elif image is not None and ext in ['pdf','PDF','CSV','csv','xls','XLS','XLSX','xlsx']:
					
				document = image
				content_type='file'
				dirname=settings.MEDIA_ROOT + '/documents/campaign-file'
				# print document.type

				if os.path.exists(dirname):
					pass

				else:
					os.mkdir(os.path.join('/file', dirname))

				fs = FileSystemStorage(location=dirname)

				ext = document.name.split('.')
				ext = ext[ len(ext) - 1 ]
			
				file_name = str(campaign_id) + datetime.datetime.now().strftime('%Y%m%d%h%s') + "." + ext
				uploaded_file_url= settings.MEDIA_URL +  'documents/campaign-file/'+ file_name
				
				fname=fs.save(file_name,document)
		
				file = Documents.objects.create(content=uploaded_file_url,content_type=content_type,campaign_id=campaign_id)			
		
			
			if file:
				response_data['success'] = True
				response_data['message'] = 'exists'
				
				response_data['file_path']=json.dumps(settings.MEDIA_ROOT + file.content)
			else:
				response_data['success'] = False
				response_data['message'] = 'not exits'
		else:
			response_data['success'] = False

		return HttpResponse(json.dumps(response_data), content_type="application/json")	
		
class CampaignDelete(DeleteView):

		template_name='campaign/confirm_delete.html'
		title = 'Campaign Delete'

		form_class=CampaignForm
		def get_object(self,**kwargs):

			return Campaign.objects.get(id=self.kwargs['id'])

		def get_success_url(self):
			return reverse('list_campaign')

class CampaignStatus(TemplateView):

		template_name='campaign/confirm_status.html'
		# model=Campaign
		def get_context_data(self,**kwargs):

			context = super(CampaignStatus, self).get_context_data(**kwargs)
			context['campaign']=Campaign.objects.get(id=self.kwargs['id'])	
			context['title']="Change Status"
			context['breadcrumb']='Change Status'

			return context		

	
		def post(self, request, *args, **kwargs):
			campaigns=Campaign.objects.get(id=self.kwargs['id'])

			if campaigns.status==0:
	
				campaigns.status=1
			else:

				campaigns.status=0
	
			campaigns.save()

			return redirect('list_campaign')



		def get_success_url(self):
			return reverse('list_campaign')			

class CampaignDetails(DetailView):
    model = Campaign
    template_name = 'campaign/campaign_detail_view.html'


    def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(CampaignDetails, self).get_context_data(**kwargs)
		page_title="Campaign Details"
		context['title']=page_title
		context['breadcrumb']='Details'
		# print context['campaign'].id

		context['documents']=Documents.objects.filter(campaign_id=context['campaign'].id)
		f=Documents.objects.filter(campaign_id=context['campaign'].id,is_featured=1)
		if f:
			context['featured_image'] = f[0]
		# context["tags"] =Tag.objects.all()
		# print context
		# context['now'] = timezone.now()
		return context		

class PaymentList(ListView):
	model = Donate
	template_name='donate/payment_list.html'

	def get_context_data(self,**kwargs):
		page_title="Payment List"
		context=super(PaymentList,self).get_context_data(**kwargs)
		
		# context['users']=User.objects.all()
		# print self.kwargs

		# data = Donate.objects.get(campaign_id=self.kwargs['campaign'])

		# print data

		if self.kwargs and 'campaign' in self.kwargs:
			name=Campaign.objects.get(id=self.kwargs['campaign'])
	
			data = Donate.objects.filter(campaign_id=self.kwargs['campaign'])
			total_donate=Donate.total_donate(condition='campaign',id_val=self.kwargs['campaign'])
			total_donate_number=Donate.total_donate_number(condition='campaign',id_val=self.kwargs['campaign'])
			context['payment_table']=PaymentCampaignTable(data)
			context['breadcrumb']= [('list_campaign','','Campaign'),('campaign_details',name.id,name.title)]
			# context['breadcrumb']= [('list_site_user','Users'),('"list_site_user" ','user')]
		

		elif self.kwargs and 'user' in self.kwargs:
			name=User.objects.get(id=self.kwargs['user'])
		
			data = Donate.objects.filter(user_id=self.kwargs['user'])
	
			total_donate=Donate.total_donate(condition='user',id_val=self.kwargs['user'])
			total_donate_number=Donate.total_donate_number(condition='user',id_val=self.kwargs['user'])
			context['payment_table']=PaymentUserTable(data)
			context['breadcrumb']= [('list_site_user','','Users'),('payment_user_list',name.id,name.username)]
		
		context['title']=page_title
		context['name']=name
		context['total_donate']=total_donate
		context['total_donate_number']=total_donate_number		

		return context

class PaymentUserTableList(PaymentList,FeedDataView):

    token = PaymentUserTable.token

    def get_queryset(self):
        return super(PaymentUserTableList, self).get_queryset()	


class PaymentCampaignTableList(PaymentList,FeedDataView):

    token = PaymentCampaignTable.token

    def get_queryset(self):
        return super(PaymentCampaignTableList, self).get_queryset()	


