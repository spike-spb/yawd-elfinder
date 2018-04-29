from django.urls import re_path, include
from django.contrib.admin.views.decorators import staff_member_required
from elfinder.views import ElfinderConnectorView

urlpatterns = [
    re_path(r'^yawd-connector/(?P<optionset>.+)/(?P<start_path>.+)/$',
        staff_member_required(ElfinderConnectorView.as_view()),
                              name='yawdElfinderConnectorView')
]
