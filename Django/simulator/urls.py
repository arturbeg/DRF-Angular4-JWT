from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from sim.views import work
from django.contrib import admin
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views

router = routers.DefaultRouter()


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
	url(r'^api/admin/', admin.site.urls),
    url(r'^api/users', work.UserViewSet),
    url(r'^api/group', work.GroupViewSet),
    url(r'^api/gainer', work.Gainer),
    url(r'^api/data', work.data),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)