from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from django.views.generic import *

from .views import *

urlpatterns = patterns('',
    url(r'^upload/$', login_required(RawImageCreateView.as_view()), name = 'rawdata.upload'),
    url(r'^plans/$', TemplateView.as_view(template_name='rawdata/plans.html'), name = 'rawdata.plans'),
)
