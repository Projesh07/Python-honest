from django import forms
from django.contrib.auth.models import User

USER_CHOICES = (
    ('unknown', 'Select Type'),
    (1, "Super User"),
    (0, "Staff")
)

class UserForm(forms.ModelForm):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':False}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','required': False}))
	first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))
	last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))
	is_superuser=forms.ChoiceField(choices = USER_CHOICES,widget=forms.Select(attrs={'class':'form-control','required': True}), label="User Type")
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required': False}))
	# confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required': False}))

	def __init__(self, *args, **kwargs):
		super(UserForm,self).__init__(*args, **kwargs)
		attrs={'class':'form-control','required': True}
		
		# self.fields['is_superuser'].empty_label  = 'Please select user type'
		# print int( self.instance.is_superuser )
		if self.instance and self.instance.pk:
			self.fields.pop('password', None)
			self.initial['is_superuser'] = int( self.instance.is_superuser )
		for field in self.fields.values():
			field.widget.attrs = attrs

	class Meta:
		model=User
		fields=['email','first_name','last_name','username','password','is_superuser']
		

	def save(self,commit=True):
		# email = self.cleaned_data['email'] 
		# print User.objects.get(email=email)
		# newUser = User.objects.get(email=email)

		# if newUser and newUser.email != self.cleaned_data['email']:
		# 	raise forms.ValidationError("please this email already exists")


		user=super(UserForm,self).save(commit=False)
		# print user.id;

		if self.instance and 'is_superuser' in self.cleaned_data:
			print 'before'
			print self.cleaned_data['is_superuser']
			if int(self.cleaned_data['is_superuser']) == 0:
				print 'after'
				user.is_superuser = 0
				user.is_staff = 1

		if self.instance and 'password' in self.cleaned_data:
			user.set_password(self.cleaned_data['password'])
		if commit and self.is_valid():
			user.save()
		return user	


class UserEditForm(forms.ModelForm):
	# username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':False}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','required': False}))
	first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))
	last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))
	is_superuser=forms.ChoiceField(choices = USER_CHOICES,widget=forms.Select(attrs={'class':'form-control','required': True})) 
	# password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required': False}))
	# confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required': False}))

	# def __init__(self, *args, **kwargs):
	# 	super(UserForm, self).__init__(*args, **kwargs)
	# 	# assign a (computed, I assume) default value to the choice field
	# 	self.initial['is_superuser'] = '1'

	class Meta:
		model=User
		fields=['email','first_name','last_name','is_superuser']
		

	def save(self,commit=True):
		email = self.cleaned_data['email'] 
		newUser = User.objects.get(email=email)
		# print self

		if newUser and newUser.email != self.cleaned_data['email']:
			raise forms.ValidationError("please this email already exists")

		user=super(UserEditForm,self).save(commit=False)
		# print user.id;

		# user.set_password(self.cleaned_data['password'])
		if commit and self.is_valid():
			user.save()
		return user	


class UserChangePasswordForm(forms.Form):
	current_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required': True}))
	new_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required': True}))
	confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required': True}))

	def __init__(self, *args, **kwargs):
		super(UserChangePasswordForm, self).__init__(*args, **kwargs)
		attrs={'class':'form-control','required': True}
		for field in self.fields.values():
			field.widget.attrs = attrs
		self.fields['current_password'].required = True
		self.fields['new_password'].required = True
		self.fields['confirm_password'].required = True

	def clean(self):
		print 'helios'
		if( self.cleaned_data.get('new_password') != self.cleaned_data.get('confirm_password')):
			raise forms.ValidationError("do not match the password")
		return self.cleaned_data
		
	# def save(self,request,commit=True):
	# 	print 'test post'
	# 	current_password = self.cleaned_data['current_password'] 
	# 	new_password = self.cleaned_data['new_password'] 

	# 	password = set_password(current_password);

	# 	user = User.objects.filter(password=password,id=self.request.user.id)

	# 	if user[0]:
	# 		newPass = set_password(new_password)
	# 		User.objects.filter(password=password,id=self.request.user.id).update(password=newPass)
			


	# def save(self,commit=True):
	# 	email = self.cleaned_data['email'] 
	# 	newUser = User.objects.get(email=email)
	# 	# print self

	# 	if newUser and newUser.email != self.cleaned_data['email']:
	# 		raise forms.ValidationError("please this email already exists")

	# 	user=super(UserEditForm,self).save(commit=False)
	# 	# print user.id;

	# 	# user.set_password(self.cleaned_data['password'])
	# 	if commit and self.is_valid():
	# 		user.save()
	# 	return user	









