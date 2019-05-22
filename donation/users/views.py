from rest_framework 			import generics,status
from django.contrib.auth.models import User
from campaign.models 			import Donate
from users.serializers 			import UserDetailsSerializer,UserProfileSerializer
from users.serializers 			import UsersListSerializer
from users.serializers 			import PaymentHistoryOfUserSerializer
from api.permissions            import IsOwner
from django.shortcuts           import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAuthenticated,
    )
from rest_framework.response import Response
from django.db.models import Sum
import json
from users.models import Profile
from rest_framework.parsers import FileUploadParser
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FormParser
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,IsOwner,)
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj

class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()

    serializer_class = UsersListSerializer

class PaymentHistoryOfUser(generics.ListAPIView):

    permission_classes = (IsAuthenticated,IsOwner,)
    serializer_class = PaymentHistoryOfUserSerializer

    def get_queryset(self):
        return Donate.objects.filter(user_id=self.request.user.id)


class UserDonationReport(APIView):
    permission_classes = (IsAuthenticated,IsOwner,)

    def get(self,format=None):
        donations= Donate.objects.filter(user_id=self.request.user.id)
        total_donation_count = donations.count()
        total_donations = Donate.objects.filter(user_id=self.request.user.id).aggregate(total=Sum('amount'))
        total_campaign_counnt = donations.values('campaign_id').distinct().count()
        content = {
            'total_donation_count':total_donation_count ,
            'total_campaign_counnt':total_campaign_counnt,
            'total_donation':total_donations['total'] if total_donations['total'] != None else 0

        }
        return Response(content)

class UserUpdate(APIView):
    permission_classes =(IsOwner,IsAuthenticated,)

    def post(self,request):
        data = json.loads(request.POST.dict().keys()[0])
        firstname=data['firstname']
        lastname=data['lastname']
        user =request.user
        user.first_name=firstname
        user.last_name=lastname
        user.save()
        result =UserDetailsSerializer(user)
        return Response(result.data,status=status.HTTP_200_OK)

class UserUploadProfileImage(APIView):
    permission_classes =(IsOwner,IsAuthenticated,)
    parser_classes = (MultiPartParser, )
    def post(self,request):
        file = request.data['file']
        profile = Profile.objects.filter(user_id=request.user.id)
        if profile.exists():
            is_private=profile[0].is_private
            profile.delete()
            profile = Profile.objects.create(user_id=request.user.id,image=file,is_private=is_private)
        else:
            profile = Profile.objects.create(user_id=request.user.id,image=file)


        result = UserProfileSerializer(profile)
        return Response(result.data,status=status.HTTP_200_OK)

class UserVisibilityUpdate(APIView):
    permission_classes = (IsOwner,IsAuthenticated,)

    def post(self,request):
        user=request.user
        data = json.loads(request.POST.dict().keys()[0])
        is_private=data['is_private']
        profile = Profile.objects.filter(user_id=user.id)
        if profile.exists():
            profile.update(is_private=is_private)
        else:
            Profile.objects.create(user_id=request.user.id,is_private=is_private)

        return Response(True,status=status.HTTP_200_OK)

