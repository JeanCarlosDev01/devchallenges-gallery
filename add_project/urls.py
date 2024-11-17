from django.urls import path
from add_project.views import register_project

urlpatterns = [
    path('', register_project, name='register')
]
