from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.db.models import *

import datetime

def customDateSerialize(o):
    if isinstance(o, datetime.date):
        return o.__str__()

class HomePageView(TemplateView):

    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        # teachers = Teachers.objects.all()
        # groups = GroupsSchool.objects.all()

        context = {'teachers': None, 'groups': None}

        return context

class TeacherPageView(TemplateView):

    template_name = "pages/teachers/list.html"

    def get_context_data(self, **kwargs):
        # teachers = Teachers.objects.all()
        # groups = GroupsSchool.objects.all()

        context = {'teachers': None, 'groups': None}

        return context

class StudentPageView(TemplateView):

    template_name = "pages/students/list.html"

    def get_context_data(self, **kwargs):
        # teachers = Teachers.objects.all()
        # groups = GroupsSchool.objects.all()

        context = {'teachers': None, 'groups': None}

        return context