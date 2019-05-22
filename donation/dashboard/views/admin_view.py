from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.views.generic import ListView,TemplateView
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from dashboard.forms.user_forms import UserForm
from dashboard.forms.user_forms import UserEditForm,UserChangePasswordForm
from django.contrib.auth.forms import PasswordChangeForm

from dashboard.tables.tables import AdminUserTable
from django.db.models import Q
from table.views import FeedDataView 

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages



# class Admin():

# 	def user_group(self, *args,**kwargs):
# 		group=Group.objects.all()
# 		return group

# 	def users(self, *args,**kwargs):
# 		users=User.objects.all()
# 		return users	

#.......................................


# User list view

class UserList(ListView):
	model = User

	template_name='admin/user_list.html'
	def get_context_data(self,**kwargs):
		page_title="List"
		context=super(UserList,self).get_context_data(**kwargs)
		context['users']=User.objects.all()
		context['breadcrumb']=page_title
		context['title']="Admin list"
		context['admin_table']=AdminUserTable(User.objects.all().filter(Q(is_superuser=1) | Q(is_staff=1)))

		return context

class UserTableList(FeedDataView):
	
        token = AdminUserTable.token
        
        def get_queryset(self):
        	print "ccc"
        	return super(UserTableList, self).get_queryset().filter(Q(is_superuser=1) | Q(is_staff=1))
            

class UserCreate(CreateView):
	template_name='admin/user_crud_form.html'
	form_class=UserForm

	def get_context_data(self,**kwargs):
		context=super(UserCreate,self).get_context_data(**kwargs)
		context['title']="Admin Create"
		context['breadcrumb']="Create"
		return context

	def get_success_url(self):
		return reverse('list_user')

class UserUpdate(UpdateView):
	template_name='admin/user_crud_form.html'
	# model = User
	form_class=UserForm

	def get_context_data(self,**kwargs):
		context=super(UserUpdate,self).get_context_data(**kwargs)
		context['title']="Admin Update"
		context['breadcrumb']="Update"
		return context
	
	def get_object(self):
		user = User.objects.get(id=self.kwargs['id'])
		return user
	
	def get_form(self, **kwargs):
		# if request.user.is_staff: # condition
		user = self.get_object()
		if user.is_superuser:
			self.initial['is_superuser'] = 1
		else:
			self.initial['is_superuser'] = 2

		# print self.get_object().is_superuser

		# self.exclude = ('password',)
		return super(UserUpdate, self).get_form(**kwargs)

	def post(self, request, *args, **kwargs):
		# print self.request 

		self.object = self.get_object()
		form = self.get_form()
		email = self.request.POST.get('email')
		newUser = User.objects.filter(email=email)

		if newUser and newUser[0].id != self.object.id:
			raise form.ValidationError('please this email already exists')

		# if form.is_valid():

		view = super(UserUpdate, self).post(request, *args, **kwargs)
		# print view
		return view

	def get_success_url(self):
		isAdmin = self.get_object()
		if isAdmin.is_superuser or isAdmin.is_staff:
			return reverse('list_user')
		else:
			return reverse('list_site_user')

		

class UserDelete(DeleteView):
	template_name='admin/user_confirm_delete.html'
	form_class=UserForm

	def get_context_data(self,**kwargs):
		context=super(UserDelete,self).get_context_data(**kwargs)
		context['title']="User Delete"
		return context

	def get_object(self):
		user = User.objects.get(id=self.kwargs['id'])
		if self.request.user.id == user.id:
			user.same_user = True;
		else:
			user.same_user = False;
		return user

	def delete(self,request, *args, **kwargs):
		self.object = self.get_object()
		if self.request.user.id == self.object.id:
			raise Exception('you can not delete yourself')
		# success_url = self.get_success_url()
		self.object.delete()
		# user = self.object.id
		# print self.object.is_superuser

		# isAdmin = User.objects.filter(id=user,is_superuser=1)
		# print success_url
		if self.object.is_superuser :
			success_url = reverse('list_user')			
		else:
			success_url = reverse('list_site_user')
		
		return HttpResponseRedirect(success_url)

	def get_success_url(self):
		return reverse('list_user')

class AdminUserStatus(TemplateView):

		template_name='admin/confirm_status.html'

		def get_context_data(self,**kwargs):

			context = super(AdminUserStatus, self).get_context_data(**kwargs)
			context['title']='User Status'
			context['user_status'] = User.objects.get(id=self.kwargs['id'])	
			if self.request.user.id == context['user_status'].id:
				context['same_user'] = True;
			else:
				context['same_user'] = False;
			# print context['user_status'].id
			return context		

	
		def post(self, request, *args, **kwargs):
			user_status=User.objects.get(id=self.kwargs['id'])

			if user_status.is_active==0:
	
				user_status.is_active=1
			else:

				user_status.is_active=0

			user_status.save()

			return redirect('list_user')		

		def get_success_url(self):
			return reverse('list_user')	

class UserPasswordChange(TemplateView):

	# template_name='admin/confirm_status.html'
	template_name='admin/change_password.html'
	form_class=UserChangePasswordForm
	# form_class= PasswordChangeForm

	def get_context_data(self,**kwargs):

		context = super(UserPasswordChange, self).get_context_data(**kwargs)
		context['title']='Change Password'
		context['breadcrumbs'] = 'Change Password'
		context['form'] = UserChangePasswordForm(self.request.POST or None);
		# context['form'] = PasswordChangeForm(self.request.POST or None);
		# for fieldName in context['form'].fields:
		# 	context['form'].fields[fieldName].widget.attrs = {'class':'form-control','required': True}
		return context		

		
	def post(self,request,commit=True):
		print 'test post'
		form = UserChangePasswordForm(self.request.POST or None);
		# form = PasswordChangeForm(self.request.POST or None);
		print self.request.POST

		if form.is_valid():

			current_password = form.cleaned_data['current_password']
			new_password = form.cleaned_data['new_password']
			
			isPassCorrect = self.request.user.check_password(current_password)
			# user1 = User.objects.get(id=self.request.user.id)
			# user1.set_password('123456')
			# password = self.request.user.password
			print isPassCorrect
			if isPassCorrect:
				user = User.objects.get(id=self.request.user.id)
				user.set_password(new_password)
				user.save()
				update_session_auth_hash(request, user)
				messages.success(request, 'Your password was updated successfully!')
				# User.objects.filter(password=password,id=self.request.user.id).update(password=newPass)
				return redirect('change_password')
			else:
				print "incorrect pass"
				messages.warning(request, 'Incorrect Current Password')
				return redirect('change_password')
		else:
			messages.error(request, 'do not match the password',extra_tags='alert-danger')	
			return redirect('change_password')	
		# return render_to_response( self.template_name, {'form': form})
    
		def get_success_url(self):
			return reverse('list_user')	
