
from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from category.models import Category
from django.core.urlresolvers import reverse

from dashboard.tables.tables import CategoryTable
from django.http import JsonResponse, HttpResponse

from category.forms.category_forms import CategoryForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from table.views import FeedDataView 
import datetime

from PIL import Image
import os
import json

from django.conf import settings


class CategoryList(TemplateView):

	def get(self, request, *args, **kwargs):
		page_title="Category List"
		context=super(CategoryList,self).get_context_data(**kwargs)
		# context['categories']=Category.objects.all()
		context['title']=page_title
		context['breadcrumb']='List'
		context['url_create']='create_category'
		context['url_delete']='delete_category'
		context['url_update']='update_category'
		form_val=self.request.GET.get('search')

		# if form_val:
		# 	context['categories']=Category.objects.filter(name__icontains=form_val)
		# else:
		# 	# pass
		# 	context['categories']=Category.objects.all()
		
		context['categories']=CategoryTable()
		# return context
		return render(request,"category/category_list.html",context)	

class CategoryTableList(FeedDataView):

        token = CategoryTable.token

        def get_queryset(self):
			return super(CategoryTableList, self).get_queryset()		


class CategoryCreate(CreateView):
		# template_name='category/crud_form.html'
		model = Category
		# fields =['name']
		form_class=CategoryForm
		def get(self, request, *args, **kwargs):
			self.object = None
			page_title="Category Create"
			context=super(CategoryCreate,self).get_context_data(**kwargs)
			# context['categories']=Category.objects.all()
			context['title']=page_title
			context['breadcrumb']='Create'

			return render(request,"category/crud_form.html",context)		

		def get_success_url(self):
			return reverse('list_category')
			
class CategoryUpdate(UpdateView):

		# template_name='category/crud_form.html'
		form_class=CategoryForm
		def get_object(self, **kwargs):
			return Category.objects.get(id=self.kwargs['id'])

		def get(self, request, *args, **kwargs):
			self.object = Category.objects.get(id=self.kwargs['id'])
			page_title="Category Update"
			context=super(CategoryUpdate,self).get_context_data(**kwargs)
			context['category']=self.object
			context['title']=page_title
			context['breadcrumb']='Update'

			return render(request,"category/crud_form.html",context)	
			
		def get_success_url(self,**kwargs):
			return reverse('list_category')

class CategoryDelete(DeleteView):

		template_name='category/delete_confirm.html'

		form_class=CategoryForm
		def get_object(self,**kwargs):

			return Category.objects.get(id=self.kwargs['id'])

		def get_success_url(self):
			return reverse('list_category')


class AJAXCategoryDocumentDelete(TemplateView):

	template_name=None

	def post(self, request, *args, **kwargs):
		response_data={}
		if self.request.is_ajax():
			file_id = request.POST.get('file_id')
			image_type = request.POST.get('image_type')

			print file_id
			print image_type
			
			if Category.objects.filter(id=file_id).exists():
				file = Category.objects.get(id=file_id)
				if image_type and image_type == 'image':					
					Category.objects.filter(id=file_id).update(image="",resized_image="")
					file_path = file.image
					file_path_rs = file.resized_image
				elif image_type and image_type == 'cover_image':
					Category.objects.filter(id=file_id).update(cover_image="")
					file_path = file.cover_image
					file_path_rs = None

				response_data['success'] = True

				try:
				    os.remove(settings.MEDIA_ROOT + str(file_path) )
				    if file_path_rs:
				    	os.remove(settings.MEDIA_ROOT + str(file_path_rs) )

				except OSError:
				    pass
				# response_data['file']=serializers.serialize('json', [file])
				# response_data['file']=json.dumps(file)
				response_data['file_path']=json.dumps(settings.MEDIA_ROOT + str(file_path) )
			else:
				response_data['success'] = False
		else:
			response_data['success'] = False
		return HttpResponse(json.dumps(response_data), content_type="application/json")	
	
	