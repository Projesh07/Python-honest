
from rest_framework import generics,status
from campaign.serializers import CampaignSerializer
from campaign.serializers import CampaignListSerializer
from campaign.serializers import CampaignHighlightedSerializer
from campaign.serializers import DocumentSerializer
from campaign.serializers import CampaignByCategorySerializer
from campaign.serializers import TagListByCampaignSerializer
from campaign.serializers import CommentsFromCampaignSerializer
from campaign.serializers import TopOrRecentDonationsSerializer
from campaign.serializers import DonateToCampaignSerializer
from campaign.serializers import TagSerializer
from campaign.serializers import UserDetailsSerializer,RelatedCampaignSerializer
from campaign.serializers import CampaignSocialShareSerializer
# from campaign.serializers import CampaignHasTagsSerializer
from django.contrib.auth.models import User
from campaign.models import Campaign
from campaign.models import Comments
from campaign.models import Documents
from campaign.models import Donate,SocialShare

from rest_framework.views import APIView

from api.permissions import IsOwner
# from campaign.models import CampaignsHasTags
from campaign.models import Tag
import json
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,

    )
    
class CampaignList(generics.ListCreateAPIView):

    # permission_classes = (IsAuthenticated,)
    
    serializer_class = CampaignListSerializer
    
    def get_queryset(self):
        category_id = self.request.GET.get('category_id')
        search_keyword = self.request.GET.get('q')
        if category_id:
            return Campaign.objects.filter(status=1,category_id=category_id)
        elif search_keyword:
            # serializer_class = CampaignSerializer
            return Campaign.objects.filter(title__contains = search_keyword)
        else:
            # serializer_class = CampaignListSerializer
            return Campaign.objects.filter(status=1)

    # queryset = Campaign.objects.filter(status=1)


class HighlightedCampaignList(generics.ListAPIView):

    # permission_classes = (IsAuthenticated,)
    
    serializer_class = CampaignHighlightedSerializer
    
    def get_queryset(self):
        return Campaign.objects.filter(status=1,is_highlighted=1,documents__is_featured=True)

    # queryset = Campaign.objects.filter(status=1)

class DocumentList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)


    def get_queryset(self,**kwargs):
        try:
            campaign_id = self.kwargs['campaign_id']
        except KeyError:
            campaign_id = None
      
        # campaign_id = self.kwargs['campaign_id']
        # print campaign_id
        return Documents.objects.filter(campaign_id=campaign_id)

    serializer_class = DocumentSerializer

class CampaignDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,IsOwner)

    queryset = Campaign.objects.filter(status=1)
    serializer_class = CampaignSerializer
    lookup_field = 'slug'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

class CampaignDetailByCategory(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
    	
        category_id = self.kwargs['category_id']
    	
        return Campaign.objects.filter(category__id=category_id,status=1)

    serializer_class = CampaignByCategorySerializer

class TagListByCampaign(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        
        campaign_id = self.kwargs['campaign_id']
        
        return Campaign.objects.filter(id=campaign_id)
        # return CampaignsHasTags.objects.all()

    # queryset = CampaignsHasTags.objects.prefetch_related('tags');

    serializer_class = TagListByCampaignSerializer


class TagList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)    

    queryset = Tag.objects.all()

    serializer_class = TagSerializer

class CommentsFromCampaign(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)

    serializer_class = CommentsFromCampaignSerializer

    def get_queryset(self):
        try:
            campaign_id = self.kwargs['campaign_id']
        except KeyError:
            campaign_id = None
        return Comments.objects.filter(campaign_id=campaign_id).order_by('-comment_at')

    def create(self, request, *args, **kwargs):
        data = json.loads(request.POST.dict().keys()[0])
        campaign_id=data['campaign_id']
        comment=data['comment']
        comment = Comments.objects.create(campaign_id=campaign_id,user=request.user,comment=comment)
        result =CommentsFromCampaignSerializer(comment)
        return Response(result.data,status=status.HTTP_201_CREATED)


class DonateToCampaign(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = DonateToCampaignSerializer

    def get_queryset(self):
        campaign_id = self.kwargs['campaign_id']
        return Donate.objects.filter(campaign_id=campaign_id)

        
    def perform_create(self, serializer):
        # print(self.request.POST.get('campaign'))
        if serializer.is_valid():
            serializer.save(user_id = self.request.user.id,campaign_id = int(self.kwargs['campaign_id']) )

class CampaignSocialShare(generics.ListCreateAPIView):
    serializer_class = CampaignSocialShareSerializer

    def get_queryset(self):
        campaign_id = self.kwargs['campaign_id']
        return SocialShare.objects.filter(campaign_id=campaign_id)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(campaign_id = int(self.kwargs['campaign_id']))

    # if request.method == 'POST':



class TopDotanationsOfCampaign(generics.ListAPIView):
# class TopDotanationsOfCampaign(APIView):
    # permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        campaign_id=self.request.query_params.get('campaign_id',None)
        if campaign_id:
            return Donate.objects.filter(campaign_id=campaign_id).order_by('-amount')[0:5]

        else:
            return Donate.objects.all().order_by('-amount')[0:5]    

    # queryset = Donate.objects.all().order_by('-amount')[0:5]

    serializer_class = TopOrRecentDonationsSerializer
    
class RecentDotanationsOfCampaign(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,) 

    def get_queryset(self):
        campaign_id=self.request.query_params.get('campaign_id', None)
        # campaign_id=self.request.GET.get('campaign_id', None)
        if campaign_id:

            return Donate.objects.filter(campaign_id=campaign_id).order_by('-donate_at')
        else:
            return Donate.objects.all().order_by('-donate_at')[0:5]


    # queryset = Donate.objects.all().order_by('-donate_at')[0:5]

    serializer_class = TopOrRecentDonationsSerializer 

class RelatedCampaignList(generics.ListAPIView):

    serializer_class = RelatedCampaignSerializer

    def get_queryset(self):
        campaign_id = self.request.query_params.get("campaign_id",None)
        if campaign_id:
           campaign = Campaign.objects.filter(id=campaign_id)
           if campaign.exists():
               category_id = campaign[0].category_id
               return Campaign.objects.filter(category_id=category_id).exclude(id=category_id)

