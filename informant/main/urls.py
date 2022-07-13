from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('teachers/', TeacherPageView.as_view(), name='teachers'),
    path('students/', StudentPageView.as_view(), name='students'),
] 
