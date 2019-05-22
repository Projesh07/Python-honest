from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Profile
from campaign.models import Donate
from campaign.serializers import CampaignInfoForDonationsSerializer,CampaignListSerializer
from rest_auth.registration.serializers import RegisterSerializer
import json

from allauth.account import app_settings as allauth_settings
from allauth.utils import (email_address_exists,get_username_max_length)

class UserProfileSerializer(serializers.ModelSerializer):
    # owner=serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Profile
        fields = ('id','image_url','is_private')


class UserDetailsSerializer(serializers.ModelSerializer):

	profile=UserProfileSerializer()


	class Meta:
		model = User
		fields = ('id','username','first_name','last_name','email','date_joined','profile',)
		# fields = '__all__'

class UsersListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username')


class PaymentHistoryOfUserSerializer(serializers.ModelSerializer):
    campaign    = CampaignListSerializer()
    # user        = UserDetailsForDotanationsSerializer();

    class Meta:
        model = Donate
        # fields = ('name')
        fields = ('id','amount','donate_at','campaign',)


class CustomRegisterSerializer(RegisterSerializer): 
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', '')
        }

    def save(self, request):
        # print self.first_name
        user = super(CustomRegisterSerializer, self).save(request)
        return user


