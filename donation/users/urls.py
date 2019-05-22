from django.conf.urls import url , include
from rest_framework.urlpatterns import format_suffix_patterns
from users import views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',  views.UserList.as_view(), name="user_list"),
    
    url(r'^details/$',views.UserDetail.as_view(),name="user_details"),
    url(r'^donations/$',views.PaymentHistoryOfUser.as_view(),name="user_donation_history"),
    url(r'^donations/report/$',views.UserDonationReport.as_view(),name="user_donation_report"),
    url(r'^update/$',views.UserUpdate.as_view(),name="user_update"),
    url(r'^upload-profile-image/$',views.UserUploadProfileImage.as_view(),name="user_image_upload"),
    url(r'^change-visibility/$',views.UserVisibilityUpdate.as_view(),name="user_change_visibility"),

]