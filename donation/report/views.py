from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from campaign.models import Campaign,Donate,SocialShare
from django.db.models import Sum
import datetime
import calendar

class HomeReport(APIView):
    #renderer_classes = (JSONRenderer, )
    def get(self,request,format=None):
        campaign_count = Campaign.objects.count()
        target_fund = Campaign.objects.aggregate(total=Sum('amount'))
        raised_fund = Donate.objects.aggregate(total=Sum('amount'))
        total_donor = User.objects.filter(is_superuser=0,is_staff=0).count()
        content = {
            'total_campaign': campaign_count,
            'target_fund':target_fund['total'],
            'raised_fund':raised_fund['total'],
            'total_donor':total_donor

        }
        return Response(content)

class CategoryReport(APIView):

    def get(self,request,pk,format=None):
        campaign_count = Campaign.objects.filter(category_id=pk).count()
        target_fund = Campaign.objects.filter(category_id=pk).aggregate(total=Sum('amount'))
        raised_fund = Donate.objects.filter(campaign__category_id=pk).aggregate(total=Sum('amount'))
        total_donor = User.objects.filter(is_superuser=0,is_staff=0).count()
        content = {
            'total_campaign': campaign_count,
            'target_fund':target_fund['total'],
            'raised_fund':raised_fund['total'],
            'total_donor':total_donor

        }
        return Response(content)


class CampaignReport(APIView):

    def get(self,request,pk,format=None):
        today = datetime.date.today()
        _, num_days = calendar.monthrange(today.year, today.month)
        first_day = datetime.date(today.year, today.month, 1)
        last_day = datetime.date(today.year, today.month, num_days)
        target_fund = Campaign.objects.filter(id=pk)
        raised_fund = Donate.objects.filter(campaign_id=pk).aggregate(total=Sum('amount'))
        total_donor = Donate.objects.filter(campaign_id=pk).count()
        monthly_donor = Donate.objects.filter(created_at__gte=first_day,created_at__lte=last_day).count()
        content = {
            'target_fund':target_fund[0].amount,
            'raised_fund':raised_fund['total'],
            'total_donor':total_donor,
            'monthly_donor':monthly_donor

        }
        return Response(content)

class CampaignSocialReport(APIView):

    def get(self,request,pk,format=None):
        facebook = SocialShare.objects.filter(campaign_id=pk,social_network='facebook').aggregate(total=Sum('count'))
        google = SocialShare.objects.filter(campaign_id=pk,social_network='google').aggregate(total=Sum('count'))
        twitter = SocialShare.objects.filter(campaign_id=pk,social_network='twitter').aggregate(total=Sum('count'))
        linkdin = SocialShare.objects.filter(campaign_id=pk,social_network='linkdin').aggregate(total=Sum('count'))
        content = {
            'facebook':facebook['total'] if facebook['total'] != None else 0,
            'google':google['total'] if google['total'] != None else 0,
            'twitter':twitter['total'] if twitter['total'] != None else 0,
            'linkdin':linkdin['total'] if linkdin['total'] != None else 0

        }
        return Response(content)


