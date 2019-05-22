from django.conf.urls import url
from .views.dashboard_view import DashboardView
from .views.login_view import LoginView
from .views.login_view import LogoutView
from .views.admin_view import UserList,UserCreate,UserUpdate,UserDelete,UserTableList,AdminUserStatus,UserPasswordChange
from .views.siteuser_view import SiteUserList,SiteUserCreate,SiteUserUpdate,SiteUserDelete,SiteUserStatus,SiteUserTableList
from .views.category_view import (CategoryList,CategoryCreate,
	CategoryUpdate,CategoryDelete,CategoryTableList,AJAXCategoryDocumentDelete)

from .views.campaign_view import *

from campaign.forms.campaign_forms import CampaignForm, CampaignForm2

from django.contrib.auth.decorators import login_required
urlpatterns = [

    # url(r'^admin/', admin.site.urls),
    url(r'^$',  LoginView.as_view()),
    url(r'^logout/$',  LogoutView.as_view(),name="logout"),
    url(r'^dashboard/$',login_required(DashboardView.as_view()),name="dashboard"),

    #Admin user admin panel
    url(r'^list-user/$',  login_required(UserList.as_view()),name="list_user"),
    url(r'^create-user/$',login_required(UserCreate.as_view()),name="create_user"),
    url(r'^update-user/(?P<id>[0-9]+)/$',login_required(UserUpdate.as_view()),name="update_user"),
    url(r'^delete-user/(?P<id>[0-9]+)/$',login_required(UserDelete.as_view()),name="delete_user"),
    url(r'^change-password/$',login_required(UserPasswordChange.as_view()),name="change_password"),

    #Category admin panel
	url(r'^list-category/$',  login_required(CategoryList.as_view()),name="list_category"),
	url(r'^create-category/$',  login_required(CategoryCreate.as_view()),name="create_category"),
	url(r'^update-category/(?P<id>[0-9]+)/$',  login_required(CategoryUpdate.as_view()),name="update_category"),
	url(r'^delete-category/(?P<id>[0-9]+)/$', login_required(CategoryDelete.as_view()),name="delete_category"),


    #Campaign Admin panle

    url(r'^list-campaign/$',  login_required(CampaignList.as_view()),name="list_campaign"),
    url(r'^create-campaign/$', login_required(CampaignCreate.as_view()),name="create_campaign"),
    url(r'^update-campaign/(?P<id>[0-9]+)/$',  login_required(CampaignUpdate.as_view()),name="update_campaign"),
    url(r'^update-campaign-photos/(?P<id>[0-9]+)/$',  login_required(CampaignUpdatePhotos.as_view()),name="update_campaign_photos"),
    url(r'^delete-campaign/(?P<id>[0-9]+)/$', login_required(CampaignDelete.as_view()),name="delete_campaign"),
    url(r'^campaign-status/(?P<id>[0-9]+)/$', login_required(CampaignStatus.as_view()),name="campaign_status"),   
    url(r'^campaign-details/(?P<pk>[0-9]+)/$', login_required(CampaignDetails.as_view()),name="campaign_details"),        
    #url (r'^contact/$', ContactWizard.as_view())),access_status



    #SiteUser Admin panel
    url(r'^list-site-user/$',  login_required(SiteUserList.as_view()),name="list_site_user"),
    url(r'^create-site-user/$',login_required(SiteUserCreate.as_view()),name="create_site_user"),
    url(r'^update-site-user/(?P<id>[0-9]+)/$',login_required(SiteUserUpdate.as_view()),name="update_site_user"),
    url(r'^delete-site-user/(?P<id>[0-9]+)/$',login_required(SiteUserDelete.as_view()),name="delete_site_user"),
    url(r'^access-status/(?P<id>[0-9]+)/$', login_required(SiteUserStatus.as_view()),name="access_status"), 
    url(r'^admin-access-status/(?P<id>[0-9]+)/$', login_required(AdminUserStatus.as_view()),name="admin_access_status"), 

    #Payment History Admin panel
    url(r'^payment-campaign-list/(?P<campaign>[0-9]+)/$',  login_required(PaymentList.as_view()),name="payment_campaign_list"),
    url(r'^payment-user/(?P<user>[0-9]+)/$',  login_required(PaymentList.as_view()),name="payment_user_list"),
    # url(r'^payment-user/$',  login_required(PaymentList.as_view()),name="payment_user"),
    url(r'^payment-campaign/$',  login_required(PaymentList.as_view()),name="payment_campaign"),
    url(r'^highlighted-campaigns/$',  login_required(HighlightedCampaignList.as_view()),name="highlighted_campaign_list"),
    
    url(r'^category-table-data$', CategoryTableList.as_view(), name='category_table_data'),
    url(r'^ajax-user-table-data$', UserTableList.as_view(), name='ajax_user_table_data'),
    url(r'^ajax-site-user-table-data$', SiteUserTableList.as_view(), name='ajax_site_user_table_data'),
    url(r'^ajax-campaign-table-data$', CampaignTableList.as_view(), name='ajax_campaign_table_data'),
    url(r'^ajax-highlighted-campaign-table-data$', HighlightedCampaignTableList.as_view(), name='ajax_highlighted_campaign_table_data'),
    url(r'^ajax-payment-table-data$', PaymentList.as_view(), name='ajax_payment_table_data'),
    url(r'^ajax-document-delete$', AJAXDocumentDelete.as_view(), name='ajax_document_delete'),
    url(r'^ajax-category-document-delete$', AJAXCategoryDocumentDelete.as_view(), name='ajax_category_document_delete'),
]

