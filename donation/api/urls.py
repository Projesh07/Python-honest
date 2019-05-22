from django.conf.urls import url , include
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt
from api import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    # url(r'^admin/', admin.site.urls),

    url(r'^v1/categories/',  include('category.urls')),
    url(r'^v1/campaigns/',  include('campaign.urls')),
    url(r'^v1/users/',  include('users.urls')),
    url(r'^v1/report/',  include('report.urls')),
    url(r'^v1/contact-form/$',  csrf_exempt(views.email_client) , name="send_contact_message"),
    # url(r'^v1/comment/$', views.CommentViewSet, name="send_comment_message"),
    url(r'^v1/documentation/', schema_view),

]

# urlpatterns = format_suffix_patterns(urlpatterns)

# url(r'^create_user/$',  UserCreate.as_view(),name="create_user"),
# 	url(r'^update_user/(?P<id>[0-9]+)/$',  UserUpdate.as_view(),name="update_user"),
# 	url(r'^delete_user/(?P<id>[0-9]+)/$',  UserDelete.as_view(),name="delete_user"),
