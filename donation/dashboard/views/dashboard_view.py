
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views.generic import TemplateView
from django.views import View
from django.conf import settings
from campaign.models import Campaign,Tag,Documents,Category,Donate
from django.contrib.auth.models import User
import datetime

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
	)
class DashboardView(TemplateView):

	template_name='dashboard/dashboard.html'
	
	def get_context_data(self,**kwargs):
		user=User.objects.all()
		context = super(DashboardView, self).get_context_data(**kwargs)
		context['data'] =user
		context['num_campaign'] =(Campaign.objects.all()).count()
		context['num_donation'] =Donate.total_donate_number(condition=None,id_val=None)
		context['total_donate'] = Donate.total_donate(condition=None,id_val=None)
		# context['total_donate'] =Donate.total_donate_number(condition='campaign',id_val=self.kwargs['campaign'])
		context['this_month'] = datetime.datetime.now().strftime('%B %Y')
		today_date = datetime.datetime.now().strftime('%Y-%m-%d')
		print today_date
		context['ongoing_camp_total_donate'] = Donate.total_donate(condition='ongoing',id_val=None)
		context['ongoing_camp'] =(Campaign.objects.all().filter(status=1)).count()
		context['ongoing_camp_details'] = Campaign.objects.all().filter(status=1,start_date__lte=today_date,end_date__gte=today_date)

		# dtotal = 0.0
		# for camp in context['ongoing_camp_details']:
		# 	dtotal += camp.
		
		return context