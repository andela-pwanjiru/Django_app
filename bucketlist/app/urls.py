from django.conf.urls import url, include
from app.views import register_view, login_view, logout_view, index_view, bucketlist_view

urlpatterns = [
    url(r'^$', index_view.as_view(), name='index'),
    url(r'^register/$', register_view.as_view()),
    url(r'^login/$', login_view.as_view()),
    url(r'^logout/$', logout_view.as_view()),
    url(r'^bucketlists/$', bucketlist_view.as_view()),
    url(r'^api/', include('api.urls')),
]
