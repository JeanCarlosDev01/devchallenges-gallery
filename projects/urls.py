from django.urls import path
from projects.views import *

urlpatterns = [
    path('device-shop-checkout/', dsc_project, name='dsc_project'),
    path('pricing-table/', pt_project, name='pt_project'),
    path('meet-the-team-section/', mtts_project, name='mtts_project'),
    path('simple-feature-section/', sfs_project, name='sfs_project'),
    path('simple-article-listing/', sal_project, name='sal_project'),
    path('join-our-newsletter/', jon_project, name='sal_project'),
]
