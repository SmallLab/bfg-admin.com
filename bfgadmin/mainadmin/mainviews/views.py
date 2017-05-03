from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.base import TemplateView
from django.contrib.auth.models import Permission, User

#Class MainView  - start page
class MainView(LoginRequiredMixin, TemplateView):

   template_name = 'index.html'

#Class UsersWork  - users page
class UsersWork(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):

   permission_required = "auth.change_user"
   template_name = 'users.html'
   login_url = '/'